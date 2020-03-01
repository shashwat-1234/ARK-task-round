import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from matplotlib import cm 
from mpl_toolkits.mplot3d import axes3d
import pandas as pd 
import numpy as np 
from xlrd import open_workbook

fig = plt.figure()

ax1 = fig.add_subplot(111, projection = '3d')
book = open_workbook("radar_dump.xlsx")
sheet = book.sheet_by_index(0)
#import file 
#data_file = pd.read_excel('radar_dump.xlsx')


#print data_file 
    #prints entire file properly 

#read columns
for i in range(78, 135, 1):	
	
	xs = sheet.cell_value(i,0)
	ys = sheet.cell_value(i,1)
	zs = sheet.cell_value(i,2)
#x = 0.1
#y = 0.1
#z = 0.1
	ax1.scatter(xs, ys, zs, c = 'r', marker = 'o')
	#plt.plot(x,y,z)
plt.show()
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')



#print axes
    #prints axes as 

#dx = .5 * np.ones
#dy = dx.copy()
#dz = data.flatten()


#ax1.bar3d(X,Y,Z)

