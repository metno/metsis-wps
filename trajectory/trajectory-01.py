"""
Cartopy fails to plot multiple images on one axis in PDF.
"""
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

# prepare sample image
x = np.linspace(-1, 1, 101)
y = np.linspace(-1, 1, 101)
z = np.exp(x**2 + y[:, None]**2)

# plot with and without cartopy CRS
proj = ccrs.PlateCarree()
for row in range(2):
    for col in range(2):

        # on the left column, add normal Matplotlib axes
        if col == 0:
            plt.subplot(2, 2, 1+2*row+col)
            plt.title('Matplotlib')

        # on the right column, add Cartopy axes
        else:
            plt.subplot(2, 2, 1+2*row+col, projection=proj)
            plt.title('Cartopy')

        # on the top row, plot one image
        if row == 0:
            plt.imshow(z, extent=[1, 2, 1, 2])

        # on the bottom row, plot three images
        if row == 1:
            plt.imshow(z, extent=[0, 1, 0, 1])
            plt.imshow(z, extent=[1, 2, 1, 2])
            plt.imshow(z, extent=[2, 3, 2, 3])

        # set axes limits
        plt.xlim(0, 3)
        plt.ylim(0, 3)

# save as png and pdf
plt.savefig('bug.png')
plt.savefig('bug.pdf')
