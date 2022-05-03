#GC Content Script
f = open("dna.fasta", "r") 
contents = (f.read()) 
length = len(contents) 
C_count = contents.count("C") 
G_count = contents.count("G")
GC_value = C_count + G_count
# GC content is calculated by dividing the GC value by the length of entiire sequnce and multiplied by 100.
GC_content = GC_value / length * 100
print(GC_content)
print("Code by hassan raza")
