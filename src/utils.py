import numpy as np

def get_mean(array, n, target_dim, custom_flag = False, target_range = None):
    '''
    array: numpy配列 (n x m)
    custom_flag: 

    '''
    mean_array = []

    if target_dim == 0:
        if not custom_flag:
            target_range = range(0,n)

        for i in range(0,n,1):
            mean_array.append(np.mean(array[i,target_range]))

    elif target_dim == 1:
        if not custom_flag:
            target_range = range(0,n)

        for i in range(0,n,1):
            mean_array.append(np.mean(array[target_range,i]))

    return mean_array