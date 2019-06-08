import os
import urllib
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

import sys
#sys.path.append('/Users/patapisp/Documents/PhD/Referenceless_PCA/PynPoint/')
#sys.path.append('/Users/patapisp/Documents/PhD/Referenceless_PCA/IPCA/')

#from ipca import IPCA

from pynpoint import Pypeline, Hdf5ReadingModule, FitsReadingModule,\
                     PSFpreparationModule, ParangReadingModule,\
                     PcaPsfSubtractionModule,\
                     FalsePositiveModule, CropImagesModule, AperturePhotometryModule,\
                     FakePlanetModule

from pynpoint.processing.iterativepsfsubtraction import IterativePcaPsfSubtractionModule

working_place = "/home/Dropbox/Dropbox/1_Philipp/1_UZH/8_FS19/BachelorProject/PynPoint"
input_place = "/home/philipp/Documents/BA_In_out/raw/hd101412"
output_place = "output/"


'''initial and ending ranks'''
pca_numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
ipca_numbers_init = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
#
### Python 3
###urllib.request.urlretrieve("https://people.phys.ethz.ch/~stolkert/pynpoint/betapic_naco_mp.hdf5",
###                           os.path.join(input_place, "betapic_naco_mp.hdf5"))
##
pipeline = Pypeline(working_place_in=working_place,
                    input_place_in=input_place,
                    output_place_in=output_place)
               
#
#module = FitsReadingModule(name_in="read",
#                           input_dir=input_place,
#                           image_tag="science")
#
#pipeline.add_module(module)
#
#
#
#
#module = CropImagesModule(2,
#                 center=None,
#                 name_in="crop_image",
#                 image_in_tag="science",
#                 image_out_tag="science_cropped")
#                 
#pipeline.add_module(module)
#
#
#module = ParangReadingModule(file_name="parang.dat",
#                             name_in="parang",
#                             input_dir=input_place,
#                             data_tag="science_cropped")
#
#pipeline.add_module(module)
#
#module = AperturePhotometryModule(radius=0.0083,
#                 position=(39, 39),
#                 name_in="aperture_photometry_star",
#                 image_in_tag="science_cropped",
#                 phot_out_tag="photometry_star")
#                 
#pipeline.add_module(module)
#
##
###module = PSFpreparationModule(name_in="prep",
###                              image_in_tag="science",
###                              image_out_tag="prep",
###                              mask_out_tag=None,
###                              norm=False,
###                              resize=None,
###                              cent_size=None,
###                              edge_size=1.1)
###
###pipeline.add_module(module)
#
#
#module = PcaPsfSubtractionModule(pca_numbers=pca_numbers,
#                                 name_in="pca",
#                                 images_in_tag="science_cropped",
#                                 reference_in_tag="science_cropped",
#                                 res_mean_tag="residuals_pca")
#
#
#pipeline.add_module(module)
#
#module = AperturePhotometryModule(radius=0.0083,
#                 position=(49, 52),
#                 name_in="aperture_photometry_pca",
#                 image_in_tag="residuals_pca",
#                 phot_out_tag="photometry_pca")
#                 
#pipeline.add_module(module)
#
#
#
#for ipca_number_init in ipca_numbers_init:
#    module = IterativePcaPsfSubtractionModule(pca_numbers=pca_numbers,
#                                     pca_number_init = ipca_number_init,
#                                     name_in="ipca_" + str(ipca_number_init),
#                                     images_in_tag="science_cropped",
#                                     reference_in_tag="science_cropped",
#                                     res_mean_tag= "residuals_ipca_" + str(ipca_number_init),
#                                     subtract_mean = False)
#    
#    pipeline.add_module(module)
#        
#        
#    module = AperturePhotometryModule(radius=0.0083,
#                 position=(49, 52),
#                 name_in="aperture_photometry_ipca_" + str(ipca_number_init),
#                 image_in_tag="residuals_ipca_" + str(ipca_number_init),
#                 phot_out_tag="photometry_ipca_" + str(ipca_number_init))
#                 
#    pipeline.add_module(module)
#
#
#pipeline.run()
##residuals = pipeline.get_data("residuals_pca")
#
##create list of pca photometry values
#photometry_pca = pipeline.get_data("photometry_pca").tolist()
#photometry_star = np.mean(pipeline.get_data("photometry_star"))
#
#for counter in range(len(photometry_pca)):
#    photometry_pca[counter] = photometry_pca[counter][0]/photometry_star
#
##create dictionairy of lists with ipca photometry values
#photometry_ipca = {}
#for ipca_number_init in ipca_numbers_init:
#    #add list for each pca_number_init to dictionairy
#    photometry_ipca[ipca_number_init] = pipeline.get_data("photometry_ipca_" + str(ipca_number_init)).tolist()
#    for counter in range(len(photometry_ipca[ipca_number_init])):
#        photometry_ipca[ipca_number_init][counter] = photometry_ipca[ipca_number_init][counter][0]/photometry_star            
#    if len(photometry_ipca[ipca_number_init]) != len(pca_numbers):
#        photometry_ipca[ipca_number_init] = [None]*(len(pca_numbers) - len(photometry_ipca[ipca_number_init])) + photometry_ipca[ipca_number_init]
#
##create matrix_ipca
#matrix_ipca = np.zeros((len(ipca_numbers_init), len(pca_numbers)))
#
#for counter_i, i in enumerate(ipca_numbers_init):
#    for counter_j, j in enumerate(pca_numbers):
#        matrix_ipca[counter_i][counter_j] = photometry_ipca[i][counter_j]
#        
##create matrix_ratio
#matrix_ratio = np.zeros((len(ipca_numbers_init), len(pca_numbers)))
#
#for counter_i, i in enumerate(ipca_numbers_init):
#    for counter_j, j in enumerate(pca_numbers):
#        try:
#            matrix_ratio[counter_i][counter_j] = photometry_ipca[i][counter_j]/photometry_pca[counter_j]
#        except TypeError:
#            matrix_ratio[counter_i][counter_j] = None
#
##create matrix_all
#matrix_all = np.zeros((len(ipca_numbers_init)+1, len(pca_numbers)))
#
#for i in range(len(ipca_numbers_init)+1):
#    for j in range(len(pca_numbers)):
#        if i == 0:
#            matrix_all[i][j] = photometry_pca[j]
#        else:
#            matrix_all[i][j] = matrix_ipca[i-1][j]


