import matplotlib.pyplot as plt

weightTrackData = {}

def createArray(name):
    # Creates a new key for the dictionary to track weight data
    weightTrackData[name] = []

def inputWeight(name):
    # Inputs weight information for a given name
    while True:
        try:
            weight = float(input("Enter the weight in kg for {}: ".format(name)))
            if weight<0 or weight>500:
                print("The weight you entered is unacceptable. Pls enter again")
            else:
                weightTrackData[name].append(weight)
                break
        except ValueError:
            print("\nPlease enter a valid weight (numeric value)")

def inputNames():
    while True:
        # Takes the name of the person and checks for existing names
        name = input("Enter the name of the person: ").upper()
        if name in weightTrackData:
            print("\nName already exists. Please enter a different name.")
        else:
            createArray(name)
            return name

def displayOptions():
    print("\nPress 'A' to add another weight for the person")
    print("Enter 'R' to remove the last weight of the person")
    print("Enter 'N' to add weight for a new person")
    print("Enter 'Q' to quit and display the statistics")

def graph():
    # Plots weight data for all individuals
    for name, weights in weightTrackData.items():
        plt.plot(range(1, len(weights) + 1), weights, label=name, marker='x')

    plt.xlabel("Days")
    plt.ylabel("Weights (kg)")
    plt.legend()
    plt.title("Weight Tracker")
    plt.show()

def main():
    while True:
        name = inputNames()
        inputWeight(name)

        while True:
            displayOptions()
            choice = input("Enter your choice: ").upper()

            if choice == "A":
                inputWeight(name)
            elif choice == "R":
                if weightTrackData[name]:
                    weightTrackData[name].pop()
                    print("Last weight entry removed for", name)
                else:
                    print("No weight entries available for", name)
            elif choice == "N":
                break
            elif choice == "Q":
                graph()
                return
            else:
                print("\nPlease enter 'A', 'R', 'N', or 'Q' only")

if __name__ == "__main__":
    main()
