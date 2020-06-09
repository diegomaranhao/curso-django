import pytest
# Create your views here.
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.base.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def teste_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_video_link(resp, videos):
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
