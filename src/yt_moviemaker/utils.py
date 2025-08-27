import numpy as np
import os 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def get_n_files_with_suffix(dir_, suffix=".athdf"):
    """ 
    Determine how many output files are in a given directory [dir_] with a given [suffix]
    """
    filelist = np.asarray(os.listdir(dir_))
    return np.sum(np.asarray([1 if (filelist[i].endswith(suffix)) else 0 for i in range(len(filelist))]))

def gen_filelist_from_pattern(data_dir, filepattern, suffix):
    """ 
    Make a list of files from a pattern
    Unknown number of files, known data file patterning (very reasonable)
    """
    nfiles = get_n_files_with_suffix(data_dir, suffix)
    files = []
    for n in range(nfiles):
        files.append(f"{data_dir}{filepattern}{str(n).zfill(5)}{suffix}")
    return np.asarray(files)
            

def gen_custom_ticks(min_, max_, scale=30, noends=False):
    """ 
    Generate custom tick labels for a given min_ and max_ at scale spacing.
    If noends = True, the smallest and largest labels will be empty strings (useful if plotting multiple panels adjacent)
    """
    labels = [f"{int(i*scale)}" for i in np.linspace(min_, max_, 7)]
    if noends:
        labels[0] = labels[-1] = ""
    return labels
    
def yaxis_labels(ax, grid, ticklabels, ylabel):
    """ 
    Sets yaxis labels
    """
    ax.yaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, grid.shape[1], 7)))
    ax.set_yticklabels(ticklabels, fontsize=16)
    ax.set_ylabel(ylabel)
    return

def xaxis_labels(ax, grid, ticklabels, xlabel):
    """ 
    Sets xaxis labels
    """
    ax.xaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, grid.shape[0], 7)))
    ax.set_xticklabels(ticklabels, fontsize=16)
    ax.set_xlabel(xlabel)
    return
    
def physical_axes(ax, grid, region, xlabel, ylabel, scale=30, noends=False):
    """ 
    Sets physical axes for grid
    """
    xtlabels = gen_custom_ticks(region[0], region[1], scale, noends)
    xaxis_labels(ax, grid, xtlabels, xlabel)
    ytlabels = gen_custom_ticks(region[2], region[3], scale, noends)
    yaxis_labels(ax, grid, ytlabels, ylabel)
    return
    
    
    