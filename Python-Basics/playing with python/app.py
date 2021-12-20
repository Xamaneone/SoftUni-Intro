from Question import Question

question_prompts = {
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) You dumbass, they don't have a color\n\n",
    "What color are Bananas?\n(a) Big\n(b) Medium|n\n(c) Yellow\n\n",
    "What color is a color?\n(a) D.Trump\n(b) Jultichko\n(c) Blue\n\n"
}

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)