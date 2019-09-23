import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import netCDF4

url='http://thredds.nersc.no/thredds/dodsC/arcticData/framStrait/arctic_ocean_acidification_20160630-20160718.nc'

ds=netCDF4.Dataset(url)
print(ds.variables['latitude'][:])

airports = np.genfromtxt("gadb_declatlon.csv",
                     delimiter=',',
                     dtype=[('lat', np.float32), ('lon', np.float32)],
                     usecols=(0, 1))
print(airports['lat'])

fig = plt.figure()
#
# themap = Basemap(projection='gall',
#               llcrnrlon = -15,
#               llcrnrlat = 28,
#               urcrnrlon = 45,
#               urcrnrlat = 73,
#               resolution = 'l',
#               area_thresh = 100000.0,
#               )


# themap = Basemap(projection='gall',
#               llcrnrlon = 3.181263,
#               llcrnrlat = 77.99095,
#               urcrnrlon = 8.084082,
#               urcrnrlat = 78.14951,
#               resolution = 'l',
#               area_thresh = 100000.0,
#               )

themap = Basemap(projection='npaeqd',boundinglat=10,lon_0=20,resolution='l')
themap.drawparallels(np.arange(-80.,81.,5.))
themap.drawmeridians(np.arange(-180.,181.,5.))
themap.drawcoastlines()
themap.drawcountries()
themap.fillcontinents(color = 'gainsboro')
themap.drawmapboundary(fill_color='steelblue')

#x, y = themap(airports['lon'], airports['lat'])
x, y = themap(ds.variables['longitude'][:], ds.variables['latitude'][:])
themap.plot(x, y,
            'o',
            color='red',
            markersize=2
            )

plt.show()
