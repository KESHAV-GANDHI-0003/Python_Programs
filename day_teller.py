#Program that takes the no of day and print th day
dayNames = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

dayNum = int(input("Enter day number: "))
firstDay = input("First day of year: ")

if dayNum < 2 or dayNum > 365:
    print("Invalid Input")
else:
    startDayIdx = dayNames.index(str.upper(firstDay))
    currDayIdx = dayNum % 7 + startDayIdx - 1

    if currDayIdx >= 7:
        currDayIdx = currDayIdx - 7

    print("Day on day number", dayNum, ":", dayNames[currDayIdx])