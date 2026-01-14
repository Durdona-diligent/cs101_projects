#The Missing assignment Checker
def absence_checker(students, assignments):
    students_set = set(i.lower() for i in students)
    assignments_set = set(i.lower() for i in assignments)
    not_submitted = students_set - assignments_set
    not_in_the_list = assignments_set - students_set
    not_submitted_list = list(not_submitted)
    not_in_the_list = list(not_in_the_list)
    not_submitted_list.sort()
    not_in_the_list.sort()
    return not_submitted_list, not_in_the_list

all_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
submitted = ["alice", "Bob", "Frank", "George"] # Note: 'alice' is lowercase, 'George' is new

list_1, list_2 = absence_checker(all_students, submitted)
print(f"Not submitted:")
[print(f"- {i.title()}") for i in list_1]
print(f"\n\nNot on class list:")
[print(f"- {i.title()}")for i in list_2]