# -*- coding: utf-8 -*-
"""ExploringLoss.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tinyMLx/colabs/blob/master/2-1-4-ExploringLoss.ipynb
"""

import math
# Edit these parameters to try different loss
# measurements. Rerun this cell when done
# Your Y will be calculated as Y=wX+b, so
# if w=3, and b=-1, then Y=3x-1

w = 2
b = -1

x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]
myY = []


for thisX in x:
  thisY = (w*thisX)+b
  myY.append(thisY)

print("Real Y is " + str(y))
print("My Y is   " + str(myY))

# let's calculate the loss
total_square_error = 0
for i in range(0, len(y)):
  square_error = (y[i] - myY[i]) ** 2
  total_square_error += square_error

print("My loss is: " + str(math.sqrt(total_square_error)))

