from django.http import HttpResponse, Http404
from odetta.models import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pylab as pl
from django.shortcuts import render_to_response, redirect, get_object_or_404
import simplejson
from django.forms.models import model_to_dict
from odetta_utils import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files import File
from odetta.settings import FITS_ROOT, HOME_URL, DATA_DIR, TEMPPASSWORD
import zipfile
import glob,os
import re
import StringIO
import numpy as np
from odetta.odetta_wrappers import oplot_process
from django.core.servers.basehttp import FileWrapper



#from simple_chi2 import *


def home_page(request):
    return render_to_response('base.html', context_instance=RequestContext(request, {"home_url": HOME_URL}))


def browse(request, pub_id=None):
    authenticated = True
    listing = []
    breadcrumbs = [{"name": "Publications", "url": reverse("odetta.views.browse")}]
    if pub_id:
        pub = Publications.objects.get(pub_id=pub_id)
        validated = pub.is_public
        breadcrumbs.append({
            "name": pub.shortname,
            "url": reverse("odetta.views.browse", kwargs={"pub_id": pub_id}),
            "active": True,
        })
        metatype = pub.metatype[:4].title() + pub.metatype[5:-1].title() + pub.metatype[-1:].upper()
        data = eval(metatype).objects.filter(pub_id=pub_id).order_by("model_id")
        for model in data:
            details = ""
            for field_name in model._meta.get_all_field_names():
                field = model._meta.get_field(field_name)
                if field_name not in ['modelname', 'model_id', 'pub_id']:
                    details += "%s: %s; " % (field.verbose_name, model.__dict__[field_name])
            listing.append({
                "obj": model,
                "name": model.modelname,
                "url": reverse("odetta.views.plot", kwargs={"model_id": model.model_id}),
                "details": details
            })
    else:
        if authenticated:
            data = Publications.objects.all().order_by("fullname")        
        else: 
            data = Publications.objects.filter(is_public = True).order_by("fullname")
        breadcrumbs = [{"name": "Publications", "url": reverse("odetta.views.browse"), "active": True}]
        for publication in data:
            details = ""
            data_urls = publication.data_urls.split(",")
            print data_urls
            data_url_names = [url.split(".")[0] for url in data_urls]
            print data_url_names
            data_urls_tuple = zip(data_urls, data_url_names)
            for field_name in publication._meta.get_all_field_names():
                field = publication._meta.get_field(field_name)
                if field_name not in ['modeltype','fullname','is_public','shortname',
                                      'pub_id', 'url', 'summary', 'metatype', 'data_urls']:
                    details += "%s: %s; " % (field.verbose_name, publication.__dict__[field_name])
            listing.append({
                "obj": publication,
                "name": publication.fullname,
                "data_urls": data_urls_tuple,
                "url": reverse("odetta.views.browse", kwargs={"pub_id": publication.pub_id}),
                "details": details
            })

    MAX_ENTRIES = 6

    page = request.GET.get("page", 1)
    pages = Paginator(listing, MAX_ENTRIES)
    try:
        results = pages.page(page)
    except PageNotAnInteger:
        results = pages.page(1)
    except EmptyPage:
        results = pages.page(pages.num_pages)

    # Creates a range of pages (like on the bottom of google search)
    page_range = []
    if results.number <= MAX_ENTRIES/2:
        page_range = pages.page_range[:MAX_ENTRIES]
    elif results.number >= pages.page_range[-1]-MAX_ENTRIES/2:
        page_range = pages.page_range[-MAX_ENTRIES:]
    else:
        page_range = range(results.number-4, results.number+5)

    # Creates a querystring without the page number
    temp = request.GET.copy()
    if temp.get("page"):
        temp.pop("page")
    query_string = temp.urlencode()

    return render_to_response('list_view.html',
                              {"results": results, "q_string": query_string, "page_range": page_range,
                               "breadcrumbs": breadcrumbs, "home_url": HOME_URL})

