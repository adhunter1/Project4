#Author: Alexandra Hunter
#Assignment: Project 4
#Completed (or last revision):  11/6/2018
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
def createGraph1(listyList):
    y=listyList
    x=["1840","1860","1880","1900","1920","1940","1960","1980","2000","2020"]
    
    y_pos = np.arange(len(listyList))
    plt.ylabel('Temperature Anomaly (Celsius)')
    plt.xlabel('year')
    plt.show()
    
def createGraph2(listyList):
    y=listyList
    x=[1840,1860,1880,1900,1920,1940,1960,1980,2000,2020]
    
    y_pos = np.arange(len(listyList))
    plt.ylabel('Temperature Anomaly (Celsius)')
    plt.xlabel('year')
    plt.plot(x,y, color='b')
    plt.show()

    
        
def main():
    L=[]
    try:#catching error
        inf = open("ocean_temp_with_exceptions.csv", "r") #open the file
        for line in inf :#read data into a list
            
            try:
                hold=float(line)
                L.append(hold)#puts data into list
                
                
            except ValueError as hold:
                print("not a floating point")
        inf.close() #close the file
    except FileNotFoundError:#if file is not found
        print("Cannot find the file")
    outf = open("p4out.txt", "w") #open new file
    #createGraph(L)
    #createGraph2(L)
    for line in L:
        line=line*100#mult by 100

        outf.write(str(line))
        outf.write("\n")

    
    outf.close()
        
    
main()
