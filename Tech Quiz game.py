# -------------------------
def game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    choice = input("Do you want to play again? (yes or no): ")
    choice = choice.upper()

    if choice == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "what is API: ": "A",
 "what is ACL?: ": "B",
 "what is BGP: ": "C",
 "what is CLI: ": "A",
 "what is CPU:": "D",
 "what is DMI:":"B"
}

options = [["A.Application programming interface", "B. application", "C. agreement", "D. application management"],
          ["A.accessing point", "B. Access control list", "C. accessing interface", "D.fttgrt"],
          ["A. bd protocol", "B. built protocol", "C. border gateway protocol", "D. SNL"],
          ["A. command line interpreter","B. False", "C. sometimes", "D. cl interpreter"],
          ["A.command process unique","B.control point ultra","C.conform program upi","D.control process unit"],
          ["A.data management","B.desktop management interface","C.dmi","D.data managemenrt"]]

game()

while play_again():
    game()

print("Byeeeeee!")

# ------------------------