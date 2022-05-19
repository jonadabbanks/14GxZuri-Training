#Write a Python calculator that can perform: addition, subtraction, division, multiplication and modulus operations. It should accept user input
#Written by Chigozie Emeribe
#defining Arithemetic Functions

def addition(no_1, no_2):
    return(no_1 + no_2)


def subtraction(no_1, no_2):
    return(no_1 - no_2)


def multiplication(no_1, no_2):
    return(no_1 * no_2)

    
def division(no_1, no_2):
    return(no_1 / no_2)


def modulus(no_1, no_2):
    return(no_1 % no_2)

#display arithematic functions available

print("Which Arithimetic Operation do you want to peform?")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("5 = Modulus")

while True:
# Users selects an option from below
        user_choice = input("Select Using [1-2-3-4-5] : ")

        if user_choice in ("1", "2", "3", "4", "5"):
             no_1 = int(input("Enter first number: "))
             no_2 = int(input("Enter second number: "))

             if user_choice == "1":
                 print(no_1, "+", no_2, "=", addition(no_1, no_2))

             elif user_choice =="2":
                print(no_1, "-", no_2, "=", subtraction(no_1, no_2))

             elif user_choice =="3":
                print(no_1, "*", no_2, "=", multiplication(no_1, no_2))

             elif user_choice =="4":
                 print(no_1, "/", no_2, "=", division(no_1, no_2))

             elif user_choice =="5":
                 print(no_1, "%", no_2, "=", modulus(no_1, no_2))

        # Ask user if they want to do another calculation
             another_calculation = input("do you want to do another calculation? = yes or no: ")
             if another_calculation =="no":
               print("Chigozie says Thank you!!")
               break

        else:
            print ("Incorrect Input")




    

