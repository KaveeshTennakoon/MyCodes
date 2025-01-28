weightTrackData = {}

def createArray(name):
    # makes a new key for the above define dictionary
    weightTrackData[name] = []

def inputWeight(name):
    #input weight inforamtion
    while True:
        try:
            weight = float(input("Enter your weigth in kg: "))
            weightTrackData[name].append(weight)
            break
        except ValueError:
            print("\nPlease enter a valid weight")

def inputNames():
    while True:
        # takes the name of the person
        name = input("Enter the name of the person: ").upper()
        if name in weightTrackData:
            print("\nName already exists")
        else:
            createArray(name)
            return name 
        
def graph():
    import matplotlib.pyplot as plt

    for name, weights in weightTrackData.items():
        plt.plot([day + 1 for day in range(len(weights))], weights, label=name, marker='x')
        
    plt.xlabel("Days")
    plt.ylabel("Weights")
    plt.legend()
    plt.title("Weight tracker")
    plt.show()

def main():
    # start the program by asking for the inputs of name and weight
    name = inputNames()
    inputWeight(name)
    while True:
        print("\nPress 'A' to add another weight to the person")
        print("Enter 'R' to remove the previous weight of the person")
        print("Enter 'N' to add weight of new person")
        print("Enter 'Q' to quit and display the statistics\n")
        choice = input("Enter your choice: ").upper()

        if choice == "A":
            #creates a new key in the dictionary
            inputWeight(name)
        elif choice == "R":
            # remove the last element in the array of the needed value
            try:
                weightTrackData[name].pop()
                
            except IndexError:
                print("\nNo weight input avaliable")
        elif choice == "N":
            # again runs the main program
            print()
            main()
            break
        elif choice == "Q":
            # ends the program
            break
        else:
            print("\nPlease enter either 'A', 'R', 'N' or 'Q' only")

if __name__ == "__main__":
    main()
    graph()