from typing import Sequence


def readInput(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    l = len(lines)
    for i in range(l):
        lines[i] = lines[i].rstrip()
    return lines[0], int(lines[1])

def writeOutput(frequent_patterns):
    f = open('OUTPUT.txt', 'w')
    output = ""
    for item in frequent_patterns:
        output += item + " "
    f.write(output)
    f.close()
    print("Successfully wrote output to OUTPUT.txt")


def frequencyTable(text, k):
    frequency_map = {}
    n = len(text)
    for i in range(n-k):
        pattern = text[i:i+k]
        if pattern in frequency_map.keys():
            frequency_map[pattern] += 1
        else:
            frequency_map[pattern] = 1  
    return frequency_map


def maxMap(frequency_map):
    max_frequency = max(frequency_map.values())
    return max_frequency


def frequentWords(text, k):
    frequent_patterns = []
    frequency_table = frequencyTable(text, k)
    max_frequency = max(frequency_table.values())
    for key in frequency_table.keys():
        if frequency_table[key] == max_frequency:
            frequent_patterns.append(key)
    return frequent_patterns


sequence, k = readInput('input/rosalind_ba1b.txt')
frequent_words = frequentWords(sequence, k)
writeOutput(frequent_words)
