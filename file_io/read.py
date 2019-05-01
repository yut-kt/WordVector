# -*- coding: utf-8 -*-

import settings

from typing import List
from multiprocessing import Pool
from itertools import chain


def __extract_sentence(line: str) -> str:
    try:
        _, sentence = line.split()
        return sentence
    except Exception:
        return ''


def __extract_sentences(path: str) -> List[str]:
    with open(path) as f:
        return [sentence for sentence in map(__extract_sentence, f.read().splitlines()) if sentence]


def sentences(paths: List[str]) -> List[str]:
    with Pool(settings.WORKERS) as p:
        sentences_list = p.map(__extract_sentences, paths)

    return list(chain.from_iterable(sentences_list))
