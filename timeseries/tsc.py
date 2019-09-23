# _*_ coding: utf-8 _*_
import sys
from collections import defaultdict
import numpy as np
import netCDF4
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

import adcUtils as adcu

def getDataset(opendapURL):
    return netCDF4.Dataset(opendapURL)

def getVarBySN(dataset,standard_name):
    for k in dataset.variables.keys():
        try:
            if dataset.variables[k].standard_name == standard_name:
                return dataset.variables[k]
        except:
            pass
    return

def getPlotData(url,xvarSN,yvarSN):
    ds  = getDataset(url)
    X   = getVarBySN(ds,xvarSN)
    Y   = getVarBySN(ds,yvarSN)
    x,y = X[:],Y[:]
    x = adcu.mask_v(x)
    y = adcu.mask_v(y)
    return X, Y, ds.title, x, y

def plot(X,Y,
         title,
         x,y,everyNth,
         fileName,fileFormat,
         figWidth=8.4,figHeight=5.6,
         linewidth=0.1):
    fig, ax = plt.subplots()
    MAX_DATA_POINTS = 200
    number_of_xticks = 15
    xtick_spacing = (x.max()-x.min())/number_of_xticks
    xticksp = np.arange(x.min(),x.max(),xtick_spacing)
    xtickss = [adcu.getSISO(dd,X.units) for dd in xticksp]
    if ((x.size / everyNth) <= MAX_DATA_POINTS):
        everyNth = int(x.size/MAX_DATA_POINTS)

    plt.figure(figsize=(figWidth,figHeight))
    plt.title('%s' % (title))
    plt.xlabel('%s' % (X.standard_name))
    plt.xticks(xticksp,xtickss,rotation=30)
    plt.ylabel('%s [%s]' % (Y.standard_name,Y.units))
    plt.xlim(x.min(),x.max())
    plt.scatter(x[0:-1:everyNth],y[0:-1:everyNth],s=3,
                facecolors='none', edgecolors='r', label='data')
    plt.plot(x[0:-1:everyNth],y[0:-1:everyNth],
             'b',linewidth=linewidth)
    plt.legend(loc=0)
    plt.autoscale(tight=True)
    #Supported formats (will need more libraries for some):
    #eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
    plt.savefig('%s.%s' %(fileName,fileFormat))
    plt.clf()




if __name__ == "__main__":
    d=defaultdict(list)
    for k, v in ((k.lstrip('-'), v) for k,v in (a.split('=') for a in sys.argv[1:])):
        d[k].append(v)
    X,Y,title,x,y = getPlotData(d['url'][0],d['xvar'][0],d['yvar'][0])
    plot(X,Y,title,x,y,int(d['everyNth'][0]),d['fileName'][0],d['fileFormat'][0])
