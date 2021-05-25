with open("zen-words.txt", "r") as reader:
    #for line in reader:
    list_words = reader.read().split()
    fnd_long = max(list_words, key=len)
    print(fnd_long)
    #print(line, end="")