def search_models(request):
    results = []
    MAX_ENTRIES = 10
    if request.method == "GET" and len(request.GET):        
        # Deals with paging of search results
        if request.GET.get("minmass", False):
            minmass = int(request.GET.get("minmass"))
        else:
            minmass = 0
        if request.GET.get("maxmass",False):
            maxmass = int(request.GET.get("maxmass"))
        else:
            maxmass = float("inf")
        if request.GET.get("modeltype", False):
            modeltype = request.GET.get("modeltype")
        else:
            modeltype = ""
        page = request.GET.get("page", 1)
        result_list = []
        if modeltype:
            metaType = "Meta"
            temp = ""
            for word in modeltype.split(" "):
                temp += word[0].lower()
            try:
                metaType += (temp.title() + str(Publications.objects.get(fullname__icontains = modeltype).modeldim) + "D")
            except Exception:
                try:
                    metaType += str(Publications.objects.get(metatype__icontains=modeltype).metatype[5:-1].title() + "D")
                except Exception:
                    return render_to_response('search.html', {"error": "Invalid Model Type"},
                                              context_instance=RequestContext(request, {"home_url": HOME_URL}))

            metaobj = eval(metaType)
            try:
                object_list = metaobj.objects.filter(mass_wd__range=(minmass,maxmass))
            except Exception:
                return render_to_response('search.html',{"error":"Mass does not exist for that model"},
                                          context_instance=RequestContext(request, {"home_url": HOME_URL}))
            for model in metaobj.objects.filter(mass_wd__range=(minmass,maxmass)):
                result_list.append({"pub":Publications.objects.get(pub_id = model.pub_id),"model":model})
                pages = Paginator(result_list, MAX_ENTRIES)
        else:
            for model in MetaDd2D.objects.filter(mass_wd__range=(minmass,maxmass)):
                result_list.append({"pub":Publications.objects.get(pub_id = model.pub_id),"model":model})
                pages = Paginator(result_list, MAX_ENTRIES)
        try:
            results = pages.page(page)
        except PageNotAnInteger:
            results = pages.page(1)
        except EmptyPage:
            results = pages.page(pages.num_pages)

        # Creates a range of pages (like on the bottom of google search)
        page_range = []
        if results.number <= MAX_ENTRIES/2:
            page_range = pages.page_range[:MAX_ENTRIES]
        elif results.number >= pages.page_range[-1]-MAX_ENTRIES/2:
            page_range = pages.page_range[-MAX_ENTRIES:]
        else:
            page_range = range(results.number-4, results.number+5)

        # Creates a querystring without the page number
        temp = request.GET.copy()
        if temp.get("page"):
            temp.pop("page")
        query_string = temp.urlencode()

        return render_to_response('search.html', {"results": results, "page_range": page_range, "q_string": query_string},
                                  context_instance=RequestContext(request, {"home_url": HOME_URL}))
    return render_to_response('search.html', context_instance=RequestContext(request, {"home_url": HOME_URL}))


def plot(request, model_id):
    metatype = Spectra.objects.filter(model_id = model_id).distinct("model_id")[0].metatype[:4].title() + Spectra.objects.filter(model_id = model_id).distinct("model_id")[0].metatype[5:-1].title() + Spectra.objects.filter(model_id = model_id).distinct("model_id")[0].metatype[-1:].upper()
    meta_data = eval(metatype).objects.filter(model_id = model_id)[0]
    breadcrumbs = [{"name": "Publications", "url": reverse("odetta.views.browse")}]
    breadcrumbs.append({
        "name": Publications.objects.get(pub_id=meta_data.pub_id).shortname,
        "url": reverse("odetta.views.browse", kwargs={"pub_id": meta_data.pub_id}),
    })
    breadcrumbs.append({
        "name": meta_data.modelname,
        "url": reverse("odetta.views.plot", kwargs={"model_id": meta_data.model_id}),
        "active": True
    })

    # Creates a detail array for display on table below graph
    # Excludes the fields in the excludes array
    details = []
    for field in meta_data._meta.get_all_field_names():
        details.append((meta_data._meta.get_field(field).verbose_name, getattr(meta_data, field.__str__())))
    return render_to_response("spectrum_detail.html",
                              {"breadcrumbs":breadcrumbs, "details": details, "meta_data": meta_data,
                               "mu_max": get_mu_max(model_id), "time_max": get_time_max(model_id),
                               "phi_max":get_phi_max(model_id), "time_vals":get_time_val(model_id),
                               "mu_vals": get_mu_val(model_id), "summary": Publications.objects.get(pub_id = meta_data.pub_id).summary,
                               "url": Publications.objects.get(pub_id = meta_data.pub_id).url},
                              context_instance=RequestContext(request, {"home_url": HOME_URL}))
    # return render_to_response("spectrum_detail.html", {"details": details, "meta_data": meta_data}, context_instance=RequestContext(request))


