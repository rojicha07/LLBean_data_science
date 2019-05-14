pi = 3.1415926
char = ''
result = ''
lenght = str(pi)[::-1].find('.')
for n in reversed(range(2, lenght+1)):
    pi2= '%.*f' % (n, pi)
    char+= '*'
    result += " "+char+" "+pi2

print(result)