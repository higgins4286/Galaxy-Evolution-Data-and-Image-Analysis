#Tutorial VII
from astropy.io import fits
import matplotlib.pyplot as plt
import sep
from astropy.convolution import Tophat2DKernel, Gaussian2DKernel, Box2DKernel
from astropy.visualization import (MinMaxInterval, PercentileInterval, ZScaleInterval, SqrtStretch, 
                                   AsinhStretch, LogStretch, ImageNormalize)

large_image = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VII_Source_Extraction_using_Python/data/large_mosaic.fits')
stamp_image = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VII_Source_Extraction_using_Python/data/postage_stamp.fits')

large_header = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VII_Source_Extraction_using_Python/data/large_mosaic.fits')
stamp_header = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VII_Source_Extraction_using_Python/data/postage_stamp.fits')

#Source extraction prep
#change "image_data" to the file name of the image
byte_swaped_data_large = large_image.byteswap().newbyteorder()
byte_swaped_data_stamp = stamp_image.byteswap().newbyteorder()

#Source Extraction steps

#above this range sources will be identified
back_size1 = 256
back_filter_size1 = 9
global_bkg1 = sep.Background(byte_swaped_data_stamp, bw=back_size1, bh=back_size1, 
                            fw=back_filter_size1, fh=back_filter_size1)

back_size2 = 128
back_filter_size2 = 5
global_bkg2 = sep.Background(byte_swaped_data_stamp, bw=back_size2, bh=back_size2, 
                            fw=back_filter_size2, fh=back_filter_size2)

#background subtracted data
bkg_subtracted1 = byte_swaped_data_stamp - global_bkg1

bkg_subtracted2 = byte_swaped_data_stamp - global_bkg2

#convolution filter
filter_size = 5 #number of pixels
Tsource_kernel = Tophat2DKernel(filter_size)
Gsource_kernel = Gaussian2DKernel(filter_size)
Bsource_kernel = Box2DKernel(filter_size)

#object catalog and segmentation map
min_area1 = 5
nsigma1 = 0.7
deb_n_thresh1 = 16
deb_count1 = 0.0001
objects1, segmap1 = sep.extract(bkg_subtracted1, nsigma1, err=global_bkg1.globalrms,
                              minarea=min_area1, deblend_nthresh=deb_n_thresh1, 
                              deblend_cont=deb_count1, segmentation_map=True, 
                              filter_kernel = Tsource_kernel.array)

min_area2 = 10
nsigma2 = 3
deb_n_thresh2 = 64
deb_count2 = 0.001
objects2, segmap2 = sep.extract(bkg_subtracted2, nsigma2, err=global_bkg2.globalrms,
                              minarea=min_area2, deblend_nthresh=deb_n_thresh2, 
                              deblend_cont=deb_count2, segmentation_map=True, 
                              filter_kernel = Tsource_kernel.array)

#Plotting image and segmap
normalization_large = ImageNormalize(large_image, interval=PercentileInterval(99.), stretch=AsinhStretch())
normalization_stamp = ImageNormalize(stamp_image, interval=PercentileInterval(99.), stretch=AsinhStretch())

fig, axs = plt.subplots(nrows=3, ncols=1, figsize=[8,10])
axs1, axs2, axs3 = axs

axs1.imshow(segmap1, origin='lower')
axs1.xaxis.set_visible(False)
axs1.yaxis.set_visible(False)
#axs1.text(400, 40, 'Config 1', color='white', fontsize=12) # 1000 x 1000, large
axs1.text(68, 10, 'Config 1', color='white', fontsize=12) # 108 x 201, stamp

axs2.imshow(stamp_image, origin='lower', cmap='Greys_r', norm=normalization_stamp)
axs2.xaxis.set_visible(False)
axs2.yaxis.set_visible(False)

axs3.imshow(segmap2, origin='lower')
axs3.xaxis.set_visible(False)
axs3.yaxis.set_visible(False)
#axs3.text(400, 40, 'Config 2', color='white', fontsize=12) # large image size 1000 x 1000
axs3.text(68, 10, 'Config 1', color='white', fontsize=12) # stamp image size 108 x 201

plt.tight_layout()
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VII_Source_Extraction_using_Python/plots/stamp_config.pdf', 
#             format='pdf', bbox_inches='tight')
plt.show()