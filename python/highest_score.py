student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Option 1
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
    
print(f"The highest score in the class is: {highest_score}")

# Option 2
highest_score = max(student_scores)
print(f"The highest score in the class is: {highest_score}")

# Sum of all items in the list
# Option 1
total_score = sum(student_scores)
print(f"The total score in the class is: {total_score}")

# Option 2
total_score = 0
for score in student_scores:
    total_score += score
print(f"The total score in the class is: {total_score}")




