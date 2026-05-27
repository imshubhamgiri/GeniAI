marks = []

for i in range(6):
    mark = int(input("Enter a mark: "))
    marks.append(mark)

# sorted_marks = sorted(marks)
# print("Sorted marks:", sorted_marks)
marks.sort()
print("Sorted marks:", marks)