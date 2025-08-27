#!/usr/bin/env python
import pytest
import numpy as np

"""Tests for `yt_moviemaker` package."""

from yt_moviemaker import yt_moviemaker, utils

def test_init():
    x = yt_moviemaker.moviemaker()
    
def test_get_frames_athenaPP_hdf5():
    x = yt_moviemaker.moviemaker()
    data_dir = "./tests/test_data/"
    filepattern = "Blast.out1."
    sim = "blast1"
    tt = x.get_frames_athenaPP_hdf5(data_dir, filepattern, sim)
    # basically just testing for failures here...
    assert tt == 1
    tt = x.produce()
    assert tt == 1
    
def test_get_frames_from_file_list():
    x = yt_moviemaker.moviemaker()
    data_dir = "./tests/test_data/"
    filepattern = "Blast.out1."
    sim = "blast1"
    suffix = ".athdf"
    file_list = utils.gen_filelist_from_pattern(data_dir, filepattern, suffix)
    tt = x.get_frames_from_file_list(file_list, data_dir, filepattern, sim)
    assert tt == 1
    tt = x.produce()
    assert tt == 1
    