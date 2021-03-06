import datetime
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
holidays = ['11/23/16', '11/24/16', '11/25/16', '11/26/16', '12/24/16', '12/25/16', '12/26/16', '12/31/16', '01/02/17', '01/16/17', '02/20/17', '05/27/17', '05/29/17','07/01/17', '07/02/17', '07/03/17', '07/04/17', '09/02/17', '09/03/17', '09/04/17', '10/09/17', '11/23/17', '11/24/17', '11/25/17', '11/26/17', '12/23/17', '12/24/17', '12/25/17']

# turn list of holidays into list of datetime objects, parsedHolidays
parsedHolidays = []
for d in holidays:
    e = datetime.datetime.strptime(d, "%m/%d/%y")
    parsedHolidays.append(e)

# making it easier/cleaner to print datetime objects
def printDate(date):
    return date.strftime('%m/%d/%y')

# Get starting date
print("What is the starting date? (mm/dd/yy)")
print(">>> ", end='')

i = str(input())

# Convert input to datetime object
startDate = datetime.datetime.strptime(i, "%m/%d/%y")

# Print startDate
print("You entered: {:%m/%d/%Y}".format(startDate))

# Check which day of the week it starts on
startDay = startDate.weekday()
print("This class starts on " + daysOfWeek[startDay])

# Find out how many weeks to run
print("How many weeks is this class?")
print(">>> ", end='')

duration = int(input())

# THE LOOP!
n = duration * 2
c = 1

# set up a toggle between 2 and 5 a la http://stackoverflow.com/questions/8381735/toggle-a-value-in-python
A = 2
B = 5
total = A + B
nextInc = A

dates = []
dates.append(printDate(startDate))
print(str(c) + ": " + printDate(startDate))
# handle starting on a Wed/Thursday
if startDay == (2 or 3):
    nextInc = 5
# handle starting on a Saturday
elif startDay == 5:
    total = 14
    nextInc = 7
    n = duration

# trigger the main loop alternating between 2 and 5
nextDate = startDate
while c < n:
    nextDate = nextDate + datetime.timedelta(days=nextInc)
    if nextDate in parsedHolidays:
        print("HOLIDAY: " + printDate(nextDate))
        nextInc = total - nextInc
        continue
    dates.append(printDate(nextDate))
    c = c + 1
    print(str(c) + ": " + printDate(nextDate))
    nextInc = total - nextInc