#photometry_pca = np.loadtxt(output_place + "photometry_pca.txt")
#matrix_ipca = np.loadtxt(output_place + "matrix_ipca.txt")
#matrix_difference = np.loadtxt(output_place + "matrix_difference.txt")
matrix_all = np.loadtxt(output_place + "ap_final.txt")


            
#np.savetxt(output_place + "4photometry_pca.txt", photometry_pca)
#np.savetxt(output_place + "4matrix_ipca.txt", matrix_ipca)
#np.savetxt(output_place + "4matrix_ratio.txt", matrix_ratio)
#np.savetxt(output_place + "matrix_all_final.txt", matrix_all)



#pixscale = pipeline.get_attribute("science_cropped", "PIXSCALE")
#size = pixscale*residuals.shape[-1]/2.

sizex = max(pca_numbers)
sizey = max(ipca_numbers_init)

#plt.figure()
#plt.imshow(matrix_ipca, origin='lower')
#plt.title("Aperture Photometry of IPCA")
#plt.xlabel('Number of PC', fontsize=12)
#plt.ylabel('Number of initial PC', fontsize=12)
#plt.xticks(np.arange(0, len(pca_numbers), 1), pca_numbers)
#plt.yticks(np.arange(0, len(ipca_numbers_init), 1), ipca_numbers_init)
#plt.colorbar()
#plt.savefig(os.path.join(output_place, "4matrix_ipca.pdf"), bbox_inches='tight')
#
#plt.figure()
#plt.imshow(matrix_ratio, origin='lower')
#plt.title("Aperture Photometry Ratio of IPCA and PCA")
#plt.xlabel('Number of PC', fontsize=12)
#plt.ylabel('Number of initial PC', fontsize=12)
#plt.xticks(np.arange(0, len(pca_numbers), 1), pca_numbers)
#plt.yticks(np.arange(0, len(ipca_numbers_init), 1), ipca_numbers_init)
#plt.colorbar()
#plt.savefig(os.path.join(output_place, "4matrix_ratio.pdf"), bbox_inches='tight')


plt.figure()
plt.imshow(matrix_all, origin='lower')
plt.title("Aperture Photometry")
plt.xlabel('Number of PC', fontsize=12)
#plt.ylabel('Number of initial PC', fontsize=12)
plt.xticks(np.arange(0, len(pca_numbers), 1), pca_numbers)
plt.yticks(np.arange(0, len(ipca_numbers_init)+1, 1), ["PCA"] + ipca_numbers_init)
plt.colorbar()
plt.savefig(os.path.join(output_place, "ap_final.pdf"), bbox_inches='tight')
#
#plt.figure()
#plt.imshow(fake[0, ], origin='lower', extent=[size, -size, -size, size], vmax=None)
#plt.title("Challenge Pynpoint - %i PCs"%(15))
#plt.xlabel('R.A. offset [arcsec]', fontsize=12)
#plt.ylabel('Dec. offset [arcsec]', fontsize=12)
#plt.colorbar()
#plt.savefig(os.path.join(output_place, "flux_fake.png"), bbox_inches='tight')
##hdu = fits.PrimaryHDU(data=residuals)
###hdu.writeto(os.path.join(output_place, "residuals_ipca_%i_%i.fits"%(rank_ipca_init, rank_ipca_end)))