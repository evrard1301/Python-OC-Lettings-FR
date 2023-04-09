from tests.fixtures import *
from django.urls import reverse_lazy


def test_profiles_index__all_profiles(client, profile):
    profiles = [
        profile('Alice', 'Angers'),
        profile('Bob', 'Belfort'),
        profile('Claire', 'Cleron')
    ]

    resp = client.get(reverse_lazy('profiles:index'))

    assert 200 == resp.status_code

    for profile in profiles:
        assert profile.user.username in resp.content.decode()
