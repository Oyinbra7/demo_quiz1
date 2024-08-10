def ask_question(question):
    """ format question"""
    print(f"Question: {question['question']}")
    for choice in question['choices']:
        print(choice)
    answer = input("Your answer: ").strip().upper()
    if answer == question['answer']:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {question['answer']}\n")
        return False
    
def calculate_result(score, pass_mark= 3):
    """Calculate if the user passes or fails based on the score."""
    return "Pass" if score >= pass_mark else "Fail"