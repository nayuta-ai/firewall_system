import pytest

from src.firewall import FireWall
from src.request import Request


@pytest.mark.parametrize(('request_json'), [
    (
        Request(table={
             "header": {
                "destination_ip_address": "XXXX.XXXX.XXXX.XXXX",
                "source_ip_address": "XXXX.XXXX.XXXX.XXXX",
                "service_name": "ftp",
                "protocol": "tcp",
                "destination_port": 21,
                "source_port": 80,
                },
        })
    )
])
def test_firewall(request_json: Request):
    firewall = FireWall()
    assert firewall.filter(request_json=request_json) is False
    firewall.add_service("ftp")
    assert firewall.filter(request_json=request_json) is True
    firewall.delete_service("ftp")
    assert firewall.filter(request_json=request_json) is False
