def greeting():
    print("========== LIFT TRACKER ==========")
    while True:
        routine = input("Input today's routine as either 'push', 'pull', or 'legs':\n")
        if routine.lower() != "push" and routine != "pull" and routine != "legs":
            print("Please type 'push', 'pull' or 'legs'.")
        else:
            break
    return routine.lower()

def initialize(routine: str):
    if routine == "legs":
        routine = "leg"
    print(f"Initializing data for {routine} day...")

def main():
    initialize(greeting())

main()