def get_plot_data(request, model_id, time_step=0, mu_step=0, phi_step=0):
    spectra = Spectra.objects.filter(model_id=model_id)
    if spectra.count() <= 0:
        raise Http404

    try:
        all_time_steps = spectra.values("t_expl").distinct("t_expl").order_by("t_expl")
        t_expl = all_time_steps[int(time_step)]["t_expl"]
    except IndexError:
        return HttpResponse(simplejson.dumps({"success": False, "error": "time_step index out of bounds", "max_time_steps": all_time_steps.count()}), content_type="application/json")
    try:
        all_mu_steps = spectra.filter(t_expl=t_expl).values("mu").order_by("-mu")
        mu = all_mu_steps[int(mu_step)]["mu"]
    except IndexError:
        mu = 0
    try:
        all_phi_steps = spectra.filter(t_expl=t_expl).values("phi").order_by("-phi")
        phi = all_phi_steps[int(phi_step)]["phi"]
    except IndexError:
        phi = 0    

    # Gets the meta data based on the calculated mu and t_expl
    # Uses range to prevent floating point errors
    spec_data = spectra.get(mu__range=(mu-0.01, mu+0.01), t_expl__range=(t_expl-0.01, t_expl+0.01), phi__range=(phi-0.01, phi+0.01))

    # Populates a flux data array from the spec_id of the selected meta_data
    qset = Fluxvals.objects.filter(spec_id=spec_data.spec_id).order_by("wavelength")
    flux_data = []
    for rec in qset:
        flux_data.append({
            "x": rec.wavelength,  # Graph's X-Axis
            "y": rec.luminosity,  # Graph's Y-Axis
        })
    data = {
        "model_id": int(spec_data.model_id),
        "time_step": int(time_step),
        "t_expl": float(t_expl),
        "max_time_steps": all_time_steps.count()-1,
        "mu_step": int(mu_step),
        "mu": float(mu),
        "phi_step": int(phi_step),
        "phi": float(phi),
        "max_mu_steps": all_mu_steps.count()-1,
        "flux_data": flux_data,
    }
    return HttpResponse(simplejson.dumps(data), content_type="application/json")


def batch_time_data(request, model_id, mu_step, phi_step):
    model = Spectra.objects.filter(model_id=model_id)

    if model.count() <= 0:
        raise Http404

    try:
        all_mu_steps = model.values("mu").distinct("mu").order_by("-mu")
        mu = all_mu_steps[int(mu_step)]["mu"]
    except IndexError:
        mu = 0
    try:
        all_phi_steps = model.values("phi").distinct("phi").order_by("-phi")
        phi = all_phi_steps[int(phi_step)]["phi"]
    except IndexError:
        phi = 0


    meta_datas = model.filter(mu__range=(mu-0.01, mu+0.01)).filter(phi__range=(phi-0.01, phi+0.01)).order_by("t_expl")
    data = []
    index = 0
    for m in meta_datas:
        data.append({
            "time_step": int(index),
            "mu_step": int(mu_step),
            "phi_step": int(phi_step),
            "flux_data": [],
        })
        qset = Fluxvals.objects.filter(spec_id=m.spec_id).order_by("wavelength")
        for rec in qset:
            data[index]['flux_data'].append({
                "x": rec.wavelength,  # Graph's X-Axis
                "y": rec.luminosity,  # Graph's Y-Axis
            })
        index += 1
    return HttpResponse(simplejson.dumps(data), content_type="application/json")


