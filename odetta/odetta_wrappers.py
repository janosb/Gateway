import numpy as np


#the following is for overplotting
def oplot_process(file, model_id, redshift=1.0,filter=False, const=0):
    '''We need the scaling model_id in order to find the best scaling'''
    # For fake data:
    from odetta.models import Fluxvals, Spectra
    qset = Fluxvals.objects.filter(spec_id=Spectra.objects.filter(model_id=39)[0].spec_id).order_by("wavelength").values("wavelength", "luminosity")
    # For use later...
    # flux = [data['luminosity'] for data in qset]
    # wave = [data['wavelength'] for data in qset]

    # Test
    flux_data = []
    for rec in qset:
        flux_data.append({
            "x": rec['wavelength'],  # Graph's X-Axis
            "y": rec['luminosity'],  # Graph's Y-Axis
        })
    return flux_data
    # read the file into wave & flux values 
    #
    #

    #make sure everything is a numpy array
    spec_arr = np.array(flux)
    wave_arr = np.array(wave)

    #any filtering would go here
    #if filter:
    #    spec_arr = filterfunc(spec_arr,args)

    #scale spectrum to 100% of the maximum fluxval in the model spectra
    spec_out = flux*[max(model)/max(flux)]+const
    wave_out = wave_arr/(1+redshift)
    return wave_out, spec_out
 
def get_model_max(model_id):
    cur=db_connect();
    cur.execute("SELECT max(luminosity) FROM fluxvals WHERE model_id="+str(model_id)+";")
    maxval=(cur.fetchone())[0]
    return maxval

def db_connect():
    import psycopg2 as pg
    conn=pg.connect("odetta","scidb1.nersc.gov",5432,None,None,"odetta_user","password?")
    cur = conn.cursor()
    return cur
