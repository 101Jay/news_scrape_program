
glovar = 5

def glvar():
    global glovar
    glovar = 10
    print(glovar)

glvar()

print(glovar)

