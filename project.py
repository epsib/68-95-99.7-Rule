import csv
from numpy import PINF
import pandas as pd
import statistics

df=pd.read_csv("StudentsPerformance.csv")
math_data=df["math score"].to_list()
reading_data=df["reading score"].to_list()
writing_data=df["writing score"].to_list()


num=len(math_data)
data = []


for i in range(0, num):
    sum = int(math_data[i])+int(reading_data[i])+int(writing_data[i])
    data.append(sum)
print(data)

mean = statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
std=statistics.stdev(data)

fstdst, fstded, sstdst, sstded, tstdst, tstded = mean-std, mean+std, mean-2*std, mean+2*std, mean-3*std, mean+3*std

f = [i for i in data if i>fstdst and i < fstded]
s = [i for i in data if i>sstdst and i < sstded]
t = [i for i in data if i>tstdst and i < tstded]

pf = len(f)*100/len(data)
ps = len(s)*100/len(data)
pt = len(t)*100/len(data)

print(pf)
print(ps)
print(pt)