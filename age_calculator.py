import datetime

#Date
year_now = datetime.datetime.now().year
month_now = datetime.datetime.now().month
day_now = datetime.datetime.now().day
#Time
hours_now = datetime.datetime.now().hour
minuts_now = datetime.datetime.now().minute
sec_now = datetime.datetime.now().second
while True:
    try:
        year = int(input("Enter your birthday (Year)[number]: "))
        month = int(input("Enter your birthday (Month)[number]: "))
        day = int(input("Enter your birthday (Day)[number]: "))
        break
    except Exception as es:
        print("Please enter only numbers ")
age_year = (year * 12) * 30
age_month = (13 - month) * 30
age_day = day
print(age_year,age_month,age_day)
year_now *= 30 * 12
month_now *= 30

sum_days = age_year + age_month + age_day
now_sum_days = year_now + day_now + month_now

total_days = now_sum_days - sum_days
print(total_days)

total_days = total_days / 360

months = total_days-int(total_days)
months *= 12

days = months* 30
print(f"Your age is : {int(total_days)} Years\nAnd {months} Months\nAnd {int(days)} Days")



print(f"Your total age is :{total_days}")
