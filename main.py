def greeting():
    print("========== LIFT TRACKER ==========")
    return input("Push, pull, or leg day?\n")

def initialize(routine):
    print(f"Initializing data for {routine} day...")

def main():
    initialize(greeting())

main()
