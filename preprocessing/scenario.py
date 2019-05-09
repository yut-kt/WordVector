# -*- coding: utf-8 -*-

from typing import List
from multiprocessing import Pool, cpu_count
from preprocessing.clean import clean_number, validate_clean_sentences, clean_in_parentheses
from preprocessing.wakati import get_wakatis
from preprocessing.stop_word import delete_stop_word
import logging

logger = logging.getLogger(__name__)


def run(sentences: List[str]) -> List[List[str]]:
    logger.info('start: preprocessing')

    logger.info('start: clean number')
    with Pool(cpu_count()) as p:
        sentences = p.map(clean_number, sentences)
    logger.info('end: clean number')

    logger.info('start: validate clean sentence')
    sentences = validate_clean_sentences(sentences)
    logger.info('end: validate clean sentence')

    logger.info('start: clean in parentheses')
    with Pool(cpu_count()) as p:
        sentences = p.map(clean_in_parentheses, sentences)
    logger.info('end: clean in parentheses')

    logger.info('start: wakati')
    sentences = get_wakatis(sentences)
    logger.info('end: wakati')

    logger.info('start: delete stop word')
    with Pool(cpu_count()) as p:
        sentences = p.map(delete_stop_word, sentences)
    logger.info('end: delete stop word')

    return sentences
