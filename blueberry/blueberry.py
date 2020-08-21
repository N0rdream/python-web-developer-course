import redis
import json
import time


class Blueberry:

    def __init__(self, host='localhost', port=6379):
        self.redis_db = redis.StrictRedis(
            host=host, 
            port=port, 
            db=0,
            decode_responses=True
        )
        self.func_registry = {}


    def delay(self, func_name, *args, **kwargs):
        data = json.dumps({
            'func': func_name,
            'args': args,
            'kwargs': kwargs
        })
        self.redis_db[str(time.time())] = data


    def register(self):
        def decorator(func):
            self.func_registry[func.__name__] = func
            return func
        return decorator