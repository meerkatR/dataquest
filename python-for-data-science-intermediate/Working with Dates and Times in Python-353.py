## 1. Introduction ##

from csv import reader
opened_file = open("potus_visitors_2015.csv")
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt
ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it
import datetime as dt
date_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    row[2] = dt.datetime.strptime(start_date, date_format)
    

## 6. Using Strftime to format dates ##

import datetime as dt
visitors_per_month = {}
for row in potus:
    appt_start_date = row[2]
    appt_start_date = appt_start_date.strftime("%B, %Y")
    if appt_start_date not in visitors_per_month:
        visitors_per_month[appt_start_date] = 1
    else:
        visitors_per_month[appt_start_date] += 1
        

## 7. The Time Class ##

import datetime as dt
appt_times = []
for row in potus:
    appt_start = row[2]
    appt_time = appt_start.time()
    appt_times.append(appt_time)

## 8. Comparing time objects ##

min_time = min(appt_times)
max_time = max(appt_times)

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days = 56)
answer_3 = dt_4 - dt.timedelta(seconds = 3600)

## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date

appt_lengths = {}
for row in potus:
    appt_start = row[2]
    appt_end = row[3]
    length = appt_end - appt_start
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1
        
min_length = min(appt_lengths)
max_length = max(appt_lengths)