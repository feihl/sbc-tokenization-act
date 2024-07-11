user = ("rewrite, unhappy, lossless")

prefix = ["un", "re", "im", "pre", "dis", "mis"]
sufix = ["ful", "less", "ness", "ly", "er"]

tmp = []

for i in user.split():
    for x in prefix:
        if i.startswith(x):
            suffix = i[len(x):]
            tmp.append(x)
            tmp.append(f"{len(x)* "#"}{suffix}")
            break
    else:
        for j in sufix:
            if i.endswith(j):
                prefix = i[:-len(j)]
                tmp.append(f"{prefix}{len(j) * "#"}")
                tmp.append(j)
                break
        else:
            tmp.append(i)        
print(tmp)