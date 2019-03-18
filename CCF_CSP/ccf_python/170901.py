N = int(input())
cnt = 0
r = N%50
cnt +=(N//50)*7
re = r%30
cnt+=(r//30)*4
cnt+=(re//10)*1
print(cnt)
