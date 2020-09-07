# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# -*- coding: utf-8 -*-
import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

# from actions.api.gdrive_service import GDriveService


logger = logging.getLogger(__name__)


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "sales_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email",
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        person_name = tracker.get_slot("person_name")
        import datetime

        budget = tracker.get_slot("budget")
        company = tracker.get_slot("company")
        email = tracker.get_slot("business_email")
        job_function = tracker.get_slot("job_function")
        person_name = tracker.get_slot("person_name")
        use_case = tracker.get_slot("use_case")
        date = datetime.datetime.now().strftime("%d/%m/%Y")

        sales_info = [company, use_case, budget, date, person_name, job_function, email]
        print(sales_info)
        dispatcher.utter_message(template="utter_confirm_salesrequest", user_name=person_name)
        return []

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
    #     """A dictionary to map required slots to
    #     - an extracted entity
    #     - intent: value pairs
    #     - a whole message
    #     or a list of them, where a first match will be picked"""
    #     return {"use_case": self.from_text(intent="inform")}

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "job_function": [
                self.from_entity(entity="job_function"),
                self.from_text(intent="enter_data"),
            ],
            "use_case": [self.from_text(intent="enter_data")],
            "budget": [
                self.from_entity(entity="amount-of-money"),
                self.from_entity(entity="number"),
                self.from_text(intent="enter_data"),
            ],
            "person_name": [
                self.from_entity(entity="name"),
                self.from_text(intent="enter_data"),
            ],
            "company": [
                self.from_entity(entity="company"),
                self.from_text(intent="enter_data"),
            ],
            "business_email": [
                self.from_entity(entity="email"),
                self.from_text(intent="enter_data"),
            ],
        }

    def validate_business_email(
        self, value, dispatcher, tracker, domain
    ) -> Dict[Text, Any]:
        """Check to see if an email entity was actually picked up by duckling."""

        if any(tracker.get_latest_entity_values("email")):
            # entity was picked up, validate slot
            return {"business_email": value}
        else:
            # no entity was picked up, we want to ask again
            dispatcher.utter_message(template="utter_no_email")
            return {"business_email": None}
    #
    # def submit(
    #     self,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> List[EventType]:
    #     """Once we have all the information, attempt to add it to the
    #     Google Drive database"""
    #
    #     import datetime
    #
    #     budget = tracker.get_slot("budget")
    #     company = tracker.get_slot("company")
    #     email = tracker.get_slot("business_email")
    #     job_function = tracker.get_slot("job_function")
    #     person_name = tracker.get_slot("person_name")
    #     use_case = tracker.get_slot("use_case")
    #     date = datetime.datetime.now().strftime("%d/%m/%Y")
    #
    #     sales_info = [company, use_case, budget, date, person_name, job_function, email]
    #
    #     try:
    #         gdrive = GDriveService()
    #         gdrive.store_data(sales_info)
    #         dispatcher.utter_message(template="utter_confirm_salesrequest")
    #         return []
    #     except Exception as e:
    #         logger.error(
    #             "Failed to write data to gdocs. Error: {}" "".format(e.message),
    #             exc_info=True,
    #         )
    #         dispatcher.utter_message(template="utter_salesrequest_failed")
    #         return []

    # def request_next_slot(self, dispatcher, tracker, domain):
    #
    #     for slot in self.required_slots(tracker):
    #         if self._should_request_slot(tracker, slot):
    #             if slot == "person_name" and tracker.get_slot("person_name") == "yxp":
    #                 dispatcher.utter_message(text="对不起，不欢迎你，走开！！")
    #                 return self.deactivate()
    #             dispatcher.utter_message(
    #                 template=f"utter_ask_{slot}", **tracker.slots
    #             )
    #             return [SlotSet("requested_slot", slot)]
    #     return None
    def request_next_slot(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any],
    ) -> Optional[List[EventType]]:
        """Request the next slot and utter template if needed,
            else return None"""
        for slot in self.required_slots(tracker):
            print(slot)
            if slot == "person_name" and tracker.get_slot("person_name") == "yxp":
                dispatcher.utter_message(text="对不起，不欢迎你，走开！！")
                return self.deactivate()

            if self._should_request_slot(tracker, slot):
                print("_should_request_slot")

                ## Condition of validated slot that triggers deactivation
                if slot == "person_name" and tracker.get_slot("person_name") == "yxp":
                    dispatcher.utter_message(text="对不起，不欢迎你，走开！！")
                    return self.deactivate()

                ## For all other slots, continue as usual
                logger.debug(f"Request next slot '{slot}'")
                dispatcher.utter_message(
                    template=f"utter_ask_{slot}", ** tracker.slots
                )
                REQUESTED_SLOT = "requested_slot"
                return [SlotSet(REQUESTED_SLOT, slot)]
            print("not _should_request_slot")
        return None