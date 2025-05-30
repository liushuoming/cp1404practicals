"""
function get_valid_score()
    input score
    while score not in 0–100
        show error
        input score
    return score

function determine_result(score)
    if score ≥ 90: return "Excellent"
    else if score ≥ 50: return "Passable"
    else: return "Bad"

function show_stars(score)
    print "*" repeated score times

function print_menu()
    display options G, P, S, Q

function main()
    score = get_valid_score()
    repeat
        print_menu()
        input choice
        if choice == G: score = get_valid_score()
        else if choice == P: print determine_result(score)
        else if choice == S: show_stars(score)
        else if choice == Q: print farewell
        else: print invalid input
    until choice == Q

 main()

"""
def main():
    """Main program to run the menu loop and handle user input."""
    score = get_valid_score()

    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print("Result:", result)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye! Thanks for using the program.")
        else:
            print("Invalid option. Please choose again.")


def print_menu():
    """Display the main menu."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Prompt user until a valid score between 0 and 100 is entered."""
    score = int(input("Enter a score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = int(input("Enter a score (0-100): "))
    return score


def determine_result(score):
    """Determine grade/result based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many stars as the score value."""
    print("*" * score)


# Call the main function to start the program
main()

