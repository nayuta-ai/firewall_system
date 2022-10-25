import xml.etree.ElementTree


class Service:
    def __init__(self, short: str, port: str, protocol: str):
        self.short = short
        self.port = Port(protocol=protocol, port=port)


class Port:
    """ A class for recording the pair of protocol and port """
    def __init__(self, protocol: str, port: str):
        self.port = port
        self.protocol = protocol


class ServiceParser:
    def __init__(self):
        self.services_path = "/workspace/services/"

    def load(self, file: str) -> Service:
        root = self._xml_parse(file=file)
        short = self._get_short(root)
        if not short:
            raise ValueError("")

        protocol, port = self._get_port(root)
        if not protocol or not port:
            raise ValueError("")

        return Service(short=short, protocol=protocol, port=port)

    def _xml_parse(self, file: str) -> xml.etree.ElementTree.Element:
        path = self.services_path + file + ".xml"
        tree = xml.etree.ElementTree.parse(path)
        return tree.getroot()

    def _get_short(self, root: xml.etree.ElementTree.Element) -> str:
        return root.find("short").text

    def _get_port(
        self,
        root: xml.etree.ElementTree.Element
    ) -> tuple[str, str]:
        port = root.find("port")
        return port.attrib.get("protocol"), port.attrib.get("port")
