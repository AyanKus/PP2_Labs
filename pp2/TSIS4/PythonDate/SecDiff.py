import datetime

firstDate = datetime.datetime(2022, 5, 13)
secondDate = datetime.datetime(2077, 5, 13)
diff = secondDate - firstDate
diffInSec = diff.total_seconds()
print("The difference between the two dates is", diffInSec, "seconds.")
