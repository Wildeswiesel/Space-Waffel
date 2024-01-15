höhe=8
stammhöhe=2
for i in range(höhe):
    spaces=" " * (höhe-i-1)
    characters="x" * (2*i+1)
    print(spaces + characters)

for j in range(stammhöhe):
    ospaces=" "*(höhe-2)
    print(ospaces + "ooo")