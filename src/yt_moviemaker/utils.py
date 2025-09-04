import numpy as np
import os 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def get_n_files_with_suffix(data_dir, suffix=".athdf"):
    """ Determine how many output files are in a given directory **dir_** with a given **suffix**
    
    **Args:**
        data_dir (str): filepath to the data directory to be searched
        
        suffix (str): string for file ends to be counted  
      
    **Returns:**
        int: the total number of files with *suffix* in *dir_* 
    
    """
    filelist = np.asarray(os.listdir(data_dir))
    return np.sum(np.asarray([1 if (filelist[i].endswith(suffix)) else 0 for i in range(len(filelist))]))

def gen_filelist_from_pattern(data_dir, filepattern, suffix):
    """ Make a list of files from a given pattern
    
        Unknown number of files, known data file patterning
        
        Assumes a file pattern of {data_dir}/{filepattern}0000i{suffix}
        
        i.e. ../data/myfilename.00001.athdf
        
    **Args:** 
        data_dir (str): filepath to the data directory
        
        filepattern (str): how the files are named
        
        suffix (str): file ending string
        
    **Returns:**
        filelist (array): an in-order list of the file paths for the given pattern
    """
    nfiles = get_n_files_with_suffix(data_dir, suffix)
    files = []
    for n in range(nfiles):
        files.append(f"{data_dir}{filepattern}{str(n).zfill(5)}{suffix}")
    return np.asarray(files)
            

def gen_custom_ticks(mmin, mmax, scale=1, noends=False):
    """ Generate custom tick labels for a given **min** and **max** at **scale** spacing.
    
        If noends = True, the smallest and largest labels will be empty strings (useful if plotting tightly spaced adjacent panels)
        
        If scale=1, will produce spacing along min-max evenly. Scale can be changed to other values to i.e. 
        rescale data from simulation scale to real. 
        
        **Args:**
            mmin (float): Minimum value for the axis
            
            mmax (float): Maximum value for the axis
            
            scale (float): rescales values along axis
            
            noends (bool): Handles whether or not to make the end values empty strings
        
        **Returns:**
            labels (list of str): axis labels
        
    """
    labels = [f"{int(i*scale)}" for i in np.linspace(min_, max_, 7)]
    if noends:
        labels[0] = labels[-1] = ""
    return labels
    
def yaxis_labels(ax, grid, ticklabels, ylabel):
    """ Sets yaxis labels and ticks
    
    **Args:**
        ax (matplotlib object): ax to set on
        grid (array): data grid to get sizing of
        ticklabels (list of str):  labels for ticks (gen_custom_ticks())
        ylabel (str): y axis label
        
    **Returns:**
        1 if successful
    """
    ax.yaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, grid.shape[1], 7)))
    ax.set_yticklabels(ticklabels, fontsize=16)
    ax.set_ylabel(ylabel)
    return 1

def xaxis_labels(ax, grid, ticklabels, xlabel):
    """Sets xaxis labels and ticks
    
    **Args:**
        ax (matplotlib object): ax to set on
        grid (array): data grid to get sizing of
        ticklabels (list of str):  labels for ticks (gen_custom_ticks())
        xlabel (str): x axis label
        
    **Returns:**
        1 if successful
    """
    ax.xaxis.set_major_locator(ticker.FixedLocator(np.linspace(0, grid.shape[0], 7)))
    ax.set_xticklabels(ticklabels, fontsize=16)
    ax.set_xlabel(xlabel)
    return 1
    
def physical_axes(ax, grid, region, xlabel, ylabel, scale=1, noends=False):
    """ Sets both axes for grid
    
    **Args:**
        ax (matplotlib object): ax to set on
        
        grid (array): data grid to get sizing of
        
        region (tuple): 4 value tuple of the (xmin, xmax, ymin, ymax) of the grid
        
        xlabel (str): x axis label
        
        ylabel (str): y axis label
        
        scale (float): rescales values along axis
        
        noends (bool): Handles whether or not to make the end values empty strings
        
    **Returns:**
        1 if successful
    """
    xtlabels = gen_custom_ticks(region[0], region[1], scale, noends)
    xaxis_labels(ax, grid, xtlabels, xlabel)
    ytlabels = gen_custom_ticks(region[2], region[3], scale, noends)
    yaxis_labels(ax, grid, ytlabels, ylabel)
    return 1
    
    
    