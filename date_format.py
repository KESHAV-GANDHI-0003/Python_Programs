#Program to convert date in proper format
date_input = input("Enter date as date in MMDDYYYY format :-")
months = ["January","Feburary", "March","April","May", "June","July","August","September", "October","November","December"]
month = int(date_input[0:2])
month -= 1
days=date_input[2:4]
year = date_input[4:8]
print(f"{months[month]} {days}, {year}")