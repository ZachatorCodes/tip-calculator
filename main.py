#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Zach's tip calculator!")

# Input Constants
total_bill = float(input("What was the total bill? ($)\n"))
tip_percent = float(input("What percent would you like to tip?\n")) / 100
people_paying = int(input("How many people are splitting the bill?\n"))

bill_and_tip = total_bill * (1 + tip_percent)
bill_per_person = round(bill_and_tip / people_paying, 2)

print(f"Each person should pay ${bill_per_person}")