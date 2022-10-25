import json
from typing import Dict


class Request:
    def __init__(self, table: Dict):
        self.request_json = self._create_json(table=table)

    def _create_json(self, table: Dict) -> json:
        return json.dumps(table, indent=4)


class RequestParser:
    def parse(self, request: Request) -> Dict:
        """ A function for parsing request json

        Args:
            request (Request): a request json

        Returns:
            Dict: a converted request table included
                source_ip_address, service_name, protocol,
                and destination_port. Using them enabled firewall
                to check whether the valid access is
        """
        request_table = self._convert_json_into_dict(request=request)["header"]
        converted_request_table = dict()
        converted_request_table["source_ip_address"] = \
            request_table["source_ip_address"]
        converted_request_table["service_name"] = \
            request_table["service_name"]
        converted_request_table["protocol"] = \
            request_table["protocol"]
        converted_request_table["destination_port"] = \
            request_table["destination_port"]
        return converted_request_table

    def _convert_json_into_dict(self, request: Request) -> Dict:
        return json.loads(request.request_json)
