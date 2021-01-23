# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests

class ActionRandomAnime(Action):

    def name(self) -> Text:
        return "action_random_anime"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text="Hello World!")
        r = requests.get('http://animevost.club/random')
        text_ = r.text
        begin = text_.find('<div class="img-games"> <center><a href="')
        end = text_.find('" rel="nofollow" target="_blank">')
        text_ = text_[begin + len('<div class="img-games"> <center><a href="'):end]
        dispatcher.utter_message(text="Попробуй этот шедевр " + text_)

        return []