def batch_mu_data(request, model_id, time_step, phi_step):
    model = Spectra.objects.filter(model_id=model_id)

    if model.count() <= 0:
        raise Http404

    try:
        all_time_steps = model.values("t_expl").distinct("t_expl").order_by("t_expl")
        t_expl = all_time_steps[int(time_step)]["t_expl"]
    except IndexError:
        return HttpResponse(simplejson.dumps({"success": False, "error": "time_step index out of bounds", "max_time_steps": all_time_steps.count()}), content_type="application/json")
    try:
        all_phi_steps = model.values("phi").distinct("phi").order_by("-phi")
        phi = all_phi_steps[int(phi_step)]["phi"]
    except IndexError:
        phi = 0

    meta_datas = model.filter(t_expl=t_expl).filter(phi__range=(phi-0.01, phi+0.01)).order_by("-mu")
    data = []
    index = 0
    for m in meta_datas:
        data.append({
            "time_step": int(time_step),
            "mu_step": int(index),
            "phi_step": int(phi_step),
            "flux_data": [],
        })
        qset = Fluxvals.objects.filter(spec_id=m.spec_id).order_by("wavelength")
        for rec in qset:
            data[index]['flux_data'].append({
                "x": rec.wavelength,  # Graph's X-Axis
                "y": rec.luminosity,  # Graph's Y-Axis
            })
        index += 1
    return HttpResponse(simplejson.dumps(data), content_type="application/json")

def batch_phi_data(request, model_id, time_step, mu_step):
    model = Spectra.objects.filter(model_id=model_id)

    if model.count() <= 0:
        raise Http404

    try:
        all_time_steps = model.values("t_expl").distinct("t_expl").order_by("t_expl")
        t_expl = all_time_steps[int(time_step)]["t_expl"]
    except IndexError:
        return HttpResponse(simplejson.dumps({"success": False, "error": "time_step index out of bounds", "max_time_steps": all_time_steps.count()}), content_type="application/json")
    try:
        all_mu_steps = model.values("mu").distinct("mu").order_by("-mu")
        mu = all_mu_steps[int(mu_step)]["mu"]
    except IndexError:
        mu = 0

    meta_datas = model.filter(t_expl=t_expl).filter(mu__range=(mu-0.01, mu+0.01)).order_by("-phi")
    data = []
    index = 0
    for m in meta_datas:
        data.append({
            "time_step": int(time_step),
            "mu_step": int(index),
            "phi_step": int(phi_step),
            "flux_data": [],
        })
        qset = Fluxvals.objects.filter(spec_id=m.spec_id).order_by("wavelength")
        for rec in qset:
            data[index]['flux_data'].append({
                "x": rec.wavelength,  # Graph's X-Axis
                "y": rec.luminosity,  # Graph's Y-Axis
            })
        index += 1
    return HttpResponse(simplejson.dumps(data), content_type="application/json")

def fitter(request):
    import random
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        search_option = request.POST.get("fitType")
        flux_data = oplot_process(file=None, model_id=39)
        matched_models = []
        data = {
            "flux_data": flux_data,
        }
        for x in range(10):
            rand = int(random.random() * 40 + 1)
            metatype = Spectra.objects.filter(model_id = rand).distinct("model_id")[0].metatype[:4].title() + Spectra.objects.filter(model_id = rand).distinct("model_id")[0].metatype[5:-1].title() + Spectra.objects.filter(model_id = rand).distinct("model_id")[0].metatype[-1:].upper()
            meta_data = eval(metatype).objects.filter(model_id = rand)[0]
            matched_models.append(meta_data)
        # fit(uploaded_file,search_option)
        # going to need an array of 10 models, so I can get model_ids in the template
        return render_to_response("fitter_results.html", {"data":flux_data, "matched_models":matched_models},
                                  context_instance=RequestContext(request, {"home_url": HOME_URL}))
    return render_to_response("fitter_form.html", context_instance=RequestContext(request, {"home_url": HOME_URL}))


def about(request):
    return render_to_response("about.html", context_instance=RequestContext(request, {"home_url": HOME_URL}))


