import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("You will be asked multiple-choice or fill-in-the-blank questions on a specific topic.")
        print("Let's begin!")

    def present_quiz_questions(self):
        for question in self.questions:
            print(question['question'])
            if question['type'] == 'multiple_choice':
                for i, choice in enumerate(question['choices'], 1):
                    print(f"{i}. {choice}")
                user_answer = input("Enter your choice (1, 2, 3, ...): ")
                if user_answer.lower() == question['answer'].lower():
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect! The correct answer is:", question['answer'])
            elif question['type'] == 'fill_in_the_blank':
                user_answer = input("Fill in the blank: ")
                if user_answer.lower() == question['answer'].lower():
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect! The correct answer is:", question['answer'])
            print()

    def calculate_final_score(self):
        print("Quiz completed! Let's see your final score.")
        print("Your score:", self.score)

    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            return True
        else:
            return False

if __name__ == "__main__":
    questions = [
        {
            'question': "What is the capital of France?",
            'type': 'multiple_choice',
            'choices': ["London", "Paris", "Berlin"],
            'answer': "Paris"
        },
        {
            'question': "Who wrote 'Romeo and Juliet'?",
            'type': 'fill_in_the_blank',
            'answer': "Shakespeare"
        }
        # Add more questions here...
    ]

    play_game = True

    while play_game:
        quiz = Quiz(questions)
        quiz.display_welcome_message()
        quiz.present_quiz_questions()
        quiz.calculate_final_score()
        play_game = quiz.play_again()

    print("Thanks for playing!")
