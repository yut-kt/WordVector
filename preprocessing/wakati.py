# -*- coding: utf-8 -*-

import subprocess
import MeCab
from typing import List
from multiprocessing import Pool, cpu_count


def get_neologd():
    dicdir = subprocess.run(
        ['mecab-config', '--dicdir'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    ).stdout.decode().strip()

    return f'{dicdir}/mecab-ipadic-neologd'


mecab = MeCab.Tagger(f'-d {get_neologd()}')


def get_wakati_list(sentence: str) -> List[str]:
    wakati = []
    for result in mecab.parse(sentence).split('\n'):
        if result == 'EOS':
            break
        morpheme, morpheme_info = result.split('\t', maxsplit=1)
        word_class, _ = morpheme_info.split(',', maxsplit=1)
        if word_class != '記号':
            wakati.append(morpheme)
    return wakati


def get_wakatis(sentences: List[str]):
    with Pool(cpu_count()) as p:
        return p.map(get_wakati_list, sentences)
