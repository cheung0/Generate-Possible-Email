def convert(string, company):
    # clean the input string
    string = string.lower()

    # test to see if input is valid
    if len(string.split(' ')) != 2:
        return 'string not properly formatted'

    # firstlast@company.com
    email1 = ''
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

    # lastfirst_initial@company.com
    email3 = ''
    arr3 = string.split(' ')
    email3 += arr3[1]
    email3 += arr3[0][0]
    email3 += '@'
    email3 += company
    email3 += '.com'

    # firstlast_initial@company.com
    email5 = ''
    arr5 = string.split(' ')
    email5 += arr5[0]
    email5 += arr5[1][0]
    email5 += '@'
    email5 += company
    email5 += '.com'

    # last@company.com
    email4 = ''
    arr4 = string.split(' ')
    email4 += arr4[1]
    email4 += '@'
    email4 += company
    email4 += '.com'

    return email1, email3, email4, email5, email2

print(convert('Jane Doe', 'amazon'))
print(convert('John Doe', 'amazon'))
