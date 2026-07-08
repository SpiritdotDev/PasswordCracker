from BruteForce import BruteForce

#Main file for the program, should take in user input for the password and cracking method
#and from there send the work to the correct algorithm function.

#List of methods that can be used, can by added to as needed to allow for more algorithms.
methods = ["Brute Force", "Dictionary", "Rainbow Table"]

def main():

    Password = input("Welcome to the password cracker, please enter the password you want to simulate cracking. ")
    print(Password)
    counter = 1
    for method in methods:
        print(f"{counter}: {method}")
        counter += 1
    Method = int(input("Please select the method you would like to simulate by entering the number of the method from the list above:"))

    match Method:
        case 1:
            BruteForce(Password)
        case 2:
            return
        case 3:
            return
        case _:
            raise Exception("Not a valid method selection.")
    

    return

if __name__ == "__main__":
    main()