#!/usr/bin/env python3

import math

# 各年の資産増加出力をひとまとめにする
def a_print( year, start_value, end_value):
    r_begin = round(start_value)
    r_end = round(end_value)
    print("%4d" % (year),"{:>11,}".format(r_begin),"{:>11,}".format(r_end), end="")

# Annual amount of investment in USD
annual_investment = 4000

# Feb 12, 2016 VOO was $171.14, Sep 21, 2018, VOO was $269.56. The valuention went up by 1.57508472595536 in 952 days. That's 1.1904 per year. 
compound_interest = 1.1904

# daily interest
daily_interest = compound_interest**(1/365.25)

# Set investment target to USD 2.5MM 
target = 2500000

print("year       start         end  [triple] start         end")

year = 1
y_begin = annual_investment
y_end = y_begin * compound_interest

# adding triple investment

t_begin = annual_investment * 3
t_end = t_begin * compound_interest

t_reached_goal = 0

while y_end < target:
    a_print(year, y_begin, y_end)
    print("", end="")
    if (t_end < target):
        a_print(year, t_begin, t_end)
        t_begin = t_end + (annual_investment * 3)
        t_end = t_begin * compound_interest
        
    elif(t_reached_goal == 0 and t_end >= target ):
        a_print(year, t_begin, t_end)
        t_reached_goal = 1
        t_years = year - 1
        t_days = math.log(target / t_begin)/math.log(daily_interest)
        
    print("")
    y_begin = y_end + annual_investment
    y_end = y_begin * compound_interest

    year += 1

a_print(year, y_begin, y_end)
print("")

days = math.log(target / y_begin)/math.log(daily_interest)


print("")
print("For USD 4,000 annual investment, it would take ", (year-1), "years ", round(days), "days", ": That's ", round((year-1)*365.25 + days), "days" )
print("For USD 12,000 annual investment, it would take ", (t_years-1), "years ", round(t_days), "days", ": That's ", round((t_years-1)*365.25 + t_days), "days" )

shortened_percentage = ((((year-1)*365.25 + days) - ((t_years-1)*365.25 + t_days))) / ((year-1)*365.25 + days)*100

print("")
print("By tripling the annual investment, it shortened the period by %.1f %%" % shortened_percentage  )