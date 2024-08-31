#BMI - Target weight
#August 31, 2024
#CSC121 m1Lab1 - Review
#Terrell Locks

#initating the while loop
run_again = True
while run_again != 'no':
#asking user to input their height and weight
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
#calculating math for bmi, and defining min and max bmi
    min_bmi= 18.5
    max_bmi = 24
    bmi = weight / height**2 * 703
    print('')
    print('Your BMI is', bmi)
    print('')
#create if/else statement to print whether the user is under, over, or within healthy bmi range    
    if bmi >0:
        if bmi <min_bmi:
            print("The number of pounds needed to gain in order to be at the bottom of the healthy range is:", min_bmi * height**2 /703 - weight)
        elif bmi >max_bmi:
            print('Weight to lose for healthy BMI is:', max_bmi * height**2 / 703 - weight)
        elif bmi > min_bmi and bmi < max_bmi:
            print('The user is within the healthy BMI range')
        else:
            print('ERROR: Weight must be positive')
#asking user to continue. program stops only if "no" is entered.
        run_again = input('Would you like to run the program again? (yes/no)')
        print('')





        
        


    
    

