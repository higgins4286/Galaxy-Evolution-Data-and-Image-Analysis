#Importing modules
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import (MinMaxInterval, PercentileInterval, ZScaleInterval, SqrtStretch, 
                                   AsinhStretch, LogStretch, ImageNormalize)

#opening file
data160 = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f160w.fits')
header160 = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f160w.fits')

data606 = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f606w.fits')
header606 = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f606w.fits')

data814 = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f814w.fits')
header814 = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f814w.fits')

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=[18,8])
axs1, axs2, axs3 = axs

#ax1
normalization = ImageNormalize(data160, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs1.imshow(data160, origin='lower', cmap='Reds_r', norm=normalization)
axs1.xaxis.set_visible(False)
axs1.yaxis.set_visible(False)

#ax2
normalization = ImageNormalize(data814, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs2.imshow(data814, origin='lower', cmap='Greens_r', norm=normalization)
axs2.xaxis.set_visible(False)
axs2.yaxis.set_visible(False)

#ax3
normalization = ImageNormalize(data606, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs3.imshow(data606, origin='lower', cmap='Blues_r', norm=normalization)
axs3.xaxis.set_visible(False)
axs3.yaxis.set_visible(False)

plt.tight_layout()
plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/plots/TaskIII_step3.pdf', 
             format='pdf', bbox_inches='tight')
plt.show()