#!/usr/bin/env python
import pytest
import numpy as np

"""Tests for `yt_moviemaker` package."""

from yt_moviemaker import utils


def test_test():
    assert True

def test_get_n_athdf_outputs():
    nfound = utils.get_n_athdf_outputs("./")
    assert nfound == 0
    
def test_gen_custom_ticks():
    tt = utils.gen_custom_ticks(-15, 15, 30, False)
    d = ["-450", "-300", "-150", "0", "150", "300", "450"]
    assert tt == d
    tt = utils.gen_custom_ticks(-15, 15, 30, True)
    d2 = ["", "-300", "-150", "0", "150", "300", ""]
    assert tt == d2