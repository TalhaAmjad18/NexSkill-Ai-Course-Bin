# Write a program , to have “Tuples” , with all “noun” in story. Print them. 

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

for noun in nouns:

    # for single word noun

    if noun in string_list:

        nouns_set.add(noun)

    # for multi word noun

    if noun in string:

        nouns_set.add(noun)

nouns_list = tuple(nouns_set)

print(nouns_list)