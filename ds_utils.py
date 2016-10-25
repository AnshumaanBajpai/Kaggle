# -*- coding: utf-8 -*-
'''
The file has some basic utility functions that are needed over and over in data processing
'''

__author__  = "Anshumaan Bajpai"


# Importing the required library
import pandas as pd
import os
import tarfile, zipfile
import os
import numpy as np
import cv2
import sys

# The script contains all the utility functions that I use for typical data
# analysis for the kaggle projects. The functions are related to extracting
# compressed files, performing data cleaning and so on

###############################################################################
def uncom_tgz(fpath):
    '''
    Function to uncompress a .tgz file
    
    @params
    fpath: .tgz file to be extracted
    type fpath: string

    return: 
    None
    '''

    # Uncompressing the files in the same directory as the compressed file
    # Obtaining the directory based on file name
    fdir, sep, fname = fpath.rpartition('/')

    #print fdir, sep, fname
    if not (fdir==""):
        os.chdir(fdir)
    
    tar = tarfile.open(fname)
    tar.extractall()
    tar.close()

    return None

#uncom_tgz('MassiveData/yelpDS/sample_submission.csv.tgz')


###############################################################################
def uncom_zip(fpath):
    '''
    Function to uncompress a .zip file
    
    @params
    fpath: .zip file to be extracted
    type fpath: string

    return: 
    None
    '''
    
    # Uncompressing the files in the same directory as the compressed file
    # Obtaining the directory based on file name
    fdir, sep, fname = fpath.rpartition('\\')

    # print fdir, sep, fname
    if not (fdir==""):
        os.chdir(fdir)
    
    zip_ref = zipfile.ZipFile(fpath, 'r')
    zip_ref.extractall(fdir)
    zip_ref.close()

    return None


###############################################################################
def csv_overview(fpath):
    '''
    Function to analyze a basic csv file to give an overview

    @params 
    fpath: .csv file to be analyzed
    type fpath: string
    
    return:
    Dictionary with the overall information
    'size in kb': Size of the file in kbs
    'readfile': A pandas data frame with basic file info
    '''

    # Obtaining the directory and the filename
    fdir, sep, fname = fpath.rpartition('/')
    print fname
    if not (fdir==""):
        os.chdir(fdir)

    # Analysis and output
    output = dict()
    output['size in kb'] = os.path.getsize(fname)/1000
    read_data = pd.read_csv(fname, sep=',', skipinitialspace=True,
                            skip_blank_lines=True, nrows=10)
    output['readfile'] = read_data

    return output

#csv_overview('MassiveData/yelpDS/train.csv')


###############################################################################
## A class that loads an image as a RGB object
class RGBHistogram:
    # Constructor
    def __init__(self, bins):
        # store the number of bins the histogram will use
        self.bins=bins

    # function to create feature vectors
    def describe(self, image):
        # Compute a 3D histogram in RGB colorspace
        hist = cv2.calcHist([image], [0,1,1], None, self.bins,
                            [0, 256, 0,256, 0,256])
        # Normalizing the histograms so that images to compare different sizes
        #print type(hist)
        cv2.normalize(hist, hist)

        # Return the 3D histogram as a flattened array
        return hist.flatten()


###############################################################################
## Import the file as a module to be able to use it
if __name__ == "__main__":
    print "You need to import this file to use it"
    #uncom_zip('C:\Users\Anshumaan\Desktop\Github\Kaggle\kaggleData\PredRedHatBusVal\sample_submission.csv.zip')
