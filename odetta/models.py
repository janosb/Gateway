from __future__ import unicode_literals
from django.db import models
from django import forms
from odetta.helpers.lightcurve import lc_point

from numpy import genfromtxt
from numpy import interp
from numpy import linspace

from odetta.settings import RAW_DATA_DIR, RAW_DATA_ROOT


class PublicationsManager(models.Manager):
    def get_or_create_publication(self, publication_dict):
        try:
            publication = Publications.objects.get(shortname=publication_dict.get("shortname"))
            return publication, False
        except Publications.DoesNotExist:
            publication = self.model()
            for k, v in publication_dict.items():
                setattr(publication, k, v)
            return publication, True


class Publications(models.Model):
    modeltype = models.CharField(max_length=40, blank=True, verbose_name='Model Type')
    modeldim = models.IntegerField(verbose_name='Model Dimension')
    date_entered = models.DateField(verbose_name='Date Entered')
    citation = models.CharField(max_length=200, blank=True, verbose_name='Citation')
    type = models.CharField(max_length=10, blank=True, verbose_name='Type')
    fullname = models.CharField(max_length=200, blank=True)
    shortname = models.CharField(max_length=200, blank=True)
    is_public = models.BooleanField()
    summary = models.TextField()
    url = models.CharField(max_length=200, blank=True)
    data_urls = models.TextField(blank=True)

    objects = PublicationsManager()

    class Meta:
        db_table = 'publications'


class PublishedModelManager(models.Manager):
    def get_or_create_published_model(self, metadata, model_name):
        try:
            pm = PublishedModel.objects.get(metadata=metadata, name=model_name)
            return pm, False
        except PublishedModel.DoesNotExist:
            pm = self.model()
            pm.metadata = metadata
            pm.name = model_name
            return pm, True


class PublishedModel(models.Model):
    publication = models.ForeignKey('Publications')
    metadata = models.TextField(blank=False)
    name = models.CharField(max_length=30)
    objects = PublishedModelManager()

    class Meta:
        db_table = 'published_model'

    def has_mu(self):
        return self.spectra_set.distinct("mu").count() > 1

    def has_phi(self):
        return self.spectra_set.distinct("phi").count() > 1


class SpectraManager(models.Manager):
    def get_or_create_spectrum(self, model_id, t_expl, mu, phi):
        try:
            spec = Spectra.objects.get(t_expl=t_expl, mu=mu, phi=phi, published_model_id=model_id)
            return spec, False
        except Spectra.DoesNotExist:
            spec = self.model()
            spec.t_expl = t_expl
            spec.mu = mu
            spec.phi = phi
            return spec, True


class Spectra(models.Model):
    published_model = models.ForeignKey("PublishedModel")
    t_expl = models.FloatField(null=True, blank=True)
    mu = models.FloatField(null=True, blank=True)
    phi = models.FloatField(null=True, blank=True)

    b_landolt = models.FloatField(null=True, blank=True)
    r_landolt = models.FloatField(null=True, blank=True)
    i_landolt = models.FloatField(null=True, blank=True)
    ux_landolt = models.FloatField(null=True, blank=True)
    v_landolt = models.FloatField(null=True, blank=True)

    objects = SpectraManager()

    class Meta:
        db_table = 'spectra'

    # fill in the values for landolt filter lightcurve points
    def fill_in_lc(self, filters, wave, lum):
        print "filling in LC, %.2e" % lc_point(wave, lum, filters["b_wave"], filters["b_trans"])
        self.b_landolt = lc_point(wave, lum, filters["b_wave"], filters["b_trans"])
        self.r_landolt = lc_point(wave, lum, filters["r_wave"], filters["r_trans"])
        self.i_landolt = lc_point(wave, lum, filters["i_wave"], filters["i_trans"])
        self.ux_landolt = lc_point(wave, lum, filters["ux_wave"], filters["ux_trans"])
        self.v_landolt = lc_point(wave, lum, filters["v_wave"], filters["v_trans"])
        self.save()

    def add_fluxvals(self, rel_file_path, columns, header_lines, filters):
        try:
            full_path = RAW_DATA_ROOT+RAW_DATA_DIR+rel_file_path
            wave, lum, ph_ct = genfromtxt(full_path, skip_header=header_lines, usecols=columns, unpack=True)
            if len(wave) > 1000:
                old_wave = wave
                old_lum = lum
                old_ph = ph_ct
                wave = linspace(min(wave), max(wave), 1000)
                lum = interp(wave, old_wave, old_lum)
                ph_ct = interp(wave, old_wave, old_ph)
            for i in range(len(wave)):
                fluxes = Fluxvals.objects.get_or_create_fluxval(wave[i], lum[i], ph_ct[i])
                self.fluxvals_set.add(fluxes)
            self.fill_in_lc(filters, wave, lum)
        except IOError:
            print "Failed to open file: %s" % full_path


class FluxvalsManager(models.Manager):
    def get_or_create_fluxval(self, wave, lum, ph_ct):
        fval = self.model()
        fval.wavelength = wave
        fval.luminosity = lum
        fval.photon_count = ph_ct
        return fval


class Fluxvals(models.Model):
    spectrum = models.ForeignKey('Spectra')
    wavelength = models.FloatField()
    luminosity = models.FloatField(null=True, blank=True)
    photon_count = models.FloatField(null=True, blank=True)

    objects = FluxvalsManager()

    class Meta:
        db_table = 'fluxvals'


class MetaDd2D(models.Model):
    model_id = models.IntegerField(primary_key=True)
    pub_id = models.IntegerField()
    modelname = models.CharField(max_length=40, blank=True)
    mass_wd = models.FloatField(null=True, blank=True)
    percent_carbon = models.FloatField(null=True, blank=True)
    percent_oxygen = models.FloatField(null=True, blank=True)
    n_ignit = models.IntegerField(null=True, blank=True)
    r_min_ignit = models.FloatField(null=True, blank=True)
    cos_alpha = models.FloatField(null=True, blank=True)
    stdev = models.FloatField(null=True, blank=True)
    ka_min = models.FloatField(null=True, blank=True)
    rho_min = models.FloatField(null=True, blank=True)
    rho_max = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'meta_dd2d'



class MetaNsm1D(models.Model):
    pub_id = models.IntegerField()
    model_id = models.IntegerField(primary_key=True)
    modelname = models.CharField(max_length=40, blank=True)
    m_ej = models.FloatField(null=True, blank=True)
    beta = models.FloatField(null=True, blank=True)
    n = models.FloatField(null=True, blank=True)
    delta = models.FloatField(null=True, blank=True)
    composition = models.CharField(max_length=4)

    class Meta:
        db_table = 'meta_nsm1d'


class MetaPi1D(models.Model):
    pub_id = models.IntegerField()
    model_id = models.IntegerField(primary_key=True)
    modelname = models.CharField(max_length=15, blank=True)
    t_expl = models.FloatField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True)
    star_type = models.CharField(max_length=2)

    class Meta:
        db_table = 'meta_pi1d'


class LightCurves(models.Model):
    model_id = models.IntegerField()
    lc_id = models.IntegerField(primary_key=True)
    theta = models.FloatField(null=True, blank=True)
    phi = models.FloatField(null=True, blank=True)
    b_lan_max = models.FloatField(null=True, blank=True)
    r_lan_max = models.FloatField(null=True, blank=True)
    i_lan_max = models.FloatField(null=True, blank=True)
    ux_lan_max = models.FloatField(null=True, blank=True)
    v_lan_max = models.FloatField(null=True, blank=True)
    t_b_lan_max = models.FloatField(null=True, blank=True)
    t_r_lan_max = models.FloatField(null=True, blank=True)
    t_i_lan_max = models.FloatField(null=True, blank=True)
    t_ux_lan_max = models.FloatField(null=True, blank=True)
    t_v_lan_max = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'lightcurves'

class LCVals(models.Model):
    lc_id = models.IntegerField(primary_key=True)
    t_expl = models.IntegerField()
    b_landolt = models.FloatField(null=True, blank=True)
    r_landolt = models.FloatField(null=True, blank=True)
    i_landolt = models.FloatField(null=True, blank=True)
    ux_landolt = models.FloatField(null=True, blank=True)
    v_landolt = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'lcvals'


def get_time_max(model_id):
    return Spectra.objects.filter(published_model_id=model_id).values("t_expl").distinct("t_expl").order_by("t_expl").count() - 1


def get_mu_max(model_id):
    return Spectra.objects.filter(published_model_id=model_id).values("mu").distinct("mu").order_by("-mu").count() - 1


def get_phi_max(model_id):
    return Spectra.objects.filter(published_model_id=model_id).values("phi").distinct("phi").order_by("-phi").count() - 1


def get_time_val(model_id):
    times = []
    for time in Spectra.objects.filter(published_model_id=model_id).values("t_expl").distinct("t_expl").order_by("t_expl"):
        times.append(time["t_expl"]) 
    return times


def get_mu_val(model_id):
    mu_steps = []
    for mu in Spectra.objects.filter(published_model_id=model_id).values("mu").distinct("mu").order_by("mu"):
        mu_steps.append(mu["mu"]) 
    return mu_steps


class SearchForm(forms.Form):
    min_mass = forms.IntegerField(required=False, label='Minimum Mass')
    max_mass = forms.IntegerField(required=False, label="Maximum Mass")
    max_lum = forms.IntegerField(required=False, label="Peak Luminosity")



class Chi2Test(models.Model):
    fname = models.CharField(max_length=200, blank=True)
    chi2dof = models.FloatField(null=True, blank=True)
    chi2dof_bin = models.FloatField(null=True, blank=True)
    dof = models.IntegerField(null=True, blank=True)
    dofb = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'chi2test'
