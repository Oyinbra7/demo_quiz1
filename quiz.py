import random


def get_questions():
    """Define and return the list of quiz questions."""
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "What is the value of pi (π) to two decimal places?",
            "choices", ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"],
            "answer": "C"
        },
        {
            "question": "Which gas is most abundant in the Earth’s atmosphere?",
            "choices": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen",
            "answer": "C"
        },
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": ["A) Charles Dickens", "B) George Orwell", "C) William Shakespeare", "D) Mark Twain"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the smallest prime number?",
            "choices": ["A) 0", "B) 1", "C) 2", "D) 3"],
            "answer": "C"
        }
    ]
    return questions

def shuffle_questions(questions):
    """Shuffle the order of questions to randomize the quiz."""
    random.shuffle(questions)
    return questions
