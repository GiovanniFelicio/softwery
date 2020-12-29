def test(string: str, length: int) -> str:
    lengthAux = length
    stringAux = ''
    strings = list()

    if isinstance(string, str) and len(string) > 0:
        strings = string.split(" ")
    else:
        return ""
        
    sizeList = len(strings)
    index = 0

    for i in strings:
        if len(i) <= lengthAux:
            lengthAux = lengthAux - (len(i)+2)
            if index <= sizeList:
                stringAux = stringAux + i + ' '
            
            index+=1
        else:
            break
        lengthAux += 1

    return stringAux
