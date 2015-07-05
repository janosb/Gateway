# encoding: utf-8
import itertools

kasen2009_publication = {
        "modeltype": "DD",
        "modeldim": 2,
        "date_entered": "2012-07-28",
        "citation": "Kasen,D.,Ropke,F.K., & Woosley, S.E. 2009, Nature, 460, 869",
        "type": "Ia",
        "fullname": "Delayed Detonation Type Ia (2D)",
        "shortname": "Kasen2009",
        "is_public": True,
        "summary": "Here we report multi-dimensional modelling of the explosion physics and radiative transfer, which reveals that the breaking of spherical symmetry is a critical factor in determining both the width-luminosity relation and the observed scatter about it.",
        "url": "http://adsabs.harvard.edu/abs/2009Natur.460..869K",
        "data_urls": ""
}

mu_list = [
    103.4935, 107.4577, 111.5103, 115.6794, 120.0001, 124.5182, 129.2966, 134.4271 ,14.8351, 140.0556,
    146.4428, 154.1582, 165.1650, 25.8420, 33.5573, 39.9445, 45.5730, 50.7036, 55.4819, 60.0001, 64.3208,
    68.4899, 72.5425, 76.5067, 80.4060, 84.2609, 88.0899, 91.9103, 95.7393, 99.5942]

kasen2009_models = [
    {
        "model_name": "DD2D_asym_01_dc2",  # perhaps extracted from the dir name
        "metadata": '{"ignition_points":20}',  # all of the other random information
        "file_columns": [0, 1, 4],  # which columns to read from the files
        "skip_header": 0,  # how many header lines to skip
        "spectra": [
            {"t_expl": t+.5,
             "mu": mu,
             "phi": 0.0,
             "specfile_rel_path": "dd2d_models/DD2D_asym_01_dc2/spectrum_t%02d_50/mu%.4f.mspec" % (t, mu)  # path is assumed to be relative to raw_data/
             } for t in range(2, 45)
        ]
    }
    for mu in mu_list]

kasen2011_publication = {
        "modeltype": "PI",
        "modeldim": 1,
        "date_entered": "2013-06-27",
        "citation": "Kasen, D., Woosley, S. & Heger, A., 2011, ApJ, 734.2, 102, pp. 13",
        "type": "Ia",
        "fullname": "Pair Instability SN (1D)",
        "shortname": "Kasen2011",
        "is_public": True,
        "summary": "Here we model the evolution, explosion, and observational signatures of representative pair instability supernovae (PI SNe) spanning a range of initial masses and envelope structures.",
        "url": "http://adsabs.harvard.edu/abs/2011ApJ...734..102K",
        "data_urls": "pair_he.tar.gz,pair_sne.tar.gz"
}


kasen2011_models = [
    {
        "model_name": "B200",  # perhaps extracted from the dir name
        "metadata": "",  # all of the other random information
        "file_columns": [0, 1, 4],  # which columns to read from the files
        "skip_header": 1,  # how many header lines to skip
        "spectra": [
            {"t_expl": t,
             "mu": 0.0,
             "phi": 0.0,
             "specfile_rel_path": "pair_sne/B200/optical_t%06.2f_I8.spec" % t  # path is assumed to be relative to raw_data/
             } for t in range(7, 803, 2)
        ]
    }
]


barnes2013_publication = {
        "modeltype": "NSM",
        "modeldim": 1,
        "date_entered": "2013-06-27",
        "citation": "Barnes, J. & Kasen, D., 2013, ApJ, 775, pp.18",
        "type": "NSM",
        "fullname": "Neutron Star Merger (1D)",
        "shortname": "Barnes2013",
        "is_public": True,
        "summary": "Here we consider the effect of heavier elements ... in time-dependent, multi-wavelength radiative transport calculations to predict the broadband light curves of one-dimensional models over a range of parameters (ejecta masses ~10^{-3}-10^{-1} M_sun and velocities ~0.1-0.3 c).",
        "url": "http://adsabs.harvard.edu/abs/2013arXiv1303.5787B",
        "data_urls": "ns_merger_spectra.tar.gz"
}

barnes2013_models = [
        {
        "model_name": "CaFN",  # perhaps extracted from the dir name
        "metadata": '{"velocity":"%s", "otherparam":"%s"}' % (x[0], x[1]),  # all of the other random information
        "file_columns": [0, 2, 3],  # which columns to read from the files
        "skip_header": 1,  # how many header lines to skip
        "spectra":[
            {"t_expl": 0.0,
             "mu": 0.0,
             "phi": 0.0,
             "specfile_rel_path": "ns_merger_spectra/bp_CaFN_%s_%s.spec" % (x[0], x[1])  # path is assumed to be relative to raw_data/
             }]
    } for x in list(itertools.product(["hv", "mv", "lv"],["h", "l", "m"]))]
