str = input()
output = ''

for i in str:
    if  i.isupper():
        output += i.lower()
    else:
        output += i.upper()
        
print(output)