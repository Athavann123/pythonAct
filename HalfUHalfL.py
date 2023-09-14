sentence = "I like turtles"
half1 = sentence[0:(len(sentence)//2)]
half2 = sentence[len(sentence)//2:-1]
print(half1.upper() + half2.lower())