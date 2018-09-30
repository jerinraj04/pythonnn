def validateString(s):
    letter flag = False
    number flag = False
    for i in s:
        if i.isalpha():
            letter flag = True
        if i.isdigit():
            number_flag = True
    return letter flag and number flag
print validateString('hasAlphanum23')
print validateString('some string')
