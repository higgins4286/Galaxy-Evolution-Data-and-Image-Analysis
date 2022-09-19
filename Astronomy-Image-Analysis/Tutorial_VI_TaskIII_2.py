#Importing modules
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import (MinMaxInterval, PercentileInterval, ZScaleInterval, SqrtStretch, 
                                   AsinhStretch, LogStretch, ImageNormalize)

#opening file
cube = fits.open('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/image_cube.fits', 
                      memmap=True)
image_data_1 = cube[1].data
image_data_2 = cube[2].data
image_data_3 = cube[3].data

image_header_1 = cube[1].header
image_header_2 = cube[2].header
image_header_3 = cube[3].header

cube.close()

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=[18,8])
axs1, axs2, axs3 = axs

#ax1
normalization = ImageNormalize(image_data_1, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs1.imshow(image_data_1, origin='lower', cmap='gray_r', norm=normalization)
axs1.xaxis.set_visible(False)
axs1.yaxis.set_visible(False)

#ax2
normalization = ImageNormalize(image_data_2, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs2.imshow(image_data_2, origin='lower', cmap='gray_r', norm=normalization)
axs2.xaxis.set_visible(False)
axs2.yaxis.set_visible(False)

#ax3
normalization = ImageNormalize(image_data_3, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs3.imshow(image_data_3, origin='lower', cmap='gray_r', norm=normalization)
axs3.xaxis.set_visible(False)
axs3.yaxis.set_visible(False)

plt.tight_layout()
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/plots/TaskIII_step2.pdf', 
#             format='pdf', bbox_inches='tight')
plt.show()