import numpy as np

def get_mean(array, n, target_dim, custom_flag = False, target_range = None):
    '''
    numpyによる2次元配列について、任意の方向、任意の範囲で平均をとる。

    ＜引数＞\\
    **must**

    - array :　numpy配列(2D)
    - n :　平均を取りたいデータ群の数(※平均するデータ数ではない)
    - target_dim :　平均したいデータがある次元

    **custom**

    - custom_flag :　平均したいレンジを指定するかどうか(T or F。Defaultでは全てのデータ)
    - target_range :　指定するレンジ
    '''
    mean_array = []

    if target_dim == 1:
        if not custom_flag:
            target_range = range(0,n)

        for i in range(0,n,1):
            mean_array.append(np.mean(array[i,target_range]))

    elif target_dim == 2:
        if not custom_flag:
            target_range = range(0,n)

        for i in range(0,n,1):
            mean_array.append(np.mean(array[target_range,i]))

    return mean_array