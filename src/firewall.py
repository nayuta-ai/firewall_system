from src.request import Request, RequestParser
from src.service import ServiceParser


class FireWall:
    def __init__(self):
        self.name_service = dict()
        self.service_parser = ServiceParser()
        self.requst_parser = RequestParser()

    def filter(self, request_json: Request) -> bool:
        """ A function for filtering request

        First, it checks whether the valid service is. Next,
        it checks whether the valid destination port and protocol is.
        Finally, if request matches all of the condition, it returns True.

        Args:
            request_json (Request): a request json

        Returns:
            bool: If a request can pass, it returns True.
        """
        request_table = self.requst_parser.parse(request=request_json)
        service = request_table["service_name"]
        if service in self.name_service:
            if request_table["destination_port"] != \
                    int(self.name_service[service].port.port):
                return False

            if request_table["service_name"] != \
                    self.name_service[service].short.lower():
                return False

            if request_table["protocol"] != \
                    self.name_service[service].port.protocol:
                return False

            return True

        else:
            print("Request Rejected")
            return False

    def add_service(self, file: str) -> None:
        """ A function for adding service

        It can add a service in services folder.

        Args:
            file (str): a service file in services folder
        """
        self.name_service[file] = self.service_parser.load(file=file)
        print(f"Add {file} service")

    def delete_service(self, file: str) -> None:
        """ A function for deleting service

        It can delete a service in services folder
        and also can't delete a file in services folder.

        Args:
            file (str): a service file in services folder
        """
        del self.name_service[file]
        print(f"Delete {file} service")

    def show_services(self):
        print("Show services")
        for service in self.name_service.keys():
            print(service)
