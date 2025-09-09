# importing matplotlib library

import matplotlib.pyplot as plt

# importing numpy to get data from our plots

import numpy as np

x=np.linspace(0,10,100) # (0,10) 100-values
y=np.sin(x)
z=np.cos(x)
print(x)
print(y)
print(z)

# ploting the data


# sin wave

plt.plot(x,y)
plt.show()


# cos wave

plt.plot(x,z)
plt.show()

# adding title x-axis and y-axis

plt.plot(x,y)
plt.xlabel('label-for x-axis')
plt.ylabel('label for y-axis')
plt.title('title')
plt.show()


# parabola

x=np.linspace(-10,10,20)
y=x**2
plt.plot(x,y)
plt.show()



# ploting with dots

plt.plot(x,y,'r+') # red color with + symbol
plt.show()


# ploting with multiple graphs

x=np.linspace(-5,5,50)
plt.plot(x,np.sin(x),'g.')
plt.plot(x,np.cos(x),'r--')
plt.show()



# Bar-plot


fig=plt.figure() # empty figure

ax=fig.add_axes([0,0,1,1]) # (x-coordinate,y-coordinate,height,weigth)
languages=["english","French","spain","latin","german"]
people=[100,50,150,40,70]
ax.bar(languages,people)
plt.xlabel('Languages')
plt.ylabel('number of people')
plt.show()




# pie-chart


fig1=plt.figure()
ax=fig1.add_axes([0,0,1,1])
languages=["english","French","spain","latin","german"]
people=[100,50,150,40,70]
ax.pie(people,labels=languages,autopct='%1.1f') # %1.1 =one decimal point



# scatter plot


x=np.linspace(0,10,30)
y=np.sin(x)
z=np.cos(x)
fig2=plt.figure()
ax=fig2.add_axes([0,0,1,1])
ax.scatter(x,y,color='g')
ax.scatter(x,z,color='b')
plt.show()



# 3d Scatter plot


fig3=plt.figure()
ax=plt.axes(projection='3d')
z=20 * np.random.random(100)
x=np.sin(z)
y=np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')