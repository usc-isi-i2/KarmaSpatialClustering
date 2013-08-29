/*******************************************************************************


 * Copyright 2013 University of Southern California
 * 


 * Licensed under the Apache License, Version 2.0 (the "License");


 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at


 * 
 * 	http://www.apache.org/licenses/LICENSE-2.0


 * 
 * Unless required by applicable law or agreed to in writing, software


 * distributed under the License is distributed on an "AS IS" BASIS,


 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and


 * limitations under the License.
 * 


 * This code was developed by the Information Integration Group as part 


 * of the Karma project at the Information Sciences Institute of the 
 * University of Southern California.  For more information, publications, 


 * and related projects, please see: http://www.isi.edu/integration


 ******************************************************************************/
from matplotlib.pyplot import *  
import random  
from collections import defaultdict
 
#function to calculate distance  
def dist(p1, p2):  
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)  
def dist2(p1, p2):
  return (abs(p1[3]-p2[3]))
 
all_points=[]
filedate = '2013-08-02'
f = open("GPSoutput" + filedate + ".txt")
contents = f.read()
lines = contents.splitlines()
nlines = len(lines) 
for i in range(nlines):
 line = lines[i]
 newline = line
 if line.count(',') >= 2:
   idx = newline.find(',')
   newline = newline[idx+1:]
   idx = newline.find(',')
   time = newline[:idx]
   newline = newline[idx+1:]

   idx = newline.find(',')
   if newline[:idx] != "latitude":
     time = int(time[11:13])
     temp = float(newline[:idx])
     # lat = int(round(temp,3)*10000)
     lat = temp

     newline = newline[idx+1:]
     idx = newline.find(',')
     temp = float(newline[:idx])
     # lng = int(round(temp,3)*10000)
     lng = temp
     label = 0
     coordinate = [lat, lng, label, time]
     all_points.append(coordinate)  
 
 
#take radius = 1 and min. points = 100  
E = 0.0005
minPts = 10
 
#find out the core points  
other_points =[]  
core_points=[]  
plotted_points=[]  
for point in all_points:  
 point.append(0) # assign initial level 0  
 total = 0  
 for otherPoint in all_points:  
   distance = dist(otherPoint,point)  
   if distance<=E:  
     total+=1  
 
 if total > minPts:  
   core_points.append(point)  
   plotted_points.append(point)
 else:  
   other_points.append(point)  
 
#find border points  
border_points=[]  
for core in core_points:  
 for other in other_points:  
   if dist(core,other)<=E:  
     border_points.append(other)  
     plotted_points.append(other)  

#implement the algorithm  
cluster_label=0  
 
for point in core_points:  
 if point[2]==0:  
   cluster_label+=1  
   point[2]=cluster_label  
 
 for point2 in plotted_points:  
   distance = dist(point2,point)  
   if point2[2] ==0 and distance<=E:  
     # print point, point2  
     point2[2] = point[2]  
 
 
#after the points are asssigned correnponding labels, we group them  
# cluster_list = defaultdict(lambda: [[],[]])  
# for point in plotted_points:  
#   cluster_list[point[2]][0].append(point[0])  
#   cluster_list[point[2]][1].append(point[1])  

cluster_list = []
for i in range(0,cluster_label):
  cluster = []
  cluster_list.append(cluster)
for point in plotted_points:
  cluster_list[point[2]-1].append(point)

########################################################################################################################################################################################################################
#take radius = 1 and min. points = 20  
E = 1
minPts = 10
Key = cluster_label
outputfile = open("cluster_time " + filedate + ".txt",'w+')
outputfile.write("latitude,longitude,timestamp\n")
for i in range(0,Key):
  cluster = cluster_list[i]
  all_points = cluster
  #find out the core points  
  other_points =[]  
  core_points=[]  
  plotted_points=[]  
  for point in all_points:
    point[2] = 0
    total = 0  
    for otherPoint in all_points:  
     distance = dist2(otherPoint,point)  
     if distance<=E:  
       total+=1  
    if total > minPts:  
     core_points.append(point)  
     plotted_points.append(point)  
    else:  
     other_points.append(point)  
  #find border points  
  border_points=[]  
  for core in core_points:  
   for other in other_points:  
     if dist2(core,other)<=E:  
       border_points.append(other)  
       plotted_points.append(other)  
  #implement the algorithm  
  cluster_label=0  
  for point in core_points:  
   if point[2]==0:
     cluster_label+=1
     point[2] = cluster_label  
   for point2 in plotted_points:  
     distance = dist2(point2,point)  
     if point2[2] ==0 and distance<=E:  
       # print point, point2
       point2[2] = point[2]
  timestamp = []
  num = len(core_points)
  for j in range(1,num):
    timestamp.append(core_points[j][3])
    timestamp = list(set(timestamp))
  timestring = str(timestamp[0])
  num = len(timestamp)
  for j in range(1,num):
    timestring = timestring + '-' + str(timestamp[j])
  string = str(float(core_points[0][0])) + ',' + str(float(core_points[0][1])) + ',' + timestring + '\n'
  print string
  outputfile.write(string)
