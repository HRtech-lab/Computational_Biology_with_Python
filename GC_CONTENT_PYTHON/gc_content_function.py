#Function for gc content of given DNA input or read from file
def gc_content(seq):
    """GC content of a given sequence"""
    #Converting all the DNA character to upper case characters
    seq = seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)
