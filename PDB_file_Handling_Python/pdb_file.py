#Pdb file handling in Python
# I have used file having pdb id "5olk.pdb"
#Part(a) Amino_acid_sequence
import re
print("Part(a) The amino acid sequence is below:  \n")
print("The amine acid sequence is below:  \n")
print("\n  Chain    ","             Amino Acid sequence\n")
g = u'\u2193'
print("   ",g,"                        ",g)
#Please Enter Your file name Below: The program will take care of the Rest 
File_name="5olk.pdb"
with open(File_name, 'r') as infile:
    for line in infile:
        if line.startswith("SEQRES"):
            a = line
            b = a.replace("SEQRES","")
            d = ''.join([i for i in b if not i.isdigit()]) 
            print(d)
countflag = 0
checkflagstotal = {}
flags = {'GLY', 'ALA', 'VAL', 'LEU', 'ILE', 'PRO', 'PHE', 'MET', 'TRP'}

# file open
fhand = open(File_name)
for line in fhand:
    # removing unneccasary line spaces
    line = line.rstrip()
    # looking for a line which stats with SEQRES
    if line.startswith('SEQRES'):
        # spliting line in words
        words = line.split()
        for word in words:
            # check word is in flag? if TRUE
            if word in flags:
                # Count total flags in which any flag found(line starts with SQRES) 
                countflag += 1
                # add word elements in dictionary
                if word not in checkflagstotal:
                    checkflagstotal[word] = 1
                else:
                    checkflagstotal[word] = checkflagstotal[word] + 1
# file close
fhand.close()
print("\nPart(B)")
print(f'Total no of Hydrophobic Amino Acids: {countflag}.')
print(f'Individual Sum:{checkflagstotal}')

#Part(c)

checkflagstotal = {}

# file open
fhand = open(File_name)

for line in fhand:
    # looking for a line which stats with COMPND
    if line.startswith('COMPND'):
        # looking for a 'CHAIN: A, B, C, D, ....;' strings
        line = re.findall("CHAIN:\s(.*)", line) # https://regex101.com/
        for chain in line:
            # remving unnecessary spaces, commas, and semicolon
            chain = chain.rstrip()
            chain = chain.replace(' ','')
            chain = chain.replace(',','')
            chain = chain.replace(';','')
            for element in chain:
                # add chain elements in dictionary
                if element not in checkflagstotal:
                    checkflagstotal[element] = 1
                else:
                    checkflagstotal[element] = checkflagstotal[element] + 1

# file close
fhand.close()
print("\nPart(c)")
print(f'Total Proteins Chains: {len(checkflagstotal)}')
print(checkflagstotal)


#Part(d & e)
File = open(File_name, 'r')
hr = File.read()
helix = hr.count("HELIX")
sheets = hr.count("SHEET")
print("\nPart(d)")
print("The number of Helices =   ", helix)
print("\nPart(e)")
print("The number of Sheets =  ", sheets)
print("\nThis code is a property of HASSAN RAZA")
