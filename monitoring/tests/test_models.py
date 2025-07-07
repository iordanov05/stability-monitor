import pytest

from monitoring.models import Metric, Server


@pytest.mark.django_db
def test_server_create_and_str():
    s = Server.objects.create(name="srv1", ip="10.1.1.1")
    assert str(s) == f"srv1 (10.1.1.1:{s.port})"


@pytest.mark.django_db
def test_metric_create():
    s = Server.objects.create(name="srv2", ip="10.1.1.2")
    m = Metric.objects.create(server=s, cpu=1, mem=2, disk=3, uptime="1d")
    assert m.server == s
    assert m.cpu == 1
