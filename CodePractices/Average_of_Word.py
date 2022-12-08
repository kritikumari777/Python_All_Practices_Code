sentence = "Hi my name is Bob"
words = sentence.split()
average = sum(len(word) for word in words) / len(words)
print(round(average))

avg= sum(map(len,words))/len(words)
print(round(avg))