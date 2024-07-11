characters = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

words = ("Hai hello how are you? Hello! Hello!")
value = []

tmp = ""

for i in words:
    if i not in characters:
        tmp += i
    else:
        t = "".join(tmp).lstrip()
        value.append(t)
        tmp = ""
print(value)