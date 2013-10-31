from django.conf.urls import patterns, include, url
from odetta.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home_page),
    url(r'^plot/(?P<model_id>\d+)/(?P<time_step>\d+)/(?P<mu_step>\d+)/(?P<phi_step>\d+)/img/$', plot_img),
    url(r'^plot/(?P<model_id>\d+)/$', plot),
    url(r'^ajax/plot/(?P<model_id>\d+)/upload/$', upload),
    url(r'^ajax/plot/(?P<model_id>\d+)/(?P<time_step>\d+)/$', get_plot_data),
    url(r'^ajax/plot/(?P<model_id>\d+)/(?P<time_step>\d+)/(?P<mu_step>\d+)/$', get_plot_data),
    url(r'^ajax/plot/(?P<model_id>\d+)/(?P<time_step>\d+)/(?P<mu_step>\d+)/(?P<phi_step>\d+)/$', get_plot_data),
    url(r'^ajax/mu/(?P<model_id>\d+)/(?P<time_step>\d+)/(?P<phi_step>\d+)/$', batch_mu_data),
    url(r'^ajax/time/(?P<model_id>\d+)/(?P<mu_step>\d+)/(?P<phi_step>\d+)/$', batch_time_data),
    url(r'^ajax/overplot/(?P<model_id>\d+)/$', ajax_overplot),
    # url(r'^ajax/plot/(?P<id>\d+)/(?P<frame>\d+)/$', get_all_data),
    # url(r'^plot_few/(\d+)/$', plot_few),
    # url(r'^text/$', text),
    url(r'^search/$', search_models),
    url(r'^about/$', about),
    url(r'^fitter/$', fitter),
    url(r'^fitter/results/$',fitter),
    url(r'^download/$',get_zip_file),
    # Examples:
    #url(r'^$', 'odetta.views.home', name='home'),
    #url(r'^odetta/', include('odetta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^browse/$', browse),
    url(r'^browse/models/(?P<pub_id>\d+)/$', browse),
)
