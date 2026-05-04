
def read_number():
    try:
        value = int(input("Enter a number: "))
        return value
    except ValueError:
        return None


#Put code in try if failure is possible and acceptable.
#Use except to define how the program should respond.