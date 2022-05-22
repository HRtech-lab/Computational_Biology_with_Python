#!/usr/bin/env python
# coding: utf-8




#Importing useful libraries
import pandas as pd
import numpy as np
import pysam
import allel
import re
import networkx as nx
import copy





#Using Pysam to read aligment file e.g BAM file
samfile = pysam.AlignmentFile('alphonso_sorted.bam',"rb")





# Extracting reads from the samfile , read by read without
for read in samfile.fetch():
    print(read)
    break





#Fetechin reads from a specific region now
for read in samfile.fetch("CM021837.1",5500,5505): #contig ID, start, end
    print(read)





print(read.aend)
print(read.cigarstring)
print(read.query_length)
print(read.get_reference_sequence())
print(read.seq) #deprecated though
print(read.pos,read.mapq )
print(read.is_proper_pair)
# print(read.get_aligned_pairs())
print(read.reference_name)





#Mapping positions to their respective index in Pysam of each read
for point in zip(read.positions, read.seq):
    print(point,end=" ")





#Extracting soft clips only
for read in samfile.fetch():
        if read.cigarstring is not None and "S" in read.cigarstring:
            print(read.cigarstring)
            break




#Checking the statistics of the BAM file
for read in samfile.get_index_statistics() :
    print(read)




#insert size final Code
import pysam
# n is my number for which I have to compare my insert size with
n = int(input("Please Enter the number you want the minimum insert size greater than = "))
# Initially I have set the counter to zero  and with each iteration one will be added if the condition is true
counter = 0
for read in samfile.fetch():
#Very useful function file.fetch, it helps in iterating over the entire sam/bam file easily
    if read.isize >= n:
        counter = counter+1 
print("Our insert size is greater than or equal to n is = ",counter)





#Function for the above situation \
def insert_size(n):
    j = 0
    for read in samfile.fetch():
        if read.isize >= n:
            j=+1
    return j
    print(j)
#Calling the funtion
insert_size(200)


# # SAMTOOL In PYSAM and writing a SAMFILE




#PYSAM COMMANDS VS SAMTOOLS COMMANDS
# pysam.sort("-o", "output.bam", "ex1.bam")
# corresponds to the command line:
# samtools sort -o output.bam ex1.bam




#Function for making a BAM file for our test data
# import pysam
# samfile = pysam.AlignmentFile("alphonso_sorted.bam","rb")
# header = samfile.header
# with pysam.AlignmentFile("multiple.bam", "wb", header=header) as outf:
# # Now you can give gtf information in samfile.fetch()
#     for read in samfile.fetch("CM021838.1"):
#         outf.write(read)





#Getting read names only
h = []
j = 0
for read in samfile.get_index_statistics() :
    j = j+1
    a = read[0]
    h.append(a)
# print(j)
print(len(h))











import pandas as pd
import numpy as np
import pysam
import allel





#Now mapping my reads with DNA_seq and its positions, without worrying about the cigar
j = 0
for read in samfile.fetch():
    j = j+1
    print(j,read)
    if j == 62:
        result = dict(zip(read.positions,read.seq))
        print(result)
    if j >62:
        break





counts = {"A":0,"T":0,"C":0,"G":0}
for read in samfile.fetch():
    for i in read.seq.rstrip():
        counts[str.upper(i)] += 1
    break
print(counts)




g =0
c = 0
a = 0
t = 0
for read in samfile.fetch():
    G = str.upper(read.seq).count("G")
    A = str.upper(read.seq).count("A")
    C = str.upper(read.seq).count("C")
    T = str.upper(read.seq).count("T")
    g = g+G
    c = c+C
    a = a+A
    t = t+T
print("G = ",g)
print("A = ",a)
print("C = ",c)
print("T = ",t)




#Plotting our nucleotide
import matplotlib.pyplot as plt
 
labels = ["T", "G","C","A"]
sizes = np.array([t,g,c,a])
explode = (0,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels)
plt.show()




for pileupcolumn in samfile.pileup("CM021837.1",5500,5505):
    print("\ncoverage at base %s = %s" % (pileupcolumn.pos, pileupcolumn.n))
    for pileupread in pileupcolumn.pileups:
        if not pileupread.is_del and not pileupread.is_refskip:
            # query position is None if is_del or is_refskip is set.
            print('\tbase in read %s = %s' %
                  (pileupread.alignment.query_name,
                   pileupread.alignment.query_sequence[pileupread.query_position]))




#Sorting reads based on the name as Pysam takes position sorted file only
bam_list = [*samfile.fetch("")]
bam_list.sort(key=lambda x: x.qname)





#Function for making a BAM file for our test data
import pysam
samfile = pysam.AlignmentFile("alphonso_sorted.bam","rb")
header = samfile.header
with pysam.AlignmentFile("multiple.bam", "wb", header=header) as outf:
# Now you can give gtf information in samfile.fetch()
    for read in samfile.fetch("CM021838.1"):
        outf.write(read)
