from datetime import datetime, timedelta
from unittest.mock import MagicMock
from freezegun import freeze_time


hit_list = []
# {timestamp_minute: counter, }
improved_hit_list = {}
# Returns num of hits in interval (5mins)
# O(n), O(1)
def get_num_of_hits():
    trim_time = datetime.utcnow() - timedelta(minutes=5)
    timestamp_bucket = (trim_time.year, trim_time.month, trim_time.day, trim_time.hour, trim_time.minute)
    num_hits = 0
    copy = improved_hit_list.copy()
    for key, value in copy.items():
        if key < timestamp_bucket:
            improved_hit_list.pop(key)
        else:
            num_hits += value
    return num_hits


# add a hit at current time
# Append to global list O[1]
def log_hit():
    now = datetime.utcnow()
    timestamp_bucket = (now.year, now.month, now.day, now.hour, now.minute)
    improved_hit_list[timestamp_bucket]  = improved_hit_list.get(timestamp_bucket, 0) + 1


def test_get_num_hits_base_case():
    log_hit()
    assert get_num_of_hits() == 1
    global improved_hit_list
    improved_hit_list = {} 

def test_mock_old_timestamps():
    with freeze_time("2018-01-01"):
        log_hit()
    assert get_num_of_hits() == 0
    global improved_hit_list
    improved_hit_list = {}

print(test_mock_old_timestamps())
