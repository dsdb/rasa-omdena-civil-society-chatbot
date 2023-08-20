from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class TestActionCivilSocietyGetPartners(Action):
    def name(self) -> Text:
        return "test_action_civil_society_get_partners"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        civil_society_partners = ["Value1", "Value2", "Value3"]

        # Set the value of the 'civil_society_partner' slot to the fetched data
        return [SlotSet("civil_society_partners", civil_society_partners)]
