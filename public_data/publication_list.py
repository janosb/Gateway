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
        "summary": "Type Ia supernovae result when carbon-oxygen white dwarfs in binary systems accrete mass from companion stars, reach a critical mass and explode. The near uniformity of their light curves makes these supernovae good 'standard candles' for measuring cosmic expansion, but a correction must be applied to account for the fact that the brighter ones have broader light curves. One-dimensional modelling, with a certain choice of parameters, can reproduce this general trend in the width-luminosity relation; but the processes of ignition and detonation have recently been shown to be intrinsically asymmetric, so parameterization must have its limits. Here we report multi-dimensional modelling of the explosion physics and radiative transfer, which reveals that the breaking of spherical symmetry is a critical factor in determining both the width-luminosity relation and the observed scatter about it. The deviation from spherical symmetry can also explain the finite polarization detected in the light from some supernovae. The slope and normalization of the width-luminosity relation has a weak dependence on certain properties of the white dwarf progenitor, in particular the trace abundances of elements other than carbon and oxygen. Failing to correct for this effect could lead to systematic overestimates of up to 2 per cent in the distance to remote supernovae.",
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
        "summary": "For the initial mass range (140 M_sun < M < 260_M sun) stars die in a thermonuclear runaway triggered by the pair-production instability. The supernovae they make can be remarkably energetic (up to ~10^53 erg) and synthesize considerable amounts of radioactive isotopes. Here we model the evolution, explosion, and observational signatures of representative pair instability supernovae (PI SNe) spanning a range of initial masses and envelope structures. The predicted light curves last for hundreds of days and range in luminosity from very dim to extremely bright (L ~ 10^44 erg s^-1). The most massive events are bright enough to be seen at high redshift, but the extended light curve duration (~1 yr)-prolonged by cosmological time-dilation—may make it difficult to detect them as transients. A more promising approach may be to search for the brief and luminous outbreak occurring when the explosion shock wave first reaches the stellar surface. Using a multi-wavelength radiation-hydrodynamics code we calculate that, in the rest frame, the shock breakout transients of PI SNe reach luminosities of 10^45-10^46 erg s^-1, peak at wavelengths ~30-170 Ang, and last for several hours. We discuss how observations of the light curves, spectra, and breakout emission can be used to constrain the mass, radius, and metallicity of the progenitor.",
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
        "summary": "The coalescence of compact objects is a promising astrophysical source of detectable gravitational wave signals. The ejection of r-process material from such mergers may lead to a radioactively powered electromagnetic counterpart signal which, if discovered, would enhance the science returns. As very little is known about the optical properties of heavy r-process elements, previous light-curve models have adopted opacities similar to those of iron group elements. Here we consider the effect of heavier elements, particularly the lanthanides, which increase the ejecta opacity by several orders of magnitude. We include these higher opacities in time-dependent, multi-wavelength radiative transport calculations to predict the broadband light curves of one-dimensional models over a range of parameters (ejecta masses ~10^{-3}-10^{-1} M_sun and velocities ~0.1-0.3 c). We find that the higher opacities lead to much longer duration light curves which can last a week or more. The emission is shifted toward the infrared bands due to strong optical line blanketing, and the colors at later times are representative of a blackbody near the recombination temperature of the lanthanides (T ~ 2500 K). We further consider the case in which a second mass outflow, composed of 56Ni, is ejected from a disk wind, and show that the net result is a distinctive two component spectral energy distribution, with a bright optical peak due to 56Ni and an infrared peak due to r-process ejecta. We briefly consider the prospects for detection and identification of these transients.",
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
