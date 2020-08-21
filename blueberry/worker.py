import time
import json
from worker_helpers import get_cmd_args, get_instance


def task_handler():
    path = get_cmd_args()
    app = get_instance(path.app)
    while True:
        time.sleep(0.5)
        redis_db = app.redis_db
        for task in sorted(redis_db.keys()):
            data = json.loads(redis_db[task])
            func = app.func_registry[data['func']]
            func(*data['args'], **data['kwargs'])
            del redis_db[task]


if __name__ == '__main__':
    task_handler()         