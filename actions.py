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


class ActionHelloWorld(Action):

	def name(self) -> Text:
		return "sample_custom_action"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		print(tracker.get_slot("stock_name"))
		
		res = requests.get("http://localhost:5000/getStockPrice?stock=")

		response = res.content
		dispatcher.utter_message(response)

		return []
