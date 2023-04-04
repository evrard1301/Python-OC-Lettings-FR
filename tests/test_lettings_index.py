from tests.fixtures import *
from django.urls import reverse_lazy
from oc_lettings_site import models


def test_lettings_index__reachable(client):
    resp = client.get(reverse_lazy('lettings_index'))
    assert 200 == resp.status_code
    assert b'<h1>Lettings</h1>' in resp.content


def test_lettings_index__all_lettings(client, address): 
    models.Letting.objects.create(
        title='first house',
        address=address(1)
    )
    
    models.Letting.objects.create(
        title='second house',
        address=address(2)
    )

    resp = client.get(reverse_lazy('lettings_index'))

    lettings = models.Letting.objects.all()
    assert 200 == resp.status_code

    for letting in lettings:
        assert letting.title in resp.content.decode()
    
