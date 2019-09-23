import matplotlib as mpl
import matplotlib.pyplot as plt

min, max = (-40, 30)
step = 10

# Setting up a colormap that's a simple transtion
mymap = mpl.colors.LinearSegmentedColormap.from_list('mycolors',['blue','red'])

# Using contourf to provide my colorbar info, then clearing the figure
Z = [[0,0],[0,0]]

levels = range(min,max+step,step)
CS3 = plt.contourf(Z, levels, cmap=mymap)
plt.clf()

# Plotting what I actually want
X=[[1,2],[1,2],[1,2],[1,2]]
Y=[[1,2],[1,3],[1,4],[1,5]]
Z=[-40,-20,0,30]
for x,y,z in zip(X,Y,Z):
    # setting rgb color based on z normalized to my range
    r = (float(z)-min)/(max-min)
    g = 0
    b = 1-r
    plt.plot(x,y,color=(r,g,b))
plt.colorbar(CS3) # using the colorbar info I got from contourf
plt.show()
