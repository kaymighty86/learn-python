treeData = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

for row in treeData:
    for pixel in row:
        shade = " " if pixel == 0 else "*"
        print(shade, end="")#print all in the same line
    print()#step down to a new line
