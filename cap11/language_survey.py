from survey import AnonymousSurvey

#Define una pregunta y hace una encuesta.
question = "What a language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Muestra la pregunta y guarda las respuestas a la pregunta.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Muestra los resultados de la encuesta
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()