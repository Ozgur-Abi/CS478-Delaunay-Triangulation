# Import the required libraries
from tkinter import *
from tkinter import ttk
import numpy as np
from delaunayRandomIncremental import DelaunayRI
from delaunayDivideAndConquer import delaunayDC
import matplotlib.pyplot as plt
import matplotlib.tri
import matplotlib.collections

    

#Remove the point selected by user
def removePoint():
   for item in pointlb.curselection():
      pointlb.delete(item)
      global points
      points = np.delete(points, item, 0)
      
#Plot Delaunay Triangulation with Divide And Conquer Algorithm
def tridd():
    global radius
    #Create triangulation
    edges = delaunayDC(points)
    fig, ax = plt.subplots()
    ax.margins(0.1)
    ax.set_aspect('equal')
    plt.axis([-1, radius+1, -1, radius+1])
    for e in edges:
        ax.plot([e.org[0], e.dest[0]], [e.org[1], e.dest[1]], 'bo--')
        #print(str("EdgeX: " + str(e.org[0])) + "   " + str(e.dest[0]))
        #print(str("EdgeY: " + str(e.org[1])) + "   " + str(e.dest[1]))
        #print("------")
    plt.title("Delaunay Triangulation with Divide And Conquer Algorithm")
    plt.show()
    #print(edges)
    
#Plot Delaunay Triangulation with Randomized Incremental Algorithm 
def triri():
    global radius
    #Create triangulation
    dt = DelaunayRI()
    for p in points:
        #print(p)
        dt.addPoint(p)
        
    #Plot triangulation
    fig, ax = plt.subplots()
    ax.margins(0.1)
    ax.set_aspect('equal')
    plt.axis([-1, radius+1, -1, radius+1])

    cx, cy = zip(*points)
    dt_tris = dt.exportTriangles()
    ax.triplot(matplotlib.tri.Triangulation(cx, cy, dt_tris), 'bo--')
    plt.title("Delaunay Triangulation with Randomized Incremental Algorithm")
    plt.show()


#Create the GUI
win=Tk()
win.title("Delaunay Triangulator")

win.geometry("700x550")

win.rowconfigure(0, weight=8)
win.rowconfigure(1, weight=1)
win.rowconfigure(2, weight=1)
win.rowconfigure(3, weight=2)
win.rowconfigure(4, weight=2)
win.rowconfigure(5, weight=2)
win.rowconfigure(6, weight=2)
win.rowconfigure(7, weight=1)
win.rowconfigure(8, weight=1)
win.rowconfigure(9, weight=2)

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=8)

#Create listbox which shows the points to the user
pointlb=Listbox(win)
pointlb.grid(column=0, row=0, columnspan = 2, padx=5, pady=5, sticky=N+S+E+W)

#Inputs for the user to specify X and Y coordinate of points
ttk.Label(win, text="X coordinate: ").grid(column=0, row=1, sticky=W, padx=0, pady=2)
xe = ttk.Entry(win)
xe.grid(column=1, row=1, sticky=W, padx=0, pady=5)
ttk.Label(win, text="Y coordinate: ").grid(column=0, row=2, sticky=W, padx=0, pady=2)
ye = ttk.Entry(win)
ye.grid(column=1, row=2, sticky=W, padx=0, pady=5)

#Add point to current point list based on user input
def addPoint():
    global points
    x = xe.get()
    y = ye.get()
    pointlb.insert(pointlb.size(), "x: " + str(x) + " y: " + str(y))
    
    points = np.append(points, np.array([[float(x), float(y)]]), axis = 0)

#Generate specified number of points that are in the specified radius
def genPoints():
    global points
    num = ne.get()
    rad = re.get()
    
    global radius
    global pointNum
    
    radius = int(rad)
    pointNum = int(num)
    points = radius * np.random.random((pointNum, 2))
    pointlb.delete(0, END)
    
    for p in points:
        pointlb.insert(pointlb.size(), ("x: " + str(p[0]) + " y: " + str(p[1])))

#Add/Delete Point and Plot Triangulation Buttons
ttk.Button(win, text="Add Point", command=addPoint).grid(column=0, row=3, sticky=W, padx=5, pady=3)
ttk.Button(win, text="Delete Selected Point", command=removePoint).grid(column=0, row=4, sticky=W, padx=2, pady=3)
ttk.Button(win, text="Triangulate Using Divide&Conquer", command=tridd).grid(column=0, row=5, sticky=W, padx=5, pady=3)
ttk.Button(win, text="Triangulate Using Randomized Incremental", command=triri).grid(column=0, row=6, sticky=W, padx=5, pady=3)

#Inputs for the user to enter number of points and point radius
ttk.Label(win, text="Number of points: ").grid(column=0, row=8, sticky=W, padx=0, pady=2)
ne = ttk.Entry(win)
ne.grid(column=1, row=8, sticky=W, padx=0, pady=5)
ttk.Label(win, text="Point radius: ").grid(column=0, row=9, sticky=W, padx=0, pady=2)
re = ttk.Entry(win)
re.grid(column=1, row=9, sticky=W, padx=0, pady=5)

#Generate point button
ttk.Button(win, text="Generate Random Points", command=genPoints).grid(column=0, row=7, sticky=W, padx=5, pady=3)

#Create the initial point set and insert them to GUI's point list
radius = 100
pointNum = 12

ne.insert(0, pointNum)
re.insert(0, radius)

points = radius * np.random.random((pointNum, 2))

for p in points:
    pointlb.insert(pointlb.size(), ("x: " + str(p[0]) + " y: " + str(p[1])))


win.mainloop()