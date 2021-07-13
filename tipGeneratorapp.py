# This program calculate tips 
# @author Macuei Mathiang 
# @date 07/13/2021
# @Verson - 1.1

# Display a greeting message
print('Welcome to the tip calculator app.')

#Ask the user to enter the total bill as double/float
total_bill = float(input('What was the total amount ? $'))

#Ask the user to enter the percentage of the tip to give
selected_tip_percentage = int(input('What percentage tip would like to give? 10, 12, 15: '))

#Ask the user to enter the number of the people
number_of_people = int(input('How many people to split the bill? '))

#Compute tips, and final payment amount per person
tip_total = float((selected_tip_percentage/100) * total_bill)

# Calculate sub total cost including tip
subtotal = (total_bill + tip_total)

#Calculate  the amount to be pay by each person
pay_per_person = (subtotal/number_of_people)

# use round() function to print only two decimal places
pay_per_person2 = round(pay_per_person, 2)

# Display pay per person to the user
print(f"Each person will pay:  $ {pay_per_person2}")