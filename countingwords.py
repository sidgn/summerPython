'''sum = 0
for i in range (1, 20):
  if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:   
    sum += i
    print(sum)
print(sum)  '''    

lyrics = "All the steps we take all the moves we make all the pain at stake I see the chaos for everyone Who are we What can we do You and I are same in the way that we have our own styles that we won't change Yours is filled with evil and mine's not there is no way I can lose"
words = lyrics.split()
#thisset = {}
thisset = set()
for word in words:
    thisset.add(word)
newlist = list(thisset)
"""for phrase in thisset:
    newlist.append(phrase)"""
print(newlist)
