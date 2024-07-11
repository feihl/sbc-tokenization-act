words = ("Hai hello how are you?")
value = []

tmp = ""

for i in words:
    if i == " ":
        value.append(tmp)  
        tmp = ""
    else:
        tmp += i
if tmp:
    value.append(tmp)
print(value)