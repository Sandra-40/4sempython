import matplotlib.pyplot as plt
students=['Alice','Bob','Charlie','David']
marks=[85,90,78,92]
plt.bar(students,marks,color='skyblue')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Students marks visualization')
plt.show()