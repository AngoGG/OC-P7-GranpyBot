#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-06
@note    0.0.1 (2020-12-06) : Init file
"""

from typing import Dict
from api.google_maps_api import GoogleMapsApi
from api.wiki_api import WikipediaApi
from parsing.sentence_parser import SentenceParser


class App:
    """This class is intended to drive the general application work by getting 
    the user research and returning him the bot response with APIs informations.
    """

    def __init__(self) -> None:
        """App init method.
        """
        self.google_maps: GoogleMapsApi = GoogleMapsApi()
        self.wikipedia: WikipediaApi = WikipediaApi()
        self.parser: SentenceParser = SentenceParser()

    def answer(self, query: str) -> Dict[str, any]:
        """From a user query, return a http Response containing the localisation, the wikipedia summary and links that 
        
        Args:
            name (type): Description. Default to False.
        
        Raises:
        Returns:
        """
        sentence: str = self.parser.get_clean_sentence(query)
        maps_info: Dict[str, float] = self.google_maps.search(sentence)

        wiki_infos = self.wikipedia.get_page_info(
            maps_info["address"], maps_info["coords"]
        )

        return {
            "info": {
                "location": maps_info["coords"],
                "address": maps_info["address"],
                "summary": wiki_infos["page_info"]["summary"],
                "url": wiki_infos["page_info"]["url"],
            },
            "search_type": wiki_infos["search_type"],
        }
