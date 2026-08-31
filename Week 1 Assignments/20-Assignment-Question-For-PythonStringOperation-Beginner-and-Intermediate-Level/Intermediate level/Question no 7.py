# 7. Compress Repeated Characters (RLE-lite)
# Compress runs of the same character as .
# o Input: "aaabbcaaaa" -> Output: "a3b2c1a4"

string = input("Enter a string: ")

l = list()

i = 0

while i < len(string):

    j = i

    count = 0

    while j < len(string):

        if string[i] == string[j]:

            count += 1
    
            j+=1

        else:
    
            j+=1
    
            break

    l.append(string[i])
    
    l.append(str(count))

    i+=count

result = "".join(l)

print(result)