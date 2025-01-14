from django.urls import reverse_lazy


def test_profiles__ok(client, profile):
    profile('Alice', 'Angers')
    profile('Bob', 'Besancon')

    resp = client.get(reverse_lazy('profiles:profile', kwargs={
        'username': 'Bob'
    }))

    assert 200 == resp.status_code

    content = resp.content.decode()
    must_be_presents = [
        'First name: bob',
        'Last name: BOB',
        'Email: bob@email.com',
        'Favorite city: Besancon'
    ]

    for txt in must_be_presents:
        assert txt in content
