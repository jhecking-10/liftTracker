def greeting():
    print("========== LIFT TRACKER ==========")
    while True:
        routine = input("Input today's routine as either push, pull, or legs:\n")
        if routine != "push" and routine != "pull" and routine != "legs":
            print("Please type push, pull or legs.")
        else:
            break
    return routine

def initialize(routine):
    print(f"Initializing data for {routine} day...")

def main():
    initialize(greeting())

main()
