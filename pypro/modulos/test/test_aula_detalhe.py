import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(clinet_com_usuario_logado, modulo, aula):
    resp = clinet_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo_id(resp, aula: Aula):
    assert_contains(resp, f'https://player.vimeo.com/video/{aula.vimeo_id}')


def test_breadcrumb_modulo_titulo_link(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


def test_breadcrumb_aula_titulo(resp, aula: Aula):
    assert_contains(resp, f'<li class="breadcrumb-item active" aria-current="page">{aula.titulo}</li>')


@pytest.fixture
def resp_sem_usuario(client, modulo, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_usuario_nao_logado_redirect(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))
