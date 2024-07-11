characters = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

words = "Hai hello how are you? Hello! Hello! hehehhe. huhuhuhuh!"
sys = []

tmp = ""

for i in words:
    if i in characters:
        if tmp:
            sys.append(tmp.strip() + i)
            tmp = ""
        else:
            if sys:
                sys[-1] += i
    else:
        tmp += i
print(sys)