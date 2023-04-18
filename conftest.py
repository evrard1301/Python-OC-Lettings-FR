import pytest
from django.test import Client
from profiles.models import Profile
from lettings.models import Address
from django.contrib.auth.models import User


@pytest.fixture
def client(db):
    return Client()


@pytest.fixture
def address(db):
    return lambda x: Address.objects.create(
        number=x,
        street='Champs de l\'Essart',
        city='Audincourt',
        state='France',
        zip_code='25400',
        country_iso_code='FR'
    )


@pytest.fixture
def profile(db):
    def create(name, city):
        user = User.objects.create(
            username=name,
            first_name=name.lower(),
            last_name=name.upper(),
            email=f'{name.lower()}@email.com'
        )
        return Profile.objects.create(
            user=user,
            favorite_city=city
        )
    return create
