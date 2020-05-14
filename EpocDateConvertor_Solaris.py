# First import date and time libraries for account expiration date analysis
import time
import datetime
#n 2. Input the data extraction date
print ('2. Input the data extraction date')
y_or_n = input("Was the material extracted today? (answer y or n)")
timestamp = time.time()
if y_or_n == 'y': # Alternative 1a: Simply confirm current date because user decided to use that as data extraction date
    print ("Calculate current date and time\n")
dt_object = datetime.datetime.fromtimestamp(timestamp)
print("dt_object =", dt_object)
if y_or_n == 'n': #1b Let user input data extraction date
    yyyy = int(input ("Input extraction year (yyyy): "))
    mm = int(input ("Input extraction month (mm): "))
    dd = int(input ("Input extraction day (dd): "))
    timestamp = datetime.datetime(yyyy, mm, dd, 0, 0).timestamp()
print ("timestamp =", timestamp)
days_since_1970 = timestamp / 3600 / 24
days_since_1970 -= days_since_1970 % 1
print ("days_since_1970 =", days_since_1970)