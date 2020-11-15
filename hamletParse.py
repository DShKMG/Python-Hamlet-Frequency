import os.path
import urllib.request
import urllib.parse
import urllib.error
import re

wholeLine = ""
fSecondName = urllib.request.urlopen(
    'http://www.cs.utsa.edu/~bylander/cs1063/hamlet.txt')

for line in fSecondName:
    wholeLine += line.decode().strip()

# After Parsing Editing and removing uncessary
# Used regex : "[\\p{Punct}\\s]+"
# rawHamletText has our raw
startRequired = wholeLine.find('Actus Primus')
endIndex = wholeLine.find("FINIS.")
rawHamletText = wholeLine[startRequired:endIndex]
# Above we get the only the raw hamlet book and not copyright or any comment on the page
hamletList = re.compile("\\W+").split(rawHamletText)

# Get the frequency of the each word
counts = dict()
for words in hamletList:
    counts[words] = counts.get(words, 0) + 1
# It is counted by key - value pairing and increase value each instance we see the word

# Add Sorting according to values
# print(counts) has the values of each occurrence

# Also add mapping so that we can list from high to low
sortedDict = {k: v for k, v in sorted(
    counts.items(), key=lambda item: item[1], reverse=True)}
# This contain the sorted keys from high to low
keyList = list(sortedDict.keys())
valList = list(sortedDict.values())
"""
In order to find the how much of a value occurs in the list is done by 

sortedDict[keyList[desiredIndex]]
"""

# File handling will be done by try except block
try:
    fileTopTen = open("Top 10 Words.txt", "w+")
except:
    print("File cannot be created !")


for i in range(0, 10):
    print(i+1, "- ", keyList[i],
          " : ", sortedDict[keyList[i]], "\n")
    if (os.path.exists("Top 10 Words.txt")):
        fileTopTen.write(str(i+1))
        fileTopTen.write("- ")
        fileTopTen.write(keyList[i])
        fileTopTen.write(" : ")
        fileTopTen.write(str(sortedDict[keyList[i]]))
        fileTopTen.write("\n")

fileTopTen.close()  # Finishes top ten list


# Saving Whole dictionary into the CSV file
# The file will have 2 headers Words , Number of Occurrence

header = {'Words': 'Number of Occurrence'}

with open('Total Word Frequency.txt', 'w', newline='') as totalWordFreq:
    rankWord = 0
    for k in range(0, len(keyList)):
        totalWordFreq.write(str(rankWord))
        totalWordFreq.write("- ")
        totalWordFreq.write(keyList[k])
        totalWordFreq.write(" : ")
        totalWordFreq.write(str(valList[k]))
        totalWordFreq.write("\n")
        rankWord += 1
