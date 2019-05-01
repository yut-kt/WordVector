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
    return [morpheme for morpheme in wakati_sentence_list if morpheme not in stop_words]


def run(sentences: List[str]) -> List[List[str]]:
    logger.info('start: preprocessing')

    logger.info('start: clean number')
    cleaned_number_sentences = list(map(clean_number, sentences))
    logger.info('end: clean number')

    logger.info('start: validate clean sentence')
    validated_clean_sentences = validate_clean_sentences(cleaned_number_sentences)
    logger.info('end: validate clean sentence')

    logger.info('start: clean in parentheses')
    cleaned_in_parentheses = list(map(clean_in_parentheses, validated_clean_sentences))
    logger.info('end: clean in parentheses')

    logger.info('start: wakati')
    wakatis_list = get_wakatis(cleaned_in_parentheses)
    logger.info('end: wakati')

    logger.info('start: delete stop word')
    with Pool(cpu_count()) as p:
        deleted_stop_word_sentence = p.map(delete_stop_word, wakatis_list)
    logger.info('end: delete stop word')

    return deleted_stop_word_sentence
