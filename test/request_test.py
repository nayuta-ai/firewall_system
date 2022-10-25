from typing import Dict

import pytest

from src.request import Request, RequestParser


@pytest.mark.parametrize(('request_json', 'converted_request'), [
    (
        Request(table={
             "header": {
                "destination_ip_address": "XXXX.XXXX.XXXX.XXXX",
                "source_ip_address": "XXXX.XXXX.XXXX.XXXX",
                "service_name": "ftp",
                "protocol": "tcp",
                "destination_port": 21,
                "source_port": 80,
                }
        }),
        {
            "source_ip_address": "XXXX.XXXX.XXXX.XXXX",
            "service_name": "ftp",
            "protocol": "tcp",
            "destination_port": 21,
        }

    )
])
def test_request_parser(request_json: Request, converted_request: Dict):
    parse = RequestParser()
    converted_request_table = parse.parse(request=request_json)
    assert type(converted_request_table) == dict
    assert converted_request_table["source_ip_address"] == \
        converted_request["source_ip_address"]
    assert converted_request_table["service_name"] == \
        converted_request["service_name"]
    assert converted_request_table["protocol"] == \
        converted_request["protocol"]
    assert converted_request_table["destination_port"] == \
        converted_request["destination_port"]
