import random
import time

def wait_random():
    min_wait_time = 10
    max_wait_time = 15
    """Espera un tiempo aleatorio entre min_wait_time y max_wait_time segundos"""
    wait_time = random.uniform(min_wait_time, max_wait_time)
    time.sleep(wait_time)