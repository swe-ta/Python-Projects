with open("story_2.txt", "r") as s:
    story_2 = s.read()

words = set()
startWord = -1

targetStart = "<"
targetEnd = ">"

for i, char in enumerate(story_2):
    if char == targetStart:
        startWord = i

    if char == targetEnd and targetStart != -1:
        word = story_2[startWord: i + 1]
        words.add(word)
        startWord = -1

answers = {}

for word in words:
    answer = input("Enter a word for" + word+ ":")
    answers[word] = answer

for word in words:
    story_2 = story_2.replace(word,answers[word])

print(story_2)
