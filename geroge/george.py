slices_per_student = 3
students = 15
enrolled_students = students + 5
present_students = enrolled_students - 3
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order*8) % present_students
# Don’t forget to print them all
print(f"Boxes to order: {boxes_to_order}, Leftover slices: {leftover_slices}, Cost per student: {cost_per_student}")