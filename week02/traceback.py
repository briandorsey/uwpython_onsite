

def exceptional():
    print "I am exceptional!"
    print 1/0

def passive():
    pass

def doer():
    passive()
    exceptional()

if __name__ == '__main__':
    doer()
