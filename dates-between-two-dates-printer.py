# Import the timedelta and date classes from the datetime module
from datetime import timedelta, date

# Define a function named daterange which generates a range of dates between date1 and date2
def daterange(date1, date2):
    # Iterate over the range of days between date1 and date2
    for n in range(int((date2 - date1).days) + 1):
        # Yield each date within the range
        yield date1 + timedelta(n)

# Define the start date
start_dt = date(2015, 12, 20)
# Define the end date
end_dt = date(2016, 1, 11)

# Iterate over the range of dates generated by the daterange function
for dt in daterange(start_dt, end_dt):
    # Print each date in the format YYYY-MM-DD
    print(dt.strftime("%Y-%m-%d"))
