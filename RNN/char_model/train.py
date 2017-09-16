import tensorflow as tf
from reader import *

data = tf.placeholder(tf.float32, [None, 25,1])
target = tf.placeholder(tf.float32, [None, vocab_size])

num_hidden = 24
cell = tf.nn.rnn_cell.LSTMCell(num_hidden,state_is_tuple=True)

val, state = tf.nn.dynamic_rnn(cell, data, dtype=tf.float32)
