import random


def random_int(min:int, max:int):
    """
    Gets a random integer between min and max.

    Args:
        min (int): minimum value while selecting the max value
        max (int): maximum value while selecting the max value

    Returns:
        int: a random integer between min and max value.
    """
    return random.randint(min, max)


def random_operation_selection():
    """
    returns: select & returns a randomly picked operation out of 3 possible choices: + - *
    """
    return random.choice(['+', '-', '*'])


def calculate(integer1:int, integer2:int, operation:str) -> (str,int):
    """Perform the operation between integer1 and integer2
    
    Args:
        integer1 (int): First integer number.
        integer2 (int): Second integer number.
        operation (str): Operation to be performed between the two numbers.

    Returns:
        problem (str): The whole operation 'n1 o n2 =' as a string.
        answer (int): The calculated value of the operation.    
    """
    problem = f"{integer1} {operation} {integer2}"

    # ADD
    if operation == '+': answer = integer1+integer2

    # SUBTRACT
    elif operation == '-': answer = integer1-integer2

    # MULTIPLY
    else: answer = integer1*integer2

    # Return the operation as a string and result as integer.
    return problem, answer

def math_quiz():
    """
    Starts a math quiz. A certain amount of questions will be asked. At each question a user answer will be taken. If the answer is correct then user gets +1 point otherwise 0.
    """
    correct_answer_counter = 0
    number_of_questions_to_ask = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_questions_to_ask):
        number1 = random_int(1, 10);
        number2 = random_int(1, 5);
        operation = random_operation_selection()

        PROBLEM, ANSWER = calculate(number1, number2, operation)

        print(f"\nQuestion: {PROBLEM}")
        user_answer = input("Your answer: ")

        # Try to convert the user_answer to int if only it is numeric.
        if str.isnumeric(user_answer):
            user_answer = int(user_answer)

        # Correct answer
        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            correct_answer_counter += -(-1)
        # Wrong answer
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {correct_answer_counter}/{number_of_questions_to_ask}")

if __name__ == "__main__":
    math_quiz()
