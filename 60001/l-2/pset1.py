#Code for PSET 1

#Part A: House Hunting
# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))
# portion_down_payment = total_cost * 0.25

# current_savings = 0
# monthly_salary = annual_salary /12
# monthly_salary_saved = monthly_salary * portion_saved

# num_of_months = 0
# while not current_savings >= portion_down_payment:
#     r = (current_savings*0.04)/12
#     current_savings += r
#     current_savings += monthly_salary_saved
#     num_of_months += 1
#     #full gains in savings for the month reached

# print(f"Number of months:  {num_of_months}")


#Part B: Saving with a raise
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the  the semi­annual raise, as a decimal: "))
portion_down_payment = total_cost * 0.25

current_savings = 0
monthly_salary = annual_salary /12
monthly_salary_saved = monthly_salary * portion_saved

num_of_months = 0
while not current_savings >= portion_down_payment:
    r = (current_savings*0.04)/12
    current_savings += r
    current_savings += monthly_salary_saved
    check_if_raise = num_of_months % 6
    if (check_if_raise == 0 and num_of_months > 0):
        annual_salary = annual_salary*(1+semi_annual_raise)
        monthly_salary = (annual_salary)/12
        monthly_salary_saved = monthly_salary * portion_saved
    num_of_months += 1
    #full gains in savings for the month reached

print(f"Number of months:  {num_of_months}")


#Part C: Finding the right amount to save 
time = 36
semi_annual_raise = .07 
r = (current_savings*0.04)/12
down_payment = 0.25 * 1000000

salary = float(input("Enter that starting salary: "))

best_savings_rate = 0
steps = 0

#while we do not reach 36 months and we are not equal to greater than the down_payment 
#we must continue to iterate

#output best savings rate and steps in bisection search
print(f"Best savings rate: {best_savings_rate}")
print(f"Steps in bisection search: {steps}")