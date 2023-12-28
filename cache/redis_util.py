import redis


redis_conn = redis.Redis(host='localhost', port=6379)


def write_to_redis(empid, name):
    try:
        redis_conn.set(empid, name)
        redis_conn.expire(empid, 24*60*60)
    except Exception as e:
        pass


def read_from_redis(empid):
    try:
        name = redis_conn.get(empid)
    except Exception as e:
        name = None

    return name
