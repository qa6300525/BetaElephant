
#!/usr/bin/python3
#-*-coding:utf-8-*-
#$File: config.py
#$Date: Sat May  7 11:00:28 2016
#$Author: Like Ma <milkpku[at]gmail[dot]com>

import tensorflow as tf

class Config(object):

    # dataset
    data_shape = [None, 9, 10, 32]
    label_shape = [None, 9, 10, 32]

    # model
    dtype=tf.float32

    # training
    optimizer = tf.train.AdamOptimizer(1e-4)
    n_epoch = 2000
    minibatch_size = 128
    evalue_point = 20
    check_point = 200

    # saving
    save_path = 'train_log/model.ckpt'


