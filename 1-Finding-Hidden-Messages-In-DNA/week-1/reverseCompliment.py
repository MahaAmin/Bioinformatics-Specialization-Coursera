def readInput(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    l = len(lines)
    for i in range(l):
        lines[i] = lines[i].rstrip()
    return lines[0]


def writeOutput(sequence):
    f = open('OUTPUT.txt', 'w')
    f.write(sequence)
    f.close()
    print('Successfully wrote output to OUTPUT.txt')


def complimentSeq(sequence):
    complimentary_seq = ""
    for nucleotide in sequence:
        if nucleotide == 'A':
            complimentary_seq += "T"
        elif nucleotide == 'T':
            complimentary_seq += "A"
        elif nucleotide == 'C':
            complimentary_seq += "G"
        elif nucleotide == 'G':
            complimentary_seq += "C"
        else:
            complimentary_seq += "-"
    return complimentary_seq


def reverseComplimentSeq(sequence):
    complimentary_seq = complimentSeq(sequence)
    return complimentary_seq[::-1]


sequence = readInput('input/rosalind_ba1c.txt')
reverse_compliment_seq = reverseComplimentSeq(sequence)
writeOutput(reverse_compliment_seq)

        