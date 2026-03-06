from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSkincareAdvice(Action):

    def name(self):
        return "action_skincare_advice"

    def run(self, dispatcher, tracker, domain):

        user_message = tracker.latest_message.get("text")

        if "oily" in user_message.lower():
            advice = "For oily skin: Use gel-based cleanser, oil-free moisturizer, and sunscreen."
        elif "dry" in user_message.lower():
            advice = "For dry skin: Use hydrating cleanser, thick moisturizer, and avoid harsh soaps."
        elif "combination" in user_message.lower():
            advice = "For combination skin: Use mild cleanser and lightweight moisturizer."
        else:
            advice = "Please tell me your skin type (oily/dry/combination)."

        dispatcher.utter_message(text=advice)
        return []


class ActionHaircareAdvice(Action):

    def name(self):
        return "action_haircare_advice"

    def run(self, dispatcher, tracker, domain):

        user_message = tracker.latest_message.get("text")

        if "curly" in user_message.lower():
            advice = "For curly hair: Use sulfate-free shampoo and deep condition weekly."
        elif "dry" in user_message.lower():
            advice = "For dry hair: Use hydrating shampoo and apply hair oil twice a week."
        elif "oily" in user_message.lower():
            advice = "For oily scalp: Use mild shampoo and avoid heavy conditioners."
        else:
            advice = "Please tell me your hair type (curly/dry/oily)."

        dispatcher.utter_message(text=advice)
        return []
