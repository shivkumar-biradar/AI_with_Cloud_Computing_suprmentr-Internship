import matplotlib.pyplot as plt

values = [10, 20, 30]
labels = ["A","B","C"]

plt.bar(labels, values)
plt.title("Bar Chart")
plt.show()

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.show()

plt.hist(values)
plt.show()
