#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-01
@note    0.0.1 (2020-12-01) : Init file
"""

from pathlib import Path
from typing import List
import json
import pytest
import re


class SentenceParser:
    """Class which handle the user query parsing to query the APIs.
    """

    def __init__(self) -> None:
        """Constructor"""
        self.stop_words: List[str] = json.loads(
            Path("parsing/stop_words.json").read_bytes()
        )

    @staticmethod
    def _split_words(sentence: str) -> List[str]:
        """This method splits a sentence string to a list of words.
        
        Args:
            sentence (str): A user sentence.
        
        Returns:
            A list of all user sentence words.
        """

        splitted_words: List[str] = re.split(r"\W", sentence.lower())

        return list(filter(None, splitted_words))

    def _remove_stop_words(self, words_list: List[str]) -> List[str]:
        """This method returns a list of all the non stop_words from a words list.
        
        Args:
            words_list (List[str]): List of words to be cleaned from stop words
        
        Returns:
            A list of words without any stop word.
        """
        return [word for word in words_list if word not in self.stop_words]

    @staticmethod
    def _rebuild_sentence(words_list: List[str]) -> str:
        """From a words list, returns a sentence string.
        
        Args:
            words_list (List[str])): Words list to be rebuild as a sentence.
        
        Returns:
            A sentence with all words from the list, separated with space.
        """
        return " ".join(words_list)

    def get_clean_sentence(self, sentence: str) -> str:
        """From a user sentence, return a clean sentence to query APIs.
        
        Args:
            sentence (str): User query sentence.

        Returns:
            Clean sentence to query APIs
        """

        return self._rebuild_sentence(
            self._remove_stop_words(self._split_words(sentence))
        )

