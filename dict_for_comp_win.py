# Program to to create a dict for competition winners
competition_winners = {}
no_of_students = int(input("Enter the no. of students :- "))
for i in range(no_of_students):
    student_name = input("Enter the name of student :- ")
    student_no_of_wins = input("Enter no of competitions won by student :- ")
    competition_winners[student_name] = student_no_of_wins
print("The Conpetition Winners :- ")
for keys in competition_winners:
    print(keys, ":", competition_winners[keys])