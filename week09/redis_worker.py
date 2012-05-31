import urllib
import redis

work_queue = 'queue:urls'
host = 'localhost'

r = redis.Redis(host)

while True:
    try:
        key, url = r.brpop(work_queue)
        print "...",
        data = urllib.urlopen(url).read()
        print '%-10s %s' % (len(data), url)
    except StandardError, e:
        print e
