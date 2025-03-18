# names = ["Алиса", "Борис", "Виктор", "Галина"]
# grades = [85, 90, 78, 92]
#
# info = {}
# 
# for name in names:
#     info[name] = grades[names.index(name)]
#
# print(info)

names = ["Алиса", "Борис", "Виктор", "Галина"]
grades = [85, 90, 78, 92]

info = {}

for name in names:
    index = names.index(name)
    student_score = grades[index]
    info[name] = student_score

print(info)
