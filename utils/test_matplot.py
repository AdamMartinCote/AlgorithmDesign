import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure(figsize=(10,10))
fig.suptitle('Test',fontsize=16)
ax = fig.add_subplot(111,frameon=True, autoscale_on=True)
ax.set_aspect('equal')
ax.grid(visible=True)
ax.plot(range(10),range(10),'-k',lw=2)
plt.show()

