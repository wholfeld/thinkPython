from os.path import dirname, join
import os
import sys
from hashlib import md5


def md5sum(file_path):
    with open(file_path, 'rb') as f:
        file = f.read()
    m = md5()
    m.update(file)
    m_bits = m.digest()
    return (m_bits, file_path)

def search_for(file_type):
    md5_dict = dict()
    file_path = join(dirname(__file__), "./")
    for currentpath, folders, files in os.walk(file_path): #'.'):
        for file in files:
            if file_type in file:
                cur_file_path = os.path.join(currentpath, file)
                # print(md5sum(cur_file_path))
                md5_tup = md5sum(cur_file_path)
                file_md5 = md5_tup[0]
                file_path = md5_tup[1]
                md5_dict.setdefault(file_md5, []).append(file_path)
                # md5_dict[file_md5] = md5_dict.get(file_md5, []).append(file_path)

    for key in md5_dict:
        print(f'{key}:{md5_dict[key]}')

search_for('txt')
# read_file = 'happy.txt'
# file_path = join(dirname(__file__), "./", read_file)
# md5sum(file_path)