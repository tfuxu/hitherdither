"""
:mod:`utils`
=======================

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>
Created on 2016-09-12, 09:50

"""

import numpy as np
from PIL import Image


def np2pil(img):
    return Image.fromarray(np.array(img, "uint8"))


def pil2np(img):
    return np.array(img, "uint8")
