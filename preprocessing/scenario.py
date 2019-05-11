# -*- coding: utf-8 -*-

from typing import List
from multiprocessing import Pool, cpu_count
from preprocessing.clean import clean_number, validate_clean_sentences, clean_in_parentheses
from preprocessing.wakati import get_wakatis
from preprocessing.stop_word import get_stop_words
import logging

logger = logging.getLogger(__name__)

stop_words = get_stop_words()


def delete_stop_word(wakati_sentence_list: List[str]) -> List[str]:
    deleted = [morpheme for morpheme in wakati_sentence_list if morpheme not in stop_words]
    del wakati_sentence_list[:]
    del wakati_sentence_list
    return deleted


def run(sentences: List[str]) -> List[List[str]]:
    logger.info('start: preprocessing')

    logger.info('start: clean number')
    with Pool(cpu_count()) as p:
        preprocessed_sentences = p.map(clean_number, sentences)
    logger.info('end: clean number')

    del sentences[:]  # sentencesを上書きしてもgcがメモリ解放しないため
    del sentences

    logger.info('start: validate clean sentence')
    preprocessed_sentences = validate_clean_sentences(preprocessed_sentences)
    logger.info('end: validate clean sentence')

    logger.info('start: clean in parentheses')
    with Pool(cpu_count()) as p:
        preprocessed_sentences = p.map(clean_in_parentheses, preprocessed_sentences)
    logger.info('end: clean in parentheses')

    logger.info('start: wakati')
    preprocessed_sentences = get_wakatis(preprocessed_sentences)
    logger.info('end: wakati')

    logger.info('start: delete stop word')
    preprocessed_sentences = list(map(delete_stop_word, preprocessed_sentences))
    logger.info('end: delete stop word')

    return preprocessed_sentences
