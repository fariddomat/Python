s=input("enter phase")
x=input('search for keyword')

for i in range(0,len(s)):
    if x==s[i:len(x)+i]:
        print('found at index ',i)
