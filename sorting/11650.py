import sys
n = int(input())
arr = []
for i in range(n):
    x, y = list(map(int,sys.stdin.readline().split()))
    arr.append([x, y])
arr.sort(key=lambda x:(x[0], x[1]))
for i in arr:
    print(i[0], i[1])
