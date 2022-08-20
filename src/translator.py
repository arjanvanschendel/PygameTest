import string

def coordsToName(coords: string):
    x, y = coords.replace('(','').replace(')', '').split(',')
    x = chr(int(x)+97)
    y = str(8-int(y))
    return str(x) + str(y)

def nameToCoords(name: string):
    x = str(ord(name[0])-97)
    y = str(8-int(name[1]))
    return x + "," + y