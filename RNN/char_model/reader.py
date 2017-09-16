import pickle
import time
from os import path


# data I/O
# should be simple plain text file
start_time = time.time()

data = open('../dataset/temp_input.txt', 'r').read()

data_read_time = time.time()
print "Time taken to read data : ", data_read_time - start_time

data_len = len(data)
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)
print 'data has %d characters, %d unique.' % (data_size, vocab_size)
char_to_ix = {ch: i for i, ch in enumerate(chars)}
ix_to_char = {i: ch for i, ch in enumerate(chars)}

preproc_time = time.time()
print "Time taken for preprocessing : ", preproc_time - data_read_time
