from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        if statement.text.startswith('dimi'):
            return True
        else:
            return False


    def process(self, input_statement, additional_response_selection_parameters):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)

        # For this example, we will just return the input as output
        print('input_statement',type(input_statement),input_statement)
        selected_statement = Statement(text='The current temperature is ')

        selected_statement.confidence = confidence

        return selected_statement