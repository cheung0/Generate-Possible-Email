def convert(string, company):
    # firstlast@company.com
    email1 = ''
    string = string.lower()
    arr1 = string.split(' ')
    for part in arr1:
        email1 += part
    email1 += '@'
    email1 += company
    email1 += '.com'

    # first.last@company.com
    email2 = ''
    arr2 = string.split(' ')
    email2 += arr2[0]
    email2 += '.'
    email2 += arr2[1]
    email2 += '@'
    email2 += company
    email2 += '.com'

    return email1, email2

print(convert('Iron Man', 'avenger'))
print(convert('Captain America', 'avenger'))
print(convert('Black Widow', 'avenger'))
