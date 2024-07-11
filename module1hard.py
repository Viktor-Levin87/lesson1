grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
a = sorted(students_list)
b = sum(grades[0])/len(grades[0])
c = sum(grades[1])/len(grades[1])
d = sum(grades[2])/len(grades[2])
e = sum(grades[3])/len(grades[3])
f = sum(grades[4])/len(grades[4])
v = []
v.append(b)
v.append(c)
v.append(d)
v.append(e)
v.append(f)

dictionary = {}
for i in range(len(a)):
    dictionary[a[i]] = v[i]
print(dictionary)
