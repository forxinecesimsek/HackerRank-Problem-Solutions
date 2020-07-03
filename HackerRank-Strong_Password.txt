n = int(input())
password = input()
dictionary = {"l" : 0,
              "u" : 0,
              "s" : 0,
              "n" : 0}

y = 0

for i in password :
    if 'a' <= i <= 'z' :
        dictionary["l"] += 1
    elif 'A' <= i <= 'Z' :
        dictionary["u"] += 1
    elif '0' <= i <= '9' :
        dictionary["n"] += 1
    else :
        dictionary["s"] += 1

for x in dictionary :
    if dictionary[x] == 0 :
        y = y + 1

if n + y < 6 :
    y = 6 - n

print(y)