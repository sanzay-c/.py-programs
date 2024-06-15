file_path = r"D:\python_programmes\python_programs\programs\pthon_class_qna\file_handling\txt_files\input.txt"
output_file_path = r"D:\python_programmes\python_programs\programs\pthon_class_qna\file_handling\txt_files\output.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

    student_score = {}

    for line in lines:
        data = line.strip().split()
        name = data[0]
        scores = []
        for score in data[1:]:
            scores.append(int(score))
            total_score = sum(scores)
            num_score = len(scores)
            avg_score = total_score / num_score
            student_score[name] = avg_score


# Write student names and average scores to output file
with open(output_file_path, 'w') as file:
    for name, avg_score in student_score.items():
        file.write(f"{name} {avg_score:.2f}\n")

# Find student with highest average score
highest_avg_score = 0
top_student = ""
for name, avg_score in student_score.items():
    if avg_score > highest_avg_score:
        highest_avg_score = avg_score
        top_student = name

# Print student with highest average score
print(f"Student with the highest average score: {top_student} with {highest_avg_score:.2f}")