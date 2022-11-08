def is_isogram(str):
    str = str.lower()
    x = 0
    for i in str:
        if str.count(i) > 1:
            x = x+1
    if x > 1:
        return (True)
    else:
        return (False)


print(is_isogram('string'))
