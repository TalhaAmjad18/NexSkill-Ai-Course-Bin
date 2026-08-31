# 10. Mask Email Username
# Mask all but the first and last character of the username with *; keep domain intact.
# o Input: "john.doe@example.com" -> Output: "j******e@example.com"

email = input("Enter your email: ")

print(f"Your email is: {email}")

splitEmail = email.split("@")

# print(splitEmail)

maskedEmailList = []

itemOne = splitEmail[0]

for i in range(len(itemOne)):

    if i == 0 or i == len(itemOne) - 1:

        maskedEmailList.append(itemOne[i])

    else:

        maskedEmailList.append('*')

maskedEmailList.append('@')

maskedEmailList.append(splitEmail[1])

maskedEmail = "".join(maskedEmailList)

print(f"After mask, your email is: {maskedEmail}")