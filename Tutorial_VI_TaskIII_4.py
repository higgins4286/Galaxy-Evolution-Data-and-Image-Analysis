#Importing modules
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import (MinMaxInterval, PercentileInterval, ZScaleInterval, SqrtStretch, 
                                   AsinhStretch, LogStretch, ImageNormalize)
from astropy.convolution import Box2DKernel, convolve, Gaussian2DKernel, Tophat2DKernel

#opening file
data160 = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f160w.fits')
header160 = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/for_RGB/gds_4608_f160w.fits')

box_sizeB = 3
box = Box2DKernel(box_sizeB)
convolved_box = convolve(data160, box)

box_sizeG = 5
gauss = Gaussian2DKernel(box_sizeG)
convolved_gauss = convolve(data160, gauss)

box_sizeT = 5
top = Tophat2DKernel(box_sizeT)
convolved_top = convolve(data160, top)

fig, axs = plt.subplots(2, 2, figsize=[8,8])
#ax1
normalization = ImageNormalize(data160, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs[0, 0].imshow(data160, origin='lower', cmap='Reds_r', norm=normalization)
axs[0, 0].xaxis.set_visible(False)
axs[0, 0].yaxis.set_visible(False)
axs[0, 0].set_title('Normal', fontsize=18)

#ax2
normalization = ImageNormalize(convolved_box, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs[0, 1].imshow(convolved_box, origin='lower', cmap='Reds_r', norm=normalization)
axs[0, 1].xaxis.set_visible(False)
axs[0, 1].yaxis.set_visible(False)
axs[0, 1].set_title('Box', fontsize=18)

#ax3
normalization = ImageNormalize(convolved_gauss, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs[1, 0].imshow(convolved_gauss, origin='lower', cmap='Reds_r', norm=normalization)
axs[1, 0].xaxis.set_visible(False)
axs[1, 0].yaxis.set_visible(False)
axs[1, 0].set_title('Gaussian', fontsize=18)

#ax4
normalization = ImageNormalize(convolved_top, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs[1, 1].imshow(convolved_top, origin='lower', cmap='Reds_r', norm=normalization)
axs[1, 1].xaxis.set_visible(False)
axs[1, 1].yaxis.set_visible(False)
axs[1, 1].set_title('Tophat', fontsize=18)

plt.tight_layout()
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/plots/TaskIII_step4.pdf', 
#             format='pdf', bbox_inches='tight')
plt.show()