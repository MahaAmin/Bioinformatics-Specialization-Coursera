def readInput(fileName):
    # TO-DO: validate input
    f = open(fileName, 'r')
    lines = f.readlines()
    l = len(lines)
    for i in range(l):
        lines[i] = lines[i].rstrip()
    return lines[0], lines[1]


def patternCount(text, pattern):
    count = 0
    end = len(text) - len(pattern)
    patternLength = len(pattern)
    for i in range(end):
        if text[i:i+patternLength] == pattern:  
            count+=1
    return count


text, pattern = readInput('input/rosalind_ba1a.txt')
print(patternCount(text,pattern))