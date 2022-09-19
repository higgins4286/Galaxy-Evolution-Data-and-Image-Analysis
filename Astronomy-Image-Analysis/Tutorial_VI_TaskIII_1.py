#Task III, 1

#Importing modules
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import (MinMaxInterval, PercentileInterval, ZScaleInterval, SqrtStretch, 
                                   AsinhStretch, LogStretch, ImageNormalize)

##Retreiving info w/o opening file
mosaic_data = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/large_mosaic.fits')

stamp_data = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/postage_stamp.fits')

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=[18,8])
axs1, axs2, axs3 = axs

#ax1
normalization = ImageNormalize(image_data, interval=MinMaxInterval(), stretch=LogStretch())
axs1.imshow(stamp_data, origin='lower', cmap='gray_r', norm=normalization)
axs1.xaxis.set_visible(False)
axs1.yaxis.set_visible(False)
axs1.text(120, 50, 'MinMaxInterval \n LogStretch', color='white', fontsize=12, 
          bbox=dict(facecolor='grey', edgecolor='grey'))

#ax2
normalization = ImageNormalize(image_data, interval=PercentileInterval(99.), stretch=SqrtStretch())
axs2.imshow(stamp_data, origin='lower', cmap='gray_r', norm=normalization)
axs2.xaxis.set_visible(False)
axs2.yaxis.set_visible(False)
axs2.text(120, 50, 'PercentileInterval \n SqrtStretch', color='white', fontsize=12, 
          bbox=dict(facecolor='grey', edgecolor='grey'))

#ax3
normalization = ImageNormalize(image_data, interval=ZScaleInterval(), stretch=AsinhStretch())
axs3.imshow(stamp_data, origin='lower', cmap='gray_r', norm=normalization)
axs3.xaxis.set_visible(False)
axs3.yaxis.set_visible(False)
axs3.text(120, 50, 'ZScaleInterval \n AsinhStretch', color='white', fontsize=12,
          bbox=dict(facecolor='grey', edgecolor='grey'))

plt.tight_layout()
plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/plots/TaskIII_step1b.pdf', 
             format='pdf', bbox_inches='tight')
plt.show()