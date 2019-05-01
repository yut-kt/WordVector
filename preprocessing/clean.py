# -*- coding: utf-8 -*-

import re
from typing import List

number_regexp = re.compile(r'[0-9０-９]+')
hiragane_regexp = re.compile(r'[ぁ-ん]')
brackets_regexp = re.compile(r'\(.+?\)|{.+?}|\[.+?\]|（.+?）|『.+?』|「.+?」|【.+?】|［.+?］|｢.+?｣|｛.+?｝')


def clean_number(sentence: str) -> str:
    return number_regexp.sub('0', sentence)


def is_include_hiragana(sentence: str) -> bool:
    return hiragane_regexp.search(sentence) is not None


def validate_clean_sentences(sentences: List[str]) -> List[str]:
    return [sentence for sentence in sentences if is_include_hiragana(sentence)]


def clean_in_parentheses(sentence: str) -> str:
    return brackets_regexp.sub('', sentence)
