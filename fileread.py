try:
    fhand = open('essay.txt', 'r')
except:
    print('File not available.')
    quit()        
thisset = set()
wordcount = dict()
for line in fhand:
    for word in line.split():
        thisset.add(word)
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1   
#print(thisset)
print(wordcount)