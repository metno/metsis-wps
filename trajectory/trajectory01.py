"""
"""
import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import traceback
import netCDF4
#import cartopy.io.img_tiles as cimgt

def get_colors(inp, colormap, vmin=None, vmax=None):
    norm = plt.Normalize(vmin, vmax)
    return colormap(norm(inp))




url='http://thredds.nersc.no/thredds/dodsC/arcticData/framStrait/arctic_ocean_acidification_20160630-20160718.nc'

ds=netCDF4.Dataset(url)


sm = plt.cm.ScalarMappable(cmap='jet',norm=plt.Normalize(min(ds.variables['Temperature'][:]),max(ds.variables['Temperature'][:])))
sm._A = []


colors=get_colors(ds.variables['Temperature'][:],plt.cm.jet,vmin=min(ds.variables['Temperature'][:]),vmax=max(ds.variables['Temperature'][:]))

#request = cimgt.OSM()
#print("Plotting...")

#strengthNpArray = np.array(strength)                                                    # Used for scaling marker
#area = (strengthNpArray)/(strengthNpArray)                                              # All markers same size for easier viewing. 1 point radii
# area = np.pi * (strengthNpArray)**2                                                   # Use to scales marker relative to strength. 0 to 15 point radii
#ax = plt.axes(projection=ccrs.PlateCarree())
ax = plt.axes(projection=ccrs.NorthPolarStereo())

#ax.set_extent([1.850117, 8.418263, 77.90023, 78.14958])
ax.set_extent([-10.0, 40.0, 75.90023, 78.14958])

#ax.set_extent([-100, 100, -90, 90], crs=ccrs.NorthPolarStereo())
#ax.set_extent([0, 360, 50, 90], crs=ccrs.PlateCarree())
#ax.plot(x,y,transform=ccrs.PlateCarree())
#ax = plt.axes(projection=ccrs.Mercator())
ax.stock_img()
ax.gridlines()
                                               # Map projection
ax.coastlines(resolution='10m')                                                         # Adds coastline to map at highest resolution
#ax.add_image(request, 8)
#plt.scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], s=5, marker='o', alpha=0.5, transform=ccrs.PlateCarree())  # Plot
#plt.scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], s=5, marker='o', alpha=0.5, transform=ccrs.Geodetic())  # Plot
plt.scatter(ds.variables['longitude'][:], ds.variables['latitude'][:], c=colors,s=5, marker='o', alpha=0.5, transform=ccrs.Geodetic())  # Plot
plt.colorbar(sm,ax=ax)
#plt.colorbar(colors)
plt.show()
