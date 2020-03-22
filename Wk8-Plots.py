# Fiona Lee
# Plot the functions x, x squared and x cubed in the range 0 to 4 on the one set of axes

import numpy as np
import matplotlib.pyplot as plt
#x = np.arange (0.0,4.1,0.2)
#Create and array between 1 and 4 in intervals of 0.2
x = np.linspace(0,4,20)
#Alternative code to create an array between 1 and 4 in 20 even parts
xsquared = x ** 2
xcubed = x ** 3
plt.plot (x , xsquared ,' g.', label = 'x squared')
#Plot x relative to x squared in green dots named 'x squared'
plt.plot (x , xcubed ,' r.', label = 'x cubed')
#Plot x relative to x cubed in red dots named 'x cubed'
plt.legend()
#Create a legend for the labels
plt.title('Plot the Values 1 to 4 Squared and Cubed')
#Create a title for the plot
plt.xlabel("Value of 'x'")
plt.ylabel("Value of 'x squared' and 'x cubed'")
#Create Labels for the x & y axis
plt.show()
#Create the plot
