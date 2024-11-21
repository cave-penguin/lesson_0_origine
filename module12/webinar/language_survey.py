from survey import AnonimousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonimousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break

    my_survey.store_response(response)

print("\nThank you to everyone who participated in survey!")
my_survey.show_result()
