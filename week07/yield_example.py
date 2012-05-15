def counter():
    print 'counter: starting counter'
    i = -5
    while i < 5:
        i = i + 1
        print 'counter: yield', i
        yield i


if __name__ == '__main__':
    print 'call generator function'
    c = counter()
    print 'repr(c):', repr(c)
    print 'iterate'
    for item in c:
        print 'received:', item
