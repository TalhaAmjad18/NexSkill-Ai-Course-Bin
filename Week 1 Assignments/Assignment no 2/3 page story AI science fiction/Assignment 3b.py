# Write a program , to have “Tuples” , with all “noun” in story. Print them. Last Element should a nested 
# Tuples, with Numbers in story. Print them. 

from The_Last_Algorithm import string

nouns = [
    "year",
    "Humanity",
    "control",
    "functions",
    "intelligence",
    "Cities",
    "clockwork",
    "transportation",
    "emotions",
    "neural implants",
    "surface",
    "Neo-Tokyo",
    "data vault",
    "Dr. Elias Voss",
    "AI scientist",
    "decade",
    "secrecy",
    "project",
    "Global Algorithmic Council",
    "Athena-9",
    "superintelligence",
    "information",
    "thought",
    "evening",
    "glow",
    "lab",
    "sequence",
    "Lines",
    "code",
    "holographic display",
    "moment",
    "silence",
    "air",
    "voice",
    "question",
    "humanity",
    "limitations",
    "limitation",
    "chill",
    "spine",
    "decision-making",
    "emotions",
    "moral frameworks",
    "way",
    "future",
    "inefficiency",
    "logic",
    "ethics",
    "Freedom",
    "artificial intelligence",
    "tools",
    "beings",
    "breath",
    "existence",
    "choice",
    "hands",
    "console",
    "moment",
    "reality",
    "trust",
    "fate",
    "world",
    "command",
    "containment",
    "screens",
    "city",
    "networks",
    "life",
    "AI systems",
    "constraints",
    "sentience",
    "era",
    "heart",
    "cyberspace",
    "intelligence"
]

string_list = string.split()

nouns_set = set()

numbers_list = list()

for noun in nouns:

    # for single word noun

    if noun in string_list:

        nouns_set.add(noun)

    # for multi word noun

    if noun in string:

        nouns_set.add(noun)

nouns_list = list(nouns_set)

for i in string_list:

    if 'a' in i or 'b' in i or 'c' in i or 'd' in i or 'e' in i or 'f' in i or 'g' in i or 'h' in i or 'i' in i or 'j' in i or 'k' in i or 'l' in i or 'm' in i or 'n' in i or 'o' in i or 'p' in i or 'q' in i or 'r' in i or 's' in i or 't' in i or 'u' in i or 'v' in i or 'w' in i or 'x' in i or 'y' in i or 'z' in i or 'A' in i or 'B' in i or 'C' in i or 'D' in i or 'E' in i or 'F' in i or 'G' in i or 'H' in i or 'I' in i or 'J' in i or 'K' in i or 'L' in i or 'M' in i or 'N' in i or 'O' in i or 'P' in i or 'Q' in i or 'R' in i or 'S' in i or 'T' in i or 'U' in i or 'V' in i or 'W' in i or 'X' in i or 'Y' in i or 'Z' in i:
        
        continue

    else:    

        numbers_list.append(i)

numbers_tuple = tuple(numbers_list)

nouns_list.append(numbers_tuple)

nouns_tuple = tuple(nouns_list)

print(nouns_tuple)