def main():
    """
    Prompts the user for the meal cost and tip percentage, 
    calculates the tip amount, and prints the result.
    """
    
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Removes the '$' from the input string and returns the amount as a float.
    """

    dollar  = float(d.replace("$", ""))

    return dollar


def percent_to_float(p):
    """
    Removes the '%' from the input string, converts to float, 
    and divides by 100 to return the decimal value.
    """
    
    percent = float(p.replace("%", ""))
    percent = percent/100

    return percent

main()