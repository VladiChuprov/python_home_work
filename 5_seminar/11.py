n=int(input())
arr=[[0]*n for i in range(n)]
i=1
x=0
y=-1
d_col=1
d_row=0
lengh=len(str(n**2))
while i<=n**2:
    if 0<=x+d_row<n and 0<=y+d_col<n and arr[x+d_row][y+d_col]==0:
        y+=d_col
        x+=d_row
        arr[x][y]=i
        i+=1
    else :
        if d_col==1:
            d_col=0
            d_row=1
        elif d_row==1:
            d_row=0
            d_col=-1
        elif d_col==-1:
            d_col=0
            d_row=-1
        elif d_row==-1:
            d_row=0
            d_col=1
for i in arr:
    for j in i:
        print(str(j).rjust(lengh),end=' ')
    print()