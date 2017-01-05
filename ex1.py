import matplotlib.pyplot as plt 

x1 = range(0, 50)
y1 = [num**2 for num in x1]

x2 = [0, 1]
y2 = [0, 1]

fig = plt.figure(figsize = (8, 4))
ax = fig.add_subplot(111)
ax.plot(x1, y1, x2, y2)
fig.show()
fig.savefig("ex1.pdf")