import numpy as np
import glob
import os
import natsort as nsort

default_dir = "../numerical_data/"

def get_filenames_list_exp(directory, fnamePattern):
    '''
    numarical_data/ディレクトリ内の
    指定したディレクトリとファイルパターンから、
    数値例ファイルのファイル名リストとファイル数を取得
    '''
    file_names = []
    full_pattern = os.path.join(default_dir, directory, fnamePattern)
    files = glob.glob(full_pattern)
    n_files = len(files)

    if not files:
        print(f"WARNING: パターン '{full_pattern}' に一致するファイルが見つかりません。")
        return []

    for f in files:
        file_name = os.path.basename(f)
        file_names.append(file_name)

    file_names = nsort.natsorted(file_names)
    # file_names = nsort.natsorted([os.path.basename(f) for f in files])

    return file_names, n_files

def read_files(directory, file_names):
    '''
    get_filenames等で作成されるファイル名のリストをもとに、
    それらのファイルデータの読み込みを行う。
    
    ファイルデータは、
    ```
    (id) (data)
    :
    :
    :
    ```
    の形式
    '''
    all_data = []

    for file_name in file_names:
        data = []
        with open(default_dir+directory+file_name, 'r') as file:
            for line in file:
                value = line.split()[1]
                data.append(float(value))
        all_data.append(np.array(data))

    array = np.array(all_data)

    return array