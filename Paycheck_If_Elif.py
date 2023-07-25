"""
This program returns paycheck amount with a
predetermined hourly rate and overtime rate.
"""

total_hours = int(input("enter a amount of hours: "))
hourly_rate = 20
overtime_rate = 30
paycheck = 0

if total_hours <= 40:
    paycheck = hourly_rate * total_hours
    print(paycheck)
elif total_hours > 40:
    difference = total_hours - 40
    hours_worked = (total_hours - difference) * hourly_rate
    overtime_worked = overtime_rate * difference
    paycheck = overtime_worked + hours_worked
    print(paycheck)
