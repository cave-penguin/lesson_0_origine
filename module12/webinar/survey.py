class AnonimousSurvey:
    def __init__(self, question) -> None:
        self.question = question
        self.responses = []


    def show_question(self):
        print(self.question)

    def store_response(self, new_question):
        self.responses.append(new_question)

    def show_result(self):
        print('Survey result')
        for response in self.responses:
            print(f'- {response}')