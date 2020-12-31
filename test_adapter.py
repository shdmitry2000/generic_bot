from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if statement.text.startswith('ירון'):
            return True
        else:
            return False


    def process(self, input_statement, additional_response_selection_parameters):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)

        # For this example, we will just return the input as output
        selected_statement = Statement(text='כאן הולכת התשובה שלי מתוך AI!!!')

        selected_statement.confidence = confidence

        return selected_statement