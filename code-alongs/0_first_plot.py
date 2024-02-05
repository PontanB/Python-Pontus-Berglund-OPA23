import matplotlib.pyplot as plt

numbers = list(range(10))
sqares = [number**2 for number in numbers]
print (numbers)
print(sqares)

plt.plot(numbers, sqares)
plt.title("x^2 for positive integers 0-9")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
