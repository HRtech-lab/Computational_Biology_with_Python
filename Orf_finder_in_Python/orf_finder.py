#Orf Finder Code
#Four nucleotides of DNA
Nucleotides = ['A', 'C', 'G', 'T']

# Validate DNA sequence in input
def validateSeq(dnaseq):
    tempseq = dnaseq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return False
    return tempseq


# Swap characters
ReverseCompDNA = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
def reverse_complement(seq):
    """
    reverse_complement function takes the single argument as sequence
    return the reverse+complement ordered. 
    """
    # Swapping A with T and G with C vice versa. Reversing newly generated string
    # https://www.geeksforgeeks.org/python-docstrings/
    # https://stackoverflow.com/questions/25188968/reverse-complement-of-dna-strand-using-python
    return ''.join([ReverseCompDNA[nuc] for nuc in seq])[::-1]


# Sequence translation
def translateseq(seq, init_pos=0):
    """
    translateq function takes the arguments
    seq: DNA string sequence
    init_pos: intial position for sequence
    return the sequence i.e. ATGCTGG 
    if init_pos=0 ->then start as/from 'ATG'
    if init_pos=1 ->then start as/from '_TGC'
    if init_pos=2 ->then start as/from '__GCT'
    """
    # https://en.m.wikipedia.org/wiki/Complementary_DNA
    #return [seq[pos:pos + 3] for pos in range(init_pos, len(seq) - 2, 3)]
    return ''.join([seq[pos] for pos in range(init_pos, len(seq), 1)])


def gen_reading_frames(seq):
    """
    gen_reading_frames function takes the single argument as sequence
    return the frames list i.e. ['frame', 'frame2',...]
    """
    # Generating eading-frames of sequences including reverse complement
    # including the reverse complement
    # https://www.genome.gov/genetics-glossary/Open-Reading-Frame
    # https://umd.instructure.com/courses/1199394/pages/exam-questions
    # http://justinbois.github.io/bootcamp/2016/lessons/l17_exercise_2.html
    frames = []
    frames.append(translateseq(seq, 0))
    frames.append(translateseq(seq, 1))
    frames.append(translateseq(seq, 2))
    frames.append(translateseq(reverse_complement(seq), 0))
    frames.append(translateseq(reverse_complement(seq), 1))
    frames.append(translateseq(reverse_complement(seq), 2))
    return frames


def searchCodon(sequence, length):
    """
    searchCodon function takes two arguments:
    sequence: DNA sequence string
    length: Used to display the ORF above the length(LIMIT)

    return the ORF
    """
    MAXLIMIT = length
    
    STARTcodon = "ATG"
    STOPcodon = ["TAA", "TAG", "TGA"]

    position = 0
    ORFsequence = ""
    aasequence = ""
#dictionary of the amino acids according to corresponding DNA string
    gencode_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }
    
    
    maxORF = list()
    
    while (position < len(sequence) - 2):
        # currentCodon-> take 3 steps.
        # i.e. ATGCTGG-> 'ATG'->'TGC'->'GCT'->... 
        currentCodon = sequence[position:position+3]

        # currentCodon is True
        # currentCodon->codon='ATG'
        if (currentCodon == STARTcodon): # ->Start codon
            # Run until currentCodon is not in STOPcodon and gencode table 
            while not (currentCodon in STOPcodon) and (currentCodon in gencode_table):
                ORFsequence = ORFsequence + currentCodon
                # Replace currentCodon i.e. 'TCA' from gencode table
                # Concatenate string with previous assequence(Amino Acid Seq)
                aasequence += gencode_table[currentCodon]
                # Postion for codon to move forward to select next codon
                position = position + 3
                # Replace currentCodon position
                currentCodon = sequence[position:position+3]
            # Concatenate ORFs with respect to currentCodon position
            ORFsequence = ORFsequence + currentCodon
            # ->Stop codon

            # Check ORFsequence length
            if (len(ORFsequence) > MAXLIMIT):
                print('\n>>>START CODON')
                print(f'{ORFsequence}')
                maxORF.append(ORFsequence)
                print('<<<END CODON')
                print("\nAmino Acid Sequence:")
                print(f'{aasequence} Lenth: {len(aasequence)}')    
            # Reset ORFsequence and assequence
            ORFsequence = ""
            aasequence = ""
        # Increase postion
        position = position + 3
    return maxORF
print()
inputfile = input('Enter DNA String: ')
genome = validateSeq(inputfile)

ORFList = list()
iteration = 0
print('\nReading Frames')
#printing all the 6 frames and their all orfs now
for frame in gen_reading_frames(genome):
    print(f'\n***************[FRAME {iteration+1}]***************')
    # return ORF on each iteration
    ORF = searchCodon(frame,0)
    # Add ORF in ORFList on each iteration
    ORFList.append(ORF)
    iteration+=1

#Now finding the longest orf among the 6 frames, if you dont need the longest orf please comment the code below

print(f'\n\n*************LONGEST ORF*************')
print('The longest ORF among all as below\n')
# Converting ORFList into Sting
s = str(ORFList)
#Delimitier
delimiter = ","
string = s.split(delimiter)  #Converts the string into list
#Finding the Longest ORF from the list
print("longest ORF sequence is = ",max(string, key = len))
print("This code is Published by Hassan Raza on Github")
