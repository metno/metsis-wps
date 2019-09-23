import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import netCDF4

url='http://thredds.nersc.no/thredds/dodsC/arcticData/framStrait/arctic_ocean_acidification_20160630-20160718.nc'

ds=netCDF4.Dataset(url)

#ax = plt.axes(projection=ccrs.PlateCarree())
# ax.stock_img()

#ax.set_extent([-150, -20, -90, 90], crs=ccrs.PlateCarree())
ax = plt.axes(projection=ccrs.NorthPolarStereo())

ax.coastlines(resolution='10m')
ax.stock_img()
ax.gridlines()

ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='blue', linewidth=2, marker='o',
         transform=ccrs.Geodetic(),
         )

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--',
         transform=ccrs.PlateCarree(),
         )

plt.text(ny_lon - 3, ny_lat - 12, 'New York',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
         horizontalalignment='left',
         transform=ccrs.Geodetic())

plt.plot(ds.variables['longitude'][:], ds.variables['latitude'][:])


plt.show()
