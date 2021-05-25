# find the longest word in zen python

with open("zen_text".text) as reader:
    words = []
    for line in reader:
        words = words + line.split("")
    words.sort()
    print("Longest word: " + words[-1])
