#Task 1

from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from astropy.convolution import Box2DKernel
import sep
import numpy as np

#importing data, reading in header information
large_image_data = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/large_mosaic.fits')
large_image_header = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/large_mosaic.fits')
#extracting WCS information from the header
large_image_WCS = WCS(large_image_header)

'''
Step 2 using configuration 2 I will run source extraction and create cutouts of 5 randomly selected objects in large_mosaic.fits
'''
#changing byte order
byte_swaped_data_large = large_image_data.byteswap().newbyteorder()

#above this range sources will be identified
back_size2 = 128
back_filter_size2 = 5
global_bkg2 = sep.Background(byte_swaped_data_large, bw=back_size2, bh=back_size2, 
                            fw=back_filter_size2, fh=back_filter_size2)
#background subtraction
bkg_subtracted2 = byte_swaped_data_large - global_bkg2

#convolution filter
filter_size = 5 #number of pixels
Bsource_kernel = Box2DKernel(filter_size)

#object catalog and segmentation map
min_area2 = 10
nsigma2 = 3
deb_n_thresh2 = 64
deb_count2 = 0.001
objects2, segmap2 = sep.extract(bkg_subtracted2, nsigma2, err=global_bkg2.globalrms,
                              minarea=min_area2, deblend_nthresh=deb_n_thresh2, 
                              deblend_cont=deb_count2, segmentation_map=True, 
                              filter_kernel = Bsource_kernel.array)

#Select 5 sources
random_sources = np.random.choice(objects2, 5)

##Create cutouts for each source
#the center for each random source
x_cen1 = random_sources[0]['x']
y_cen1 = random_sources[0]['y']

x_cen2 = random_sources[1]['x']
y_cen2 = random_sources[1]['y']

x_cen3 = random_sources[2]['x']
y_cen3 = random_sources[2]['y']

x_cen4 = random_sources[3]['x']
y_cen4 = random_sources[3]['y']

x_cen5 = random_sources[4]['x']
y_cen5 = random_sources[4]['y']

#size of each cutout
xsize = 100
ysize = 100

#creating the cutouts for each random source
cutout_image1 = Cutout2D(large_image_data, (x_cen1, y_cen1), (xsize, ysize), wcs = large_image_WCS)
cutout_image2 = Cutout2D(large_image_data, (x_cen2, y_cen2), (xsize, ysize), wcs = large_image_WCS)
cutout_image3 = Cutout2D(large_image_data, (x_cen3, y_cen3), (xsize, ysize), wcs = large_image_WCS)
cutout_image4 = Cutout2D(large_image_data, (x_cen4, y_cen4), (xsize, ysize), wcs = large_image_WCS)
cutout_image5 = Cutout2D(large_image_data, (x_cen5, y_cen5), (xsize, ysize), wcs = large_image_WCS)

#accessing the image data from the cutout
cutout_data1 = cutout_image1.data
cutout_WCS1 = cutout_image1.wcs

cutout_data2 = cutout_image2.data
cutout_WCS2 = cutout_image2.wcs

cutout_data3 = cutout_image3.data
cutout_WCS3 = cutout_image3.wcs

cutout_data4 = cutout_image4.data
cutout_WCS4 = cutout_image4.wcs

cutout_data5 = cutout_image5.data
cutout_WCS5 = cutout_image5.wcs

#create seperate fits files for each cutout
fits.writeto('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/cutout_1.fits', 
             cutout_data1, header=cutout_WCS1.to_header())

fits.writeto('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/cutout_2.fits', 
             cutout_data2, header=cutout_WCS2.to_header())

fits.writeto('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/cutout_3.fits', 
             cutout_data3, header=cutout_WCS3.to_header())

fits.writeto('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/cutout_4.fits', 
             cutout_data4, header=cutout_WCS4.to_header())

fits.writeto('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/cutout_5.fits', 
             cutout_data5, header=cutout_WCS5.to_header())