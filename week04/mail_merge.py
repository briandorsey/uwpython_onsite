
data = [
    {'name': 'George',
     'gift': 'a goldfish',
    },
    {'name': 'Joe',
     'gift': 'several small pieces of lint',
    },
    {'name': 'Jennifer',
     'gift': 'a red wagon',
    },
]

template = """
Dear %(name)s,

Thank you so much for your gift of %(gift)s. I will treasure it forever.
I've always wanted an excuse to get %(gift)s, and now I don't have to pay for it!

Please enjoy this form letter as a token of my sincere appreciation.

"""

for item in data:
    print 'Filling template for %s' % item['name']
    message = template % item
    file_name = 'thank_you_%s.txt' % item['name'].lower()
    f = open(file_name, 'w')
    f.write(message)
    f.close()


