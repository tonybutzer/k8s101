import os
import sys
import subprocess

from playLib.bo_bucket import bo_get_bucket_list
from playLib.cl_numpy import np_load_cloud
from playLib.pl_objects import Play
from playLib.log_logger import log_make_logger

import logging
import boto3
from botocore.exceptions import ClientError

def s3cp(from_file):
    bucket='dev-rhassan'
    prefix='tony'
    objecta='{}/{}'.format(prefix,from_file)
    log.info(objecta)
    #upload_file(from_file, bucket, objecta)
    s3 = boto3.client('s3')
    with open(from_file, "rb") as f:
        s3.upload_fileobj(f, bucket, objecta)


def normal(x, amin, amax):
    x = (x+amin)/(amax-amin)
    return x

def make_fname(file):
     a=file.split('_')
     FNAME=a[0] + a[1] + '.png'
     return FNAME

def main_stuff(bucket_name, prefix, numpy_file, log):
    #log=log_make_logger('PNG Builder')
    
    pl=Play()

    bucket_file = '{}/{}{}'.format(bucket_name, prefix, numpy_file)
    print(bucket_file)
    ary = np_load_cloud(bucket_file)
    amin = ary.min()
    amax = ary.max()
    print(amin, amax)
    ary = normal(ary, amin, amax)
    fname=make_fname(numpy_file)
    print(fname)
    pl.pl_create_png(fname, ary, cmap='magma', title=fname, subtitle=fname)
    msg = '{} - created by fname with cmap = magma'.format(fname)
    log.info(msg)
    s3cp(fname)
    os.remove(fname)
    msg = '{} - removed/deleted'.format(fname)
    log.info(msg)
    
    
bucket_name = "ga-et-data"
prefix      = "Cloud_Veg_ET/Data/TMAX/"
numpy_file = "tmax_011_gw.tif.npy"

if len(sys.argv) > 1:
   global log
   log=log_make_logger('PNG Builder')
   log.info('YAY!')
   bucket_name, prefix, numpy_file = sys.argv[1].split(',')

main_stuff(bucket_name, prefix, numpy_file, log)
