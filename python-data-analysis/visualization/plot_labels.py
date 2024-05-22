import numpy as np
import matplotlib.pyplot as plt

#you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis
#you can use the title() function to set a title for the plot
#use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels
#use the loc parameter in title() to position the title

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.plot(x, y)

plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.show()