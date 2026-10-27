def main():
    """
    Prompts the user for mass in kilograms, calculates the equivalent 
    energy in Joules, and prints the result.
    """

    m = input("m: ")
    result = energy(m)

    print(result)  

def energy(mass):
    """
    Calculate the energy (in Joules) given a specific mass in kilograms.
    """

    c = 300000000 # meters per second
    c_2 = pow(c, 2)
    joules = int(mass)*c_2

    return joules

main()
