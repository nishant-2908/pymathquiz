import random
import sys


def take_input_as_numeric(
    message: str = "Enter the number",
    error_message: str = "Please enter a valid number",
    negative_allowed: bool = False,
    decimal_allowed: bool = False,
    zero: bool = False,
) -> float | int:
    """
    Takes input from the user as integer
    Parameters:
    message (str) - The message to be displayed to the user
    error_message (str) - The error message to be displayed to the user
    negative_allowed (bool) - Whether negative numbers are allowed or not
    Returns:
    int - The integer entered by the user
    """

    # Running a while Loop
    while True:

        # Getting the input from the user while displaying the message
        userinput = input(message)

        # Try-except block
        try:

            # Try to convert to decimal
            decimal_value = float(userinput)

            # If zero is allowed and the decimal value is zero itself
            if zero and decimal_value == 0:
                # Return the decimal of the userinput
                return decimal_value

            # If the negative allowed is allowed
            if negative_allowed:

                # If the decimal is allowed
                if decimal_allowed:

                    # Return the decimal value
                    return decimal_value

                # If decimal value is not allowed
                else:

                    # If the decimal value is an integer
                    if decimal_value == int(decimal_value):

                        # Return the integer of the decimal value
                        return int(decimal_value)

                    # If the decimal value is not an integer
                    else:

                        # Print the error message
                        print(error_message)

            # If the negative allowed is not allowed
            else:

                # If decimal is allowed
                if decimal_allowed:

                    # Return the decimal value
                    return decimal_value

                # If decimal is not allowed
                else:

                    # If the decimal value is an integer
                    if decimal_value == int(decimal_value):

                        # Return an integral value of the decimal
                        return int(decimal_value)

                    # If decimal value is not an integer
                    else:

                        # Print an error message
                        print(error_message)

        # If the operation faces ValueError
        except ValueError:

            # Print the error message
            print(error_message)


def input_in_options(
    message: str,
    options: list,
    error_message: str = "Invalid option",
):
    """
    Asks for the input from a given option
    If the userinput is not in the given options, it asks for the input again
    """

    # Running a while loop
    while True:

        # Getting the input from the user
        userinput = input(message)

        # If the lower case of the userinput is not in the list generated by lowercasing all the options of the given
        # list
        if userinput.lower().strip() in [str(option).lower() for option in options]:

            # Return the userinput
            return userinput

        # Else
        else:

            # Print the error message
            print(error_message)


def generate_random_question(
    question_number: int, operations: list, upper_limit: int, lower_limit: int = 1
):

    # Getting a random operation
    random_operation = random.choice(operations)

    # Getting two random numbers
    number1 = random.randint(lower_limit, upper_limit)
    number2 = random.randint(lower_limit, upper_limit)

    # Generating the answers
    answer = (
        number1 + number2
        if random_operation == "Addition"
        else (
            number1 - number2
            if random_operation == "Subtraction"
            else (
                number1 * number2
                if random_operation == "Multiplication"
                else (number1 // number2)
            )
        )
    )

    if random_operation == "Addition":
        return f"Question {question_number}. {number1} + {number2}", answer
    elif random_operation == "Subtraction":
        return f"Question {question_number}. {number1} - {number2}", answer
    elif random_operation == "Multiplication":
        return f"Question {question_number}. {number1} × {number2}", answer
    elif random_operation == "Division":
        return (
            f"Question {question_number}. {number1} ÷ {number2} (Only Quotient)",
            answer,
        )


def main():

    # Defining the supported operations
    operations = ["Addition", "Subtraction", "Multiplication", "Division", "Remainder"]

    # Printing and welcoming the user
    print("Welcome to PyMathQuiz !\n")

    # Taking the marking scheme
    for_positive = take_input_as_numeric(
        "Enter the number of marks to be awarded for correct: ",
        "Invalid number of marks",
        decimal_allowed=True,
    )

    for_negative = take_input_as_numeric(
        "Enter the number of marks to be deducted for incorrect: ",
        "Invalid number of marks",
        decimal_allowed=True,
        negative_allowed=True,
    )

    # Getting the mode
    mode = input_in_options(
        "Enter the mode (Easy [E] / Medium [M] / Difficult [D]: ", ["E", "M", "D"]
    )

    upper_limit = 0
    lower_limit = 0

    # Defining the limits based on the mode
    if mode.upper() == "E":
        lower_limit = 1
        upper_limit = 15
    elif mode.upper() == "M":
        lower_limit = 1
        upper_limit = 25
    elif mode.upper() == "D":
        lower_limit = 1
        upper_limit = 35

    # Taking input from the users for the number of questions
    no_of_questions = take_input_as_numeric(
        "Enter the number of questions to be asked: ", "Invalid number of questions"
    )

    # Defining counts for each type of questions
    counts = {
        "Incorrect Questions": 0,
        "Correct Questions": 0,
    }

    # For running the questions
    for i in range(1, no_of_questions + 1):

        # Getting the question and the answer for the question number
        q_a = generate_random_question(
            question_number=i,
            operations=operations,
            upper_limit=upper_limit,
            lower_limit=lower_limit,
        )

        # Printing the question
        print(
            f"\n{q_a[0]}",
        )

        # Taking the input from the user for the answer
        user_answer = take_input_as_numeric(
            "Answer: ",
            "Invalid answer",
            negative_allowed=True,
            decimal_allowed=True,
            zero=True,
        )

        # Checking if the answer is correct
        if user_answer == q_a[1]:
            counts["Correct Questions"] += 1
            print("Correct!")

        # If the answer is not correct
        else:
            counts["Incorrect Questions"] += 1
            print(
                "Incorrect Answer",
            )
            print(f"Correct Answer: {q_a[1]}")

    # Printing the results
    print("Correct Questions: {}".format(counts["Correct Questions"]))
    if counts["Incorrect Questions"] > 0:
        print(
            "Incorrect Questions: {}".format(counts["Incorrect Questions"]),
        )
    print(
        "Total Marks for Correct Questions: {}".format(
            counts["Correct Questions"] * for_positive
        ),
    )
    if counts["Incorrect Questions"] > 0:
        print(
            "Deducted Marks for Incorrect Questions: {}".format(
                counts["Incorrect Questions"] * for_negative
            ),
        )
    print(
        "\nTotal Marks {}".format(
            counts["Correct Questions"] * for_positive
            - counts["Incorrect Questions"] * for_negative
        ),
    )


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nYou chose to interrupt the program")
        sys.exit(1)
