from __future__ import print_function
import numpy as np

import sys

if sys.version_info.major == 2:
  def range(start, stop=None, step=None):
      start = int(start)
      if stop is None:
          return xrange(start)
      elif step is None:
          step = int(stop)
          return xrange(start, stop)
      else:
          stop = int(stop)
          step = int(step)
          return xrange(start, stop, step)

EXC, INH = 0, 1
ROW, COL = 0, 1
OFF, ON = 0, 1
D2R = np.pi/180.
R2D = 180./np.pi
MERGED, SPLIT = 0, 1
dvs_modes = ['merged', 'split']

def deg2rad(d):
    return D2R*d

def rad2deg(r):
    return R2D*r

def normalize(mat):
  w = 1./np.sum(np.abs(mat))
  return mat*w, w

def conv2one(mat):
  w = 1./np.sqrt(np.sum(mat**2))
  return mat*w, w

def sum2zero(mat):
  return mat - np.mean(mat)

def seed_rand(seed=None):
    # if seed is None:
        # time.sleep(0.001)
        # seed = np.uint32(time.time()*(10*15))
    np.random.seed(seed)

def subsamp_size(start, end, step):
    return ( (end - start - 1)//step ) + 1

def print_debug(txt):
    print("------------------------------------------------------------")
    print(txt)
    print("------------------------------------------------------------")
