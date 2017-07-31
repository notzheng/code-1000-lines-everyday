b = 0
comment = []
f = open("xiechenglvxing1.txt","r", encoding='utf-8')

for line in f:
    b += 1
    s = line.split()
    try:
        a = {
            "comment":s[0],
            "rating":s[1]
        }
        comment.append(a)

    except:
        pass

f.close()
print(b)
print(comment)