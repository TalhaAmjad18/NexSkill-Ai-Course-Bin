# 3. Title Case (Manual)
# Convert a sentence to title case without using .title().
# o Input: "hELLO wORLD from PYTHON" -> Output: "Hello World From Python"

string = input("Enter a string: ")

print(f"String is: {string}")

stringList = string.split()

word = []

sentence = []

for item in stringList:

    for i in range(len(item)):

        if i == 0:

            if item[i] == 'a':

                word.append('A')

            elif item[i] == 'b':

                word.append('B')

            elif item[i] == 'c':

                word.append('C')

            elif item[i] == 'd':

                word.append('D')

            elif item[i] == 'e':

                word.append('E')

            elif item[i] == 'f':

                word.append('F')

            elif item[i] == 'g':

                word.append('G')

            elif item[i] == 'h':

                word.append('H')

            elif item[i] == 'i':

                word.append('I')

            elif item[i] == 'j':

                word.append('J')

            elif item[i] == 'k':

                word.append('K')

            elif item[i] == 'l':

                word.append('L')

            elif item[i] == 'm':

                word.append('M')

            elif item[i] == 'n':

                word.append('N')

            elif item[i] == 'o':

                word.append('O')

            elif item[i] == 'p':

                word.append('P')

            elif item[i] == 'q':

                word.append('Q')

            elif item[i] == 'r':

                word.append('R')

            elif item[i] == 's':

                word.append('S')

            elif item[i] == 't':

                word.append('T')

            elif item[i] == 'u':

                word.append('U')

            elif item[i] == 'v':

                word.append('V')

            elif item[i] == 'w':

                word.append('W')

            elif item[i] == 'x':

                word.append('X')
            
            elif item[i] == 'y':

                word.append('Y')

            elif item[i] == 'z':

                word.append('Z')

            else:

                word.append(item[i])

        elif i >= 1 and i <= len(item)-1:

            
            if item[i] == 'A':

                word.append('a')

            elif item[i] == 'B':

                word.append('b')

            elif item[i] == 'C':

                word.append('c')

            elif item[i] == 'D':

                word.append('d')

            elif item[i] == 'E':

                word.append('e')

            elif item[i] == 'F':

                word.append('f')

            elif item[i] == 'G':

                word.append('g')

            elif item[i] == 'H':

                word.append('h')

            elif item[i] == 'I':

                word.append('i')

            elif item[i] == 'J':

                word.append('j')

            elif item[i] == 'K':

                word.append('k')

            elif item[i] == 'L':

                word.append('l')

            elif item[i] == 'M':

                word.append('m')

            elif item[i] == 'N':

                word.append('n')

            elif item[i] == 'O':

                word.append('o')

            elif item[i] == 'P':

                word.append('p')

            elif item[i] == 'Q':

                word.append('q')

            elif item[i] == 'R':

                word.append('r')

            elif item[i] == 'S':

                word.append('s')

            elif item[i] == 'T':

                word.append('t')

            elif item[i] == 'U':

                word.append('u')

            elif item[i] == 'V':

                word.append('v')

            elif item[i] == 'W':

                word.append('w')

            elif item[i] == 'X':

                word.append('x')
            
            elif item[i] == 'Y':

                word.append('y')

            elif item[i] == 'Z':

                word.append('z')

            else:

                word.append(item[i])

    sentence.append("".join(word))
   
    word = []

print(f"String in title case: {' '.join(sentence)}")