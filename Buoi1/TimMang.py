input_str=input("Nhap x,y:")
dimensions=[int(x) for x in input_str.split(",")]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist=[[0 for col in range (colNum)] for row in range( rowNum)]
for row in range (rowNum):
    for col in range (colNum):
        multilist[row][col]=row*col
print(multilist)