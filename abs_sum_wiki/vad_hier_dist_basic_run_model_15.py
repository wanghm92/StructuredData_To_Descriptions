from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import time
import math
import sys
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
from optparse import OptionParser
from models.vad_hier_dist_basic_15_model import *
from models.basic_files.dataset_iterator_hier_15 import *
from run_model_hier_15 import *
import os



def main():
    parser = OptionParser()
 
    parser.add_option(
    "-w", "--work-dir", dest="wd", default="../Data/")
    parser.add_option(
        "-l", "--learning-rate", dest="lr", default=0.0001)
    parser.add_option(
        "-e", "--embedding-size", dest="emb_size",
        help="Size of word embeddings", default=50)
    parser.add_option(
        "-s", "--hidden-size", dest="hid_size",
        help="Hidden size of the cell unit", default=100)
    parser.add_option(
        "-a", "--batch-size", dest="batch_size",
        help="Number of examples in a batch", default=32)
    parser.add_option(
        "-n", "--epochs", dest="epochs",
        help="Maximum Number of Epochs", default=10)

    parser.add_option(
        "-t", "--early_stop", dest="early_stop",
        help="Stop after these many epochs if performance on validation is not improving", default=2)

    parser.add_option(
        "-o", "--output_dir", dest="outdir",
        help="Output directory where the model will be stored", default="../out/")

    parser.add_option(
        "-x", "--emb-train", dest="emb_tr")

    parser.add_option(
	"-p", "--vocab-freq", dest="vocab_frequency")
    parser.add_option(
	"-m", "--num-fields", dest="num_fields")

    parser.add_option(
	"-f", "--feed-previous", dest="feed_previous")

    parser.add_option(
	"-j", "--is_stay", dest="is_stay")

    parser.add_option(
	"-k", "--is_stay_nlb", dest="is_stay_nlb")

    (option, args) = parser.parse_args(sys.argv)


    if (int(option.emb_tr) == 1):
        x = True
    else:
        x = False 

    if (option.is_stay == 'True'):
	is_stay = True
    else:
	is_stay = False

    if (option.is_stay_nlb == 'True'):
        is_stay_nlb = True
    else:
	is_stay_nlb = False
    c = Config(float(option.lr), int(option.emb_size), int(option.hid_size), int(option.batch_size),
                int(option.epochs), early_stop=int(option.early_stop), outdir= option.outdir, emb_tr=x, feed_previous=int(option.feed_previous), 
		num_fields = int(option.num_fields), vocab_frequency=int(option.vocab_frequency), is_stay = is_stay, is_stay_nlb = is_stay_nlb)


    run_attention = run_model(option.wd, BasicAttention(), c)
    run_attention.run_training()



if __name__ == '__main__':
    main()

