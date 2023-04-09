from tests.fixtures import *
from django.urls import reverse_lazy
from lettings import models


def test_lettings__ok(client, address):
    letting = models.Letting.objects.create(
        title='my letting',
        address=address(89)
    )

    resp = client.get(reverse_lazy('lettings:letting', kwargs={
        'letting_id': letting.id
    }))

    assert 200 == resp.status_code
    assert b'my letting' in resp.content
    assert b'89 Champs de l&#x27;Essart' in resp.content
    assert b'Audincourt, France 25400' in resp.content
