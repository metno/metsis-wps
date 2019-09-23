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
#import cartopy.io.img_tiles as cimgt
#from mpl_toolkits.axes_grid1 import make_axes_locatable

def get_colors(inp, colormap, vmin=None, vmax=None):
    norm = plt.Normalize(vmin, vmax)
    return colormap(norm(inp))

#dsvar='Temperature'
#dsvar='Soundspeed'
#dsvar='pH'
dsvar='CO2'

url='http://thredds.nersc.no/thredds/dodsC/arcticData/framStrait/arctic_ocean_acidification_20160630-20160718.nc'
ds=netCDF4.Dataset(url)

sm = plt.cm.ScalarMappable(cmap='jet',norm=plt.Normalize(min(ds.variables[dsvar][:]),max(ds.variables[dsvar][:])))
sm._A = []
colors=get_colors(ds.variables[dsvar][:],plt.cm.jet,vmin=min(ds.variables[dsvar][:]),vmax=max(ds.variables[dsvar][:]))


fig, axs = plt.subplots(2, 1)
axs[0] = plt.axes(projection=ccrs.NorthPolarStereo())
#axs[0] = plt.axes(projection=ccrs.Mercator())
axs[0].coastlines(resolution='10m')

axs[0].set_extent([-10.0, 40.0, 75.90023, 78.14958])

axs[0].stock_img()
#axs[0].gridlines()

axs[0].gridlines(linewidth=1, color='gray', alpha=0.5, linestyle='--')

#axs[0].gridlines(draw_labels=True,linewidth=1, color='gray', alpha=0.5, linestyle='--')
# axs[0].xlabels_top = False
# axs[0].ylabels_left = False
# axs[0].xlines = False
# axs[0].xlocator = mticker.FixedLocator([-180, -45, 0, 45, 180])
# axs[0].xformatter = LONGITUDE_FORMATTER
# axs[0].yformatter = LATITUDE_FORMATTER
# axs[0].xlabel_style = {'size': 15, 'color': 'gray'}
# axs[0].xlabel_style = {'color': 'red', 'weight': 'bold'}
#

axs[0].scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], c=colors,s=1, marker='.', alpha=0.5, transform=ccrs.Geodetic())
plt.title('%s' %(ds.title))

# axs[1] = plt.axes(projection=ccrs.NorthPolarStereo())
# axs[1].set_extent([1.850117, 8.418263, 77.90023, 78.14958])
# axs[1].scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], c=colors,s=1, marker='o', alpha=0.5, transform=ccrs.Geodetic())

plt.colorbar(sm,ax=axs[0],orientation='horizontal',label='%s [%s]' %(ds.variables[dsvar].long_name,ds.variables[dsvar].units))





fig.tight_layout()
plt.savefig('trajectory.pdf')
plt.show()









#request = cimgt.OSM()
#print("Plotting...")

#strengthNpArray = np.array(strength)                                                    # Used for scaling marker
#area = (strengthNpArray)/(strengthNpArray)                                              # All markers same size for easier viewing. 1 point radii
# area = np.pi * (strengthNpArray)**2                                                   # Use to scales marker relative to strength. 0 to 15 point radii
#ax = plt.axes(projection=ccrs.PlateCarree())

#axs[1] = plt.axes(projection=ccrs.NorthPolarStereo())



#axs[1].set_extent([-10.0, 40.0, 75.90023, 78.14958])

#ax.set_extent([-100, 100, -90, 90], crs=ccrs.NorthPolarStereo())
#ax.set_extent([0, 360, 50, 90], crs=ccrs.PlateCarree())
#ax.plot(x,y,transform=ccrs.PlateCarree())
#ax = plt.axes(projection=ccrs.Mercator())

                                               # Map projection
                                                   # Adds coastline to map at highest resolution
#ax.add_image(request, 8)
#plt.scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], s=5, marker='o', alpha=0.5, transform=ccrs.PlateCarree())  # Plot
#plt.scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], s=5, marker='o', alpha=0.5, transform=ccrs.Geodetic())  # Plot
  # Plot
#axs[1].scatter([1,2,3,4,5,6],[6,7,6,5,4,4])  # Plot

# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.05)
#
# plt.colorbar(sm,cax=cax)
#    ds.variables[dsvar].standard_name+''ds.variables[dsvar].units
#plt.colorbar(colors)
#plt.show()