def run_all_data(request, x2, y2, y2var):
    #get id's
    qset = Spectra.objects.distinct('model_id')
    m_id = [rec.m_id for rec in qset]
    print "There are " + len(m_id) + " spectra in DB. Running them all..."

    #get wavelengths
    qset2 = Spectra.objects.filter(model_id=1)
    waves = [rec.wavelength for rec in qset2]
    ##need to add something to make sure we have same grid for both spectra
    ##HERE

    output = []
    for id in m_id:
        wave = [rec.wavelength for rec in qset]
        lum = [rec.luminosity for rec in qset]
        [chi2, dof, a] = compute_chi2(waves, lum, y2, y2var)
        output.append([m_id, chi2, dof, a])

    response = HttpResponse(content_type='???')
    return response


def plot_img(request, model_id, time_step=0, mu_step=0, phi_step=0):
    model = Spectra.objects.filter(model_id=model_id)
    if model.count() <= 0:
        raise Http404

    try:
        all_time_steps = model.values("t_expl").distinct("t_expl").order_by("t_expl")
        t_expl = all_time_steps[int(time_step)]["t_expl"]
    except IndexError:
        return HttpResponse(simplejson.dumps({"success": False, "error": "time_step index out of bounds", "max_time_steps": all_time_steps.count()}), content_type="application/json")
    try:
        all_mu_steps = model.values("mu").distinct("mu").order_by("-mu")
        mu = all_mu_steps[int(mu_step)]["mu"]
    except IndexError:
        mu = 0
    try:
        all_phi_steps = model.values("phi").distinct("phi").order_by("-phi")
        phi = all_phi_steps[int(phi_step)]["phi"]
    except IndexError:
        phi = 0

    # Gets the meta data based on the calculated mu and t_expl
    # Uses range to prevent floating point errors
    meta_data = model.get(mu__range=(mu-0.01, mu+0.01), t_expl__range=(t_expl-0.01, t_expl+0.01))

    # Populates a flux data array from the spec_id of the selected meta_data
    qset = Fluxvals.objects.filter(spec_id=meta_data.spec_id).order_by("wavelength")
    wave = [rec.wavelength for rec in qset]
    lum = [rec.luminosity for rec in qset]
    spec_id = meta_data.spec_id
    ttle = 'Model '+str(spec_id)
    xl = 'Wavelength (A)'
    yl = 'Luminosity'

    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_title(ttle)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.plot(wave,lum)

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    if int(request.GET.get("download", 0)) == 1:
        response['Content-Disposition'] = 'attachment; filename="graph.png"'
    canvas.print_png(response)
    return response


def plot_few(request,id):
    qset = Spectra.objects.filter(model_id=id)
    wave = [rec.wavelength for rec in qset]
    lum = [rec.luminosity for rec in qset]
    ttle = 'Model '+str(id)
    xl = 'Wavelength (A)'
    yl = 'Luminosity'
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_title(ttle)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.plot(wave, lum)

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response



def text(request):
    return HttpResponse(simplejson.dumps({"foo":"bar","test":True}), content_type = "application/json")

def get_zip_file(request):
    string_file = StringIO.StringIO()
    zipped_file = zipfile.ZipFile(string_file, 'w', compression=zipfile.ZIP_DEFLATED)
    for content in glob.glob(FITS_ROOT + "/*"):
        zipped_file.write(content, os.path.basename(content),zipfile.ZIP_DEFLATED)
    zipped_file.close()
    contents = string_file.getvalue()
    response = HttpResponse(contents, content_type='application/x-zip-compressed')
    response['Content-Disposition'] = 'attachment; filename=blarg.zip'
    return response
    
def upload(request, model_id):
    return render_to_response("upload.html", {"model_id":model_id}, context_instance=RequestContext(request, {"home_url": HOME_URL}))


def ajax_overplot(request, model_id):
    flux_data = oplot_process(file=None, model_id=model_id)
    data = {
        "flux_data": flux_data,
    }
    return HttpResponse(simplejson.dumps(data), content_type="application/json")


def download(request, filename):
    if not re.search("[a-zA-Z_.]+.(tar|zip|gz)", filename):
        print "no match for filename "+filename
        return HttpResponse()
    try:
        wrapper = FileWrapper(file(DATA_DIR+filename))
        response = HttpResponse(wrapper, content_type='multipart/x-gzip')
        response['Content-Disposition'] = 'attachment; filename=\"'+filename+'\"'
    except IOError:
        print "unable to open file: " + filename
        response = HttpResponse("Unable to locate your file.")
    return response