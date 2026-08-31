# Write a program, to list all words, with vowel in it.

from The_Last_Algorithm import string

string_list = string.split()

vowel_words_list = []

for i in range(len(string_list)):
    if 'A' in string_list[i] or 'E' in string_list[i] or 'I' in string_list[i] or 'O' in string_list[i] or 'U' in string_list[i] or 'a' in string_list[i] or 'e' in string_list[i] or 'i' in string_list[i] or 'o' in string_list[i] or 'u' in string_list[i]:
        vowel_words_list.append(string_list[i])

print(vowel_words_list)