import matplotlib.pyplot as plt
import numpy as np

f = open("TRINITI.txt", "r")
y = list(map(int, f.read().split()))
x = [i for i in range(len(y))]
print(y)
f.close()

data = np.column_stack((x, y))

fig, ax = plt.subplots(figsize=(10, 2))

ax.scatter(x=x, y=y)
ax.set_title('Scatter: $x$ versus $y$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

plt.show()



