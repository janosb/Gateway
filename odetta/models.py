from __future__ import unicode_literals
from django.db import models
from django import forms


class Publications(models.Model):
    modeltype = models.CharField(max_length=40, blank=True, verbose_name='Model Type')
    modeldim = models.IntegerField(verbose_name='Model Dimension')
    date_entered = models.DateField(verbose_name='Date Entered')
    citation = models.CharField(max_length=200, blank=True, verbose_name='Citation')
    type = models.CharField(max_length=10, blank=True, verbose_name='Type')
    pub_id = models.IntegerField(primary_key=True, verbose_name='Publication ID')
    fullname = models.CharField(max_length=200, blank=True)
    shortname = models.CharField(max_length=200, blank=True)
    is_public = models.BooleanField()
    metatype = models.CharField(max_length=20, blank=True)
    summary = models.TextField()
    url = models.CharField(max_length=200, blank=True)
    data_urls = models.TextField(blank=True)

    class Meta:
        db_table = 'publications'


class Chi2Test(models.Model):
    fname = models.CharField(max_length=200, blank=True)
    chi2dof = models.FloatField(null=True, blank=True)
    chi2dof_bin = models.FloatField(null=True, blank=True)
    dof = models.IntegerField(null=True, blank=True)
    dofb = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'chi2test'


class Spectra(models.Model):
    model_id = models.IntegerField()
    spec_id = models.IntegerField(primary_key=True)
    t_expl= models.FloatField(null=True,blank=True)
    mu = models.FloatField(null=True,blank=True)
    phi = models.FloatField(null=True, blank=True)
    metatype = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'spectra'


class Fluxvals(models.Model):
    spec_id = models.IntegerField(primary_key=True)
    wavelength = models.FloatField()
    luminosity = models.FloatField(null=True, blank=True)
    photon_count = models.FloatField(null=True, blank=True)

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

    # @property
    # def date_entered(self):
    #     return Models.objects.values("date_entered").get(m_type_id=self.m_type_id)['date_entered']

    # @property
    # def sntype(self):
    #     return Models.objects.values("sntype").get(m_type_id=self.m_type_id)['sntype']

    # @property
    # def citation(self):
    #     return Models.objects.values("citation").get(m_type_id=self.m_type_id)['citation']

    def has_mu(self):
        return Spectra.objects.filter(model_id=self.model_id).distinct("mu").count() > 1

    def has_phi(self):
        return Spectra.objects.filter(model_id=self.model_id).distinct("phi").count() > 1


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
    return Spectra.objects.filter(model_id=model_id).values("t_expl").distinct("t_expl").order_by("t_expl").count() - 1


def get_mu_max(model_id):
    return Spectra.objects.filter(model_id=model_id).values("mu").distinct("mu").order_by("-mu").count() - 1


def get_phi_max(model_id):
    return Spectra.objects.filter(model_id=model_id).values("phi").distinct("phi").order_by("-phi").count() - 1


def get_time_val(model_id):
    times = []
    for time in Spectra.objects.filter(model_id = model_id).values("t_expl").distinct("t_expl").order_by("t_expl"):
        times.append(time["t_expl"]) 
    return times


def get_mu_val(model_id):
    mu_steps = []
    for mu in Spectra.objects.filter(model_id = model_id).values("mu").distinct("mu").order_by("mu"):
        mu_steps.append(mu["mu"]) 
    return mu_steps


class SearchForm(forms.Form):
    min_mass = forms.IntegerField(required=False, label='Minimum Mass')
    max_mass = forms.IntegerField(required=False, label="Maximum Mass")
    max_lum = forms.IntegerField(required=False, label="Peak Luminosity")
