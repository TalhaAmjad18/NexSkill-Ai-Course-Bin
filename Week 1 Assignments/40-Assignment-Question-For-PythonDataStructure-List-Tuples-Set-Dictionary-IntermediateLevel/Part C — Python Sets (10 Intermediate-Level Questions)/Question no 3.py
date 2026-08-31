# 3. Given a sentence, return all unique words in lowercase.

sentence = input("Enter a sentence: ").lower()

splittedSentence = sentence.split()

uniqueSplittedSentence = set(splittedSentence)

print(f"Unique words in lowercase: {uniqueSplittedSentence}")