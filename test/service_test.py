import xml.etree.ElementTree

import pytest

from src.service import Service, ServiceParser


@pytest.mark.parametrize(('file', 'expected'), [
    (
        "ftp", Service(short="FTP", protocol="tcp", port="21")
    ),
])
def test_service_parser(file: str, expected: Service):
    parser = ServiceParser()
    assert type(parser._xml_parse(file=file)) == xml.etree.ElementTree.Element
    root = parser._xml_parse(file=file)
    assert type(parser._get_short(root=root)) == str
    assert parser._get_short(root=root) == expected.short
    assert type(parser._get_port(root=root)) == tuple
    assert parser._get_port(root=root)[0] == expected.port.protocol
    assert parser._get_port(root=root)[1] == expected.port.port
    service = parser.load(file=file)
    assert service.short == expected.short
    assert service.port.protocol == expected.port.protocol
    assert service.port.port == expected.port.port
