"""Main module."""
import numpy as np
import matplotlib.pyplot as plt
import yt
from yt import FixedResolutionBuffer
yt.set_log_level('error')

import yt_moviemaker.utils as u


class moviemaker(object):
    def __init__(self):
        print("Initialized object")
        self.paramdict={"region":(-1, 1, -1, 1),
                        "resolutionx": 64,
                        "resolutiony": 64,
                        "field": 'density',
                        "units" : 'g/cm**3',
                        "normal" : [0, -1, 0],
                        "center" : [0,0,0],
                        "north_vec" : [0,0,1],
                        "units_override": {"length_unit": (1.0, "cm"), "time_unit": (1.0, "s"),"mass_unit": (1.0, "g")}
                        }

    def get_frames_athenaPP_vtk(self):
        print("Loading .vtk files of Athena++ data")

    def get_frames_athenaPP_hdf5(self, data_dir, filepattern, customparams=None):
        print("Loading HDF5 files of Athena++ data")
        self.data_dir = data_dir
        self.filepattern = filepattern
        if customparams is not None:
            for keys in customparams:
                # print(keys, customparams[keys], self.paramdict[keys])
                self.paramdict[keys] = customparams[keys]
                

        self.nfiles = u.get_n_outputs(data_dir)
        print(f"nfiles: {self.nfiles}")
        self.time_array = np.zeros(self.nfiles)
        self.frames_all = np.zeros((self.nfiles, self.paramdict['resolutionx'], self.paramdict['resolutiony']))


        for i in range(self.nfiles):
            file = f"{data_dir}{filepattern}{str(i).zfill(5)}.athdf"
            print(file)
            ds = yt.load(file, units_override=self.paramdict["units_override"])
            self.time_array[i] = ds.current_time
            sl = ds.cutting(self.paramdict["normal"], self.paramdict["center"], self.paramdict["north_vec"])
            frb = FixedResolutionBuffer(sl, self.paramdict["region"], (self.paramdict["resolutiony"], self.paramdict["resolutionx"]))
            ### YYY why this ordering for shapes...hm.
            f = frb[self.paramdict["field"]]
            if self.paramdict["units"] is not None: f.to(self.paramdict["units"])
            self.frames_all[i] = f

        return 

    def get_frames_from_yt_ds(self, ds):
        print("Generating frames from a dataset already loaded into yt")

    def produce(self, filetype="gif", customfile = None):
        print(f"Making frames into a {filetype}")
        if customfile is not None:
            print(f"Saving into {customfile}")
