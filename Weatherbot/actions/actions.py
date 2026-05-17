# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")

        if location:
            dispatcher.utter_message(text=f"The weather in {location} is sunny today.")
        else:
            dispatcher.utter_message(text="For which location?")

        return []