"""
Demonstrate generators and lazy computation
From Jon Jacky's Intro to Python course:
    http://staff.washington.edu/jon/python-course/
"""


# review range
print range(10)

# Print a million elements, type ^C to stop
# for i in range(1000000): print i

# Try to print a billion elements, may fail with MemoryError
# for i in range(1000000000): print i

# Use xrange not range for a billion elements, type ^C to stop
# for i in xrange(1000000000): print i

# range is eager - computes all the elements first
# xrange is lazy - computes each element as needed

# Python generators code lazy computation,
# remember values of local variables between calls


def my_xrange(size):
    i = -1
    while True:
        i += 1
        if i < size:
            yield i  # yield not return makes generator
        else:
            return   # StopIteration is automatically raised on return

for i in my_xrange(3):
    print i

# generate a billion elements
# for i in my_xrange(1000000000): print i  # ^C to stop

# Generator expressions are like list comprehensions, but lazy

# one hundred million elements
# list comprehension may fail with MemoryError after 20+ sec
# sum([2*i for i in xrange(100000000)])

# one hundred million elements
# generator expression returns result after 20+ sec
# sum(2*i for i in xrange(100000000))


######################################

class IterateMe(object):
    limit = 3
    current = 0

    def __iter__(self):
        return self
    
    def next(self):
        self.current += 1
        if self.current > self.limit:
            raise StopIteration
        else:
            return self.current

import time
# generate values which will never be repeated
def timer(count):
    i = 0
    while i < count:
        i += 1
        time.sleep(1)
        yield time.time()

# generate lines from a file, without needing to read entire file into memory
def lines():
    for line in open('generator.py'):
        print len(line)
