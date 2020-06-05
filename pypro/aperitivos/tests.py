import pytest
# Create your views here.
from django.urls import reverse

from pypro.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def teste_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp):
    assert_contains(resp, '<h1>Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/425991579"')
