from odetta.settings import RAW_DATA_ROOT, RAW_DATA_DIR


def get_lightcurve(wave, fluxes, times, filter_name, plot=False):
    filtx, filty = get_filter(filter_name)
    filter_interp = interpol_lin(filtx, filty, wave)
    lc = []
    for flux in fluxes:
        lc.append(lc_point(wave, flux, wave, filter_interp))
    if plot:
        from pylab import plot, clf, show, legend
        clf()
        plot(times, lc)
        show()


def lc_point(wave, flux, filter_wave, filter_flux, needs_interpol=True):
    from numpy import trapz, log10
    if needs_interpol:
        # interpolate filter onto model/data grid
        filter_interp = interpol_lin(filter_wave, filter_flux, wave, plot=False)
    else:
        filter_interp = filter_flux
    y1 = []
    y2 = []
    for i in range(len(wave)):
        y_top = wave[i]*filter_interp[i]*flux[i]
        y_bot = filter_interp[i]/wave[i]
        y1.append(y_top)
        y2.append(y_bot)
    int1 = trapz(y1, x=wave)
    int2 = trapz(y2, x=wave)
    ABMAG = -2.5*log10(int1/int2) - 2.407948

    # from notes: ABMAG = -2.5log[int(lam * R_b-band * f)dlam/int(R/lam)dlam] - 2.407948
    return ABMAG


def interpol_lin(xin, yin, xout, plot=False):
    from scipy.interpolate import interp1d
    f = interp1d(xin, yin, bounds_error=False, fill_value=0)
    yout = f(xout)
    if plot:
        import pylab as pl
        pl.plot(xout, yout, xin, yin, '.')
    return yout


def check_binning(wave):
    if (wave[1]-wave[0]) == (wave[-1]-wave[-2]):
        print "found linear binning"
    elif (wave[1]/wave[0]) == (wave[-1]/wave[-2]):
        print "found logarithmic binning"
    else:
        print "could not identify binning"


def get_filter(filter_name):
    import numpy as np
    dir = RAW_DATA_ROOT+RAW_DATA_DIR+'/filters/'
    if filter_name.lower() in ['ux', 'b', 'v', 'r', 'i']:
        fname = dir+'s'+filter_name.lower()+'.dat'
        wave, T = np.genfromtxt(fname, unpack=True)
        return wave, T
    else:
        'filter does not exist. choose from ux, b, v, r, i'
        return -1, -1

def get_filters():
    import numpy as np
    dir = RAW_DATA_ROOT+RAW_DATA_DIR+'/filters/'
    filters = {}
    for filter_name in ['ux', 'b', 'v', 'r', 'i']:
        wave_name = filter_name+"_wave"
        flux_name = filter_name+"_trans"
        fname = dir+'s'+filter_name.lower()+'.dat'
        wave, T = np.genfromtxt(fname, unpack=True)
        filters[wave_name] = wave
        filters[flux_name] = T
    return filters






#extras 
def plot_filter(filter):
    from pylab import clf, plot, legend, show
    import numpy as np
    dir = RAW_DATA_ROOT+RAW_DATA_DIR+'/filters/'
    
    if filter in ['UX', 'B', 'V', 'R', 'I']:
        from glob import glob
        fsearch = 's'+filter.lower()+'*.dat'
        fnames = glob(dir+fsearch)
        clf()
        titles = []
        for f in fnames:
            wave, T = np.genfromtxt(f, unpack=True)
            plot(wave, T)
            titles.append((f.split('/'))[-1])
        legend(titles)
        show()


