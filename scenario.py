# -*- coding: utf-8 -*-

from file_io import read
import preprocessing.scenario
import settings

from os.path import join, dirname
from glob import glob
import logging
from datetime import datetime
from argparse import ArgumentParser

from gensim.models import word2vec


def train():
    sentences = read.sentences(glob(join(dirname(__file__), 'storage/texts/*.txt')))
    sentences = preprocessing.scenario.run(sentences=sentences)

    model = word2vec.Word2Vec(
        sentences=sentences,
        size=settings.DIMENSION,
        window=settings.WINDOW,
        min_count=settings.MIN_COUNT,
        workers=settings.WORKERS,
        iter=settings.EPOCH,
    )
    model.save(join(dirname(__file__), f'storage/model/{args.model_name}.model'))


if __name__ == '__main__':
    log_formatter = '%(levelname)s : %(asctime)s : %(message)s'
    log_filename = datetime.now().strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(filename=f'./storage/logs/{log_filename}.log', level=logging.DEBUG, format=log_formatter)

    parser = ArgumentParser()
    parser.add_argument('-o', '--model_name', help='モデルの保存名', default='output')
    args = parser.parse_args()

    train()
