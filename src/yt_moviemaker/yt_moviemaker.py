"""Main module."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable

import imageio_ffmpeg
plt.rcParams["animation.ffmpeg_path"] = imageio_ffmpeg.get_ffmpeg_exe()

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
                        "units_override": {"length_unit": (1.0, "cm"), "time_unit": (1.0, "s"),"mass_unit": (1.0, "g")},
                        "normalize":None,
                        'cmap':'turbo',
                        "save_dir":"./",
                        }
        

    def get_frames_athenaPP_hdf5(self, data_dir, filepattern, sim, customparams=None):
        print("Loading HDF5 files of Athena++ data")
        self.data_dir = data_dir
        self.sim = sim
        self.filepattern = filepattern
        if customparams is not None:
            for keys in customparams:
                # print(keys, customparams[keys], self.paramdict[keys])
                self.paramdict[keys] = customparams[keys]
                
        self.nfiles = u.get_n_files_with_suffix(data_dir, suffix='.athdf')
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

        return 1

    def get_frames_from_file_list(self, file_list, data_dir, filepattern, sim, customparams=None):
        print("Generating frames from a list of filepaths - should work for any type of input data that is yt-readable")
        self.data_dir = data_dir
        self.sim = sim
        self.filepattern = filepattern
        if customparams is not None:
            for keys in customparams:
                # print(keys, customparams[keys], self.paramdict[keys])
                self.paramdict[keys] = customparams[keys]
                
        self.nfiles = len(file_list)
        print(f"nfiles: {self.nfiles}")
        self.time_array = np.zeros(self.nfiles)
        self.frames_all = np.zeros((self.nfiles, self.paramdict['resolutionx'], self.paramdict['resolutiony']))
        
        for i in range(self.nfiles):
            file = file_list[i]
            print(file)
            ds = yt.load(file, units_override=self.paramdict["units_override"])
            self.time_array[i] = ds.current_time
            sl = ds.cutting(self.paramdict["normal"], self.paramdict["center"], self.paramdict["north_vec"])
            frb = FixedResolutionBuffer(sl, self.paramdict["region"], (self.paramdict["resolutiony"], self.paramdict["resolutionx"]))
            ### YYY why this ordering for shapes...hm.
            f = frb[self.paramdict["field"]]
            if self.paramdict["units"] is not None: f.to(self.paramdict["units"])
            self.frames_all[i] = f
        
        return 1

    def produce(self, filetype="gif", customfile = None):
        print(f"Making frames into a {filetype}")
        if customfile is not None:
            print(f"Saving into {customfile}")
            outfile = customfile
        else: 
            outfile = f"{self.paramdict["save_dir"]}/{self.sim}_{self.paramdict["field"]}_movie.{filetype}"
            
        fig, ax = plt.subplots(1, figsize=(10,10))
        f0 = self.frames_all[0]
        im = ax.pcolormesh(f0, norm=self.paramdict['normalize'], cmap=self.paramdict['cmap'])
        cax = ax.inset_axes([0.25, 0.05, 0.5, 0.05])
        cbar = plt.colorbar(im, cax=cax, orientation='horizontal')
        tx = ax.set_title(f"{self.sim} {self.paramdict["field"]} [{self.paramdict["units"]}] t={self.time_array[0]:.2f}")
        
        u.physical_axes(ax, f0, self.paramdict["region"], xlabel='x', ylabel='y')
        
        def animate(i):
            fi = self.frames_all[i]
            im.set_array(fi.ravel())
            if self.paramdict["normalize"] is None:
                im.set_clim(np.min(fi), np.max(fi))
            tx.set_text(f"{self.sim} {self.paramdict["field"]} [{self.paramdict["units"]}] t={self.time_array[i]:.2f}")
            
        self.ani = animation.FuncAnimation(fig, animate, frames=self.nfiles, interval=200, blit=False, repeat_delay=10_000)
        plt.tight_layout()
        
        print(outfile)
        if filetype == 'gif':
            self.ani.save(filename=outfile, writer='pillow')
        elif filetype == 'mp4':
            self.ani.save(filename=outfile, writer="ffmpeg")
        else:
            raise ValueError("That is not a valid file output type - must be 'gif' or 'mp4' ")
        
        return 1
        
            
