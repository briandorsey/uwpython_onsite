import redis

host = 'localhost'

r = redis.Redis(host)

r.subscribe('messages')

for event in r.listen():
    print event['data']
