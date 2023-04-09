from tests.fixtures import *
from django.urls import reverse_lazy


def test_index__reachable(client):
    resp = client.get(reverse_lazy('index'))
    assert 200 == resp.status_code
    assert b'Welcome to Holiday Homes' in resp.content
