#Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import time
from array import *
import math
import os
import csv
import matplotlib.ticker as ticker
#Global Declarations
col = []
delimiters =""
cont = 0
insturment = "GDD - MPP-EM2S+"
#Parse Mag Sus Text File
#Option Two, graph for any table, Hard
#   Parse column headers into array
#   ask for which colums is required
#   each interval grab the data from matching columns
#   than plot graph.  Will work for more than mag sus

#   Add option to change colour based on values entered
#       enter 0 for no change
#
#
#Add start graph value

#Gather information for Hole and Data
hole = input("Enter the Hole ID: ")
#start = input("Enter Starting Depth: ")
#end = input("Enter Ending Depth: ")
gstart = input("Enter what depth you want the Graph to start: ")
initials = input("Enter your initials for the logger code: ")
multiple = input("Enter the number of readings per Meter, ie: every .25m is 4 per meter: ")
gstart = float(gstart)
multiple = int(multiple)
cwd = os.getcwd()
cwd = cwd + "\\Data\\"
arr = os.listdir(cwd)

#current hard coded max of 500 lines
# 0 = depth, 1 = relog, 2 = insturment, 3 = diamater, 4 = reading, 5 = comments, 6 = code, 7 = date
arra=[[" " for x in range(8)] for i in range(100000)]   
headings = ["mDepth   ", "Relog    ", "Insturment         ", "Diamater    ", "Reading       ", "Comments  ", "LoggerCode      " + "LogDate\n"]
#Gather Input
for file in arr:
    with open(cwd+file) as fp:
        for cont, line in enumerate(fp):
            if cont >1:
                cnt = cont-2
                parsed = line.split()
                for item in parsed:
                    #Handle question marks random size factor
                    if "?" in parsed:
                        parsed.remove("?")
                        arra[cnt][5]="?"
                        if "?" in parsed:
                            parsed.remove("?")
            
                
                arra[cnt][0] = parsed[3]
                arra[cnt][1] = "0"
                arra[cnt][2] = insturment
                arra[cnt][3] = parsed[5]
                arra[cnt][4] = parsed[8]
                arra[cnt][6] = initials
                arra[cnt][7] = parsed[1]
    fp.close()
#truestart = int(math.ceil(float(start)))
#graphstart = int(math.ceil(float(gstart))-1)
start = float(arra[0][0])
end = float(arra[cont-2][0])
print(int((float(end)*multiple))-int((float(gstart)*multiple))+1)

depths=[float(arra[cont-2][0]) for a in range(int((float(end)*multiple))-int((float(gstart)*multiple))+1)]
reads =[float(arra[cont-2][4]) for b in range(int((float(end)*multiple))-int((float(gstart)*multiple))+1)]



#Write new File
filename = hole + "_"+str(start)+"m-" + str(end) + "m.csv"
with open(filename,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['mDepth','Relog', 'Insturment', 'Diamater', 'Reading', 'Comments', 'LoggerCode', 'LogDate'])
    gst = 0
    for x in range(cnt+1):
        csvwriter.writerow([arra[x][0],arra[x][1], arra[x][2], arra[x][3], arra[x][4], arra[x][5], arra[x][6], arra[x][7]]) 
        if float(arra[x][0])>=float(gstart):
            depths[gst] = float(arra[x][0])
            reads[gst] = float(arra[x][4])
            gst = gst+1
            if float(arra[x][4])>10:
                col.append("y-")
            elif float(arra[x][4])>100:
                col.append("g-")
            else:
                col.append("b-")

csvfile.close()



    #Convert Text to Graph

#ig,axs= plt.subplots(4)
fig, ax = plt.subplots()


ax.set(xlabel='Depth(M)', ylabel='Reading',
       title=hole)

#sizea = float(cont-float(gstart)+float(start)-1)
#size = int(math.ceil(float(sizea/4)))
#print(size)
#print(sizea)

ax.set_ylim(0, 30)
ax.plot(depths, reads)
ax.grid()
tick_spacing = 5
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
#axs[0].plot(depths[0:size+1], reads[0:size+1], 'b-')
#axs[1].plot(depths[size:size*2], reads[size:size*2], 'b-')
#axs[2].plot(depths[size*2:size*3], reads[size*2:size*3], 'b-')
#axs[3].plot(depths[size*3:size*4], reads[size*3:size*4], 'b-')


#for i in range(size//2):
#    axs[0].annotate(str(reads[3*i]), xy=(depths[3*i],reads[3*i]), ha='center', va='bottom')
#for i in range(size//2):
#    axs[1].annotate(str(reads[size+2*i]), xy=(depths[size+2*i],reads[size+2*i]), ha='center', va='bottom')
#for i in range(size//2):
#    axs[2].annotate(str(reads[size*2+2*i]), xy=(size*2+depths[2*i],reads[size*2+2*i]), ha='center', va='bottom')
#for i in range(size//2):
#    axs[3].annotate(str(reads[size*3+2*i]), xy=(depths[size*3+2*i],reads[size*3+2*i]), ha='center', va='bottom')
plt.show()
time.sleep(3)