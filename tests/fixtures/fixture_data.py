import random
from datetime import datetime

import pytest


@pytest.fixture
def random_timestamp():
    left_ts = 1000198000
    right_ts = 1000198991
    return random.randint(left_ts, right_ts)


@pytest.fixture
def current_timestamp():
    return datetime.now().timestamp()


@pytest.fixture
def api_url():
    return 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
