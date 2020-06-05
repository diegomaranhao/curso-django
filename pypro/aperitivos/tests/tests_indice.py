import pytest
# Create your views here.
from django.urls import reverse

from pypro.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def teste_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Motivação',
        'Passar do dia'
    ]
)
def test_video_title(resp, titulo):
    assert_contains(resp, titulo)
