string = str(input())
rev_string = string[::-1]
rev_string = rev_string.replace(' ', '')
rev_string = rev_string.lower()
string = string.replace(' ', '')
string = string.lower()

if string == rev_string:
    print('YES')
else:
    print('NO')
