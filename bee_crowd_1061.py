dia,date1=input().split()
date1 = int(date1)
h1,m1,s1=map(int,input().split(":"))

dia,date2=input().split()
date2 = int(date2)
h2,m2,s2=map(int,input().split(":"))

s = s2 - s1
m = m2 - m1
h = h2 - h1
date = date2 - date1

if s < 0:
    s = s + 60
    m-= 1
if m < 0:
    m = m + 60
    h-= 1
if h < 0:
    h = h + 24
    date-= 1

print(f"{date} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")