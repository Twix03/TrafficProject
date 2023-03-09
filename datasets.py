import matplotlib
import matplotlib.pyplot as plt

import matplotlib.colors
from pandas import *
import sys
original = sys.stdout
colnames = ["A","B","C","D","E","F","G","H","I","J"]
ds = read_csv('L001_F001_trajectory.csv',names=colnames, header=None)
file_obj = open('textFile.txt', 'w')
dummyFile = open('writing.txt','w')
custom_map = matplotlib.colors.LinearSegmentedColormap.from_list("custom", ["#8c0001","#f31d01","#feb800","#90ff70","#0bddf5","#0141fe","#0000a0"])

def func(lst):

    ls = []
    initime = 7*3600
    
    for i in lst:
        a = str(i)
        hr = int(a[0:1])
        mm = int(a[1:3])
        ss = int(a[3:5])
        fff = int(a[5:])
        ls.append(hr*3600 + mm*60 + ss + fff*0.001 - initime)
    
    return ls  
  
def speed(lst):
    
    ls= []
    for i in range(0, len(lst)):
        temp = lst[i]/60
        if temp<=1:
            ls.append(temp)
        else:
            ls.append(1)
    return ls        


vehicle_id = ds['A'].tolist()
time = func(ds['B'].tolist())
print(time, file=file_obj)
vehicle_type = ds['C'].tolist()
vel = speed(ds['D'].tolist())
lane = ds['E'].tolist()
dist = ds['H'].tolist()
vehicle_len = ds['I'].tolist()
flag = ds['J'].tolist()
x1 = []
y1 = []
color1 = []
x2=[]
y2=[]
color2=[]
x3=[]
y3=[] 
x4=[]
y4= []
x5=[]
y5=[]
x_ticks = [0,300,600,900,1200,1500,1800,2100,2400,2700,3000,3300,3600]

for i in range (0, len(vehicle_id)):
    
    if lane[i]==1 and lane[i-1]==2:
        x4.append(time[i])
        y4.append(dist[i])
    if lane[i]==2 and lane[i-1]==1:
        x5.append(time[i])
        y5.append(dist[i])    
    elif lane[i]==1:
        x1.append(time[i])
        y1.append(dist[i])
        color1.append(vel[i])
    elif lane[i]==2:
        x2.append(time[i])
        y2.append(dist[i])
        color2.append(vel[i])
    if lane[i]==3 and lane[i+1]==1:
        x3.append(time[i])
        y3.append(dist[i])   
          
fig, axes = plt.subplots(2, 1,figsize=(20,8))

plt1 = axes[0].scatter(x1,y1,c=color1, cmap=custom_map,s=0.3)
axes[0].scatter(x3,y3,color="black",s=1.5)
axes[0].scatter(x4,y4,color="magenta",s=1.5)
plt2 = axes[1].scatter(x2,y2,c=color2,cmap=custom_map,s=0.3)
axes[1].scatter(x5,y5,color="magenta",s=1.5)


axes[0].set_xlabel("Time (seconds)")
axes[0].set_title("Driving lane")
axes[1].set_title("Passing lane")
axes[1].set_xlabel("Time (seconds)")
axes[0].set_ylabel("Kilopost (m)")
axes[0].set_ylabel("Kilopost (m)")

axes[0].set_ylim(5000,3000)
axes[1].set_ylim(5000,3000)
axes[0].set_xlim(0,3600)
axes[1].set_xlim(0,3600)

axes[0].set_xticks(ticks=x_ticks)
axes[1].set_xticks(ticks=x_ticks)

plt.colorbar(plt1,ax = axes[0])
plt.colorbar(plt2,ax = axes[1])

fig.tight_layout(pad=3.0)
plt.show()