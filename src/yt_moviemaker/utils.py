def do_something_useful():
    print("Replace this with a utility function")

import numpy as np
import os 

def get_n_outputs(dir_):
    """ Determine how many output files are in a given directory
    """
    filelist = np.asarray(os.listdir(dir_))
    return np.sum(np.asarray([1 if (filelist[i].endswith(".athdf")) else 0 for i in range(len(filelist))]))