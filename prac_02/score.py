"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))

def determine_status(score):
    """Determine the status of a given score."""
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    if score >= 50:
        print("Passable")
    else:
        print("bad")

main()