"""
tools
-----------

:copyright: 2017-05-10 by hbldh <henrik.blidh@nedomkull.com>

"""

import pytest
from pathlib import Path

from hitherdither.data import _image


@pytest.fixture(scope='session')
def test_png():
    p = Path(__file__).parent.joinpath('astronaut.png')
    url = 'https://raw.githubusercontent.com/scikit-image/scikit-image/master/skimage/data/astronaut.png'
    i = _image(p, url)
    return i


@pytest.fixture(scope='session')
def test_jpeg():
    p = Path(__file__).parent.joinpath('rocket.jpg')
    url = 'https://raw.githubusercontent.com/scikit-image/scikit-image/master/skimage/data/rocket.jpg'
    i = _image(p, url)
    return i
