import random


def get_questions():
    """Define and return the list of quiz questions."""
    questions = [
        {
            "question": "How many ethnic groups do we have in Nigeria?",
            "choices": ["A) 250", "B) 3", "C) 776", "D) 400"],
            "answer": "A"
        },
        {
            "question": "In Nigeria, democracy day is now celebrated on:",
            "choices": ["A) May 1st", "B) June 12th", "C) October 1st", "D) May 29th"],
            "answer": "B"
        },
        {
            "question": " Which continent is the smallest in the world?",
            "choices": ["A) South America", "B) Africa", "C) Australia", "D) Asia"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "How long does it take the earth to complete one revolution?",
            "choices": ["A) 30", "B) 360", "C) 365", "D) 180"],
            "answer": "C"
        }
    ]
    return questions

def shuffle_questions(questions):
    """Shuffle the Questions"""
    random.shuffle(questions)
    return questions