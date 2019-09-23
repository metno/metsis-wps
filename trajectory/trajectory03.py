"""
"""
import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import traceback
import netCDF4
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from matplotlib import gridspec
#import cartopy.io.img_tiles as cimgt
#from mpl_toolkits.axes_grid1 import make_axes_locatable

def get_colors(inp, colormap, vmin=None, vmax=None):
    norm = plt.Normalize(vmin, vmax)
    return colormap(norm(inp))



#dsvar='AirSaturation'
#dsvar='mole_concentration_of_dissolved_molecular_oxygen_in_sea_water'
#dsvar='Soundspeed'
#dsvar='sea_surface_density'
#dsvar='sea_water_practical_salinity'
#dsvar='Temperature'
#dsvar='sea_water_electrical_conductivity'
#dsvar='AirSaturation_2'
#dsvar='O2Concentration'
#dsvar='temperature_of_sensor_for_oxygen_in_sea_water'
#dsvar='surface_partial_pressure_of_carbon_dioxide_in_sea_water'
#dsvar='Temperature_2'
#dsvar='CO2'
#dsvar='pH'
#dsvar='Temperature_3'
dsvar='Temperature_4'



proj='ccrs.NorthPolarStereo()'

url='http://thredds.nersc.no/thredds/dodsC/arcticData/framStrait/arctic_ocean_acidification_20160630-20160718.nc'
ds=netCDF4.Dataset(url)

sm = plt.cm.ScalarMappable(cmap='jet',norm=plt.Normalize(min(ds.variables[dsvar][:]),max(ds.variables[dsvar][:])))
sm._A = []
colors=get_colors(ds.variables[dsvar][:],plt.cm.jet,vmin=min(ds.variables[dsvar][:]),vmax=max(ds.variables[dsvar][:]))


plt.figure(figsize=(11,7))

ax1=plt.subplot(2,1,1,projection=ccrs.NorthPolarStereo())
ax1.coastlines(resolution='10m')
ax1.set_extent([-10.0, 40.0, 75.90023, 78.14958])
ax1.stock_img()
ax1.gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--')
ax1.scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], c=colors,s=1, marker='.', alpha=0.5, transform=ccrs.Geodetic())
ax1.set_title('%s' %(ds.getncattr('title')))

ax2=plt.subplot(2,1,2,projection=ccrs.NorthPolarStereo())
ax2.coastlines(resolution='10m')
ax2.set_extent([1.850117, 8.418263, 77.90023, 78.14958])
ax2.stock_img()
#ax2.gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--')
ax2.scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], c=colors,s=1, marker='.', alpha=0.5, transform=ccrs.Geodetic())





plt.colorbar(sm,ax=ax2,orientation='horizontal',label='%s [%s]' %(ds.variables[dsvar].long_name,ds.variables[dsvar].units))
plt.tight_layout()
fileName=dsvar.replace(" ","_")
plt.savefig('%s.pdf' %(fileName))
