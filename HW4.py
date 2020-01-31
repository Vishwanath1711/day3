# if we found the cookies start with vowels we have to replace with the next non vowel
start=0
for i in range(0,11):
    cookie=(input("Enter the cookie name"))
    if cookie[start]=='a' or cookie[start]=='A':
            cookie[start]='b'
    elif cookie[start]=='e' or cookie[start]=='E':
            cookie[start]='f'
    elif cookie[start]=='I' or cookie[start]=='i':
            cookie[start]='j'
    elif cookie[start]=='O' or cookie[start]=='o':
            cookie[start]='p'
    elif cookie[start]=='U' or cookie[start]=='u':
            cookie[start]='v'
    else:
            print("updated cookies are:")
            print(cookie)

    
