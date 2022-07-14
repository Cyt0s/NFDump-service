from api.application_runners.uvicorn_application_runner import UvicornApplicationRunner
from api.models.fastapi_application import FastApiApplication
from api.models.fastapi_router import FastApiRouter
import api.routers.basic_router
import api.routers.netflow_router
from core.parsers.nfdump_parser import NFDumpParser
from core.parsers.command_generators.nfdump_command_generator import NFDumpCommandGenerator
from core.providers.keeping_headers_list_provider import KeepingHeadersListProvider
from core.providers.header_names_substitute_provider import HeaderNamesSubstituteProvider
from core.serializers.json_serializer import JsonSerializer
from core.normalizers.netflow_normalizer import NetflowNormalizer
from core.models.flow_scheduler import FlowScheduler
from core.binary_file_orchestrator import BinaryFileOrchestrator
from core.normalizers.logics.extract_headers_logic import ExtractHeadersLogic
from core.normalizers.logics.change_headers_logic import ChangeHeadersLogic
from core.io.file_handler import FileHandler
from configurations.yaml_configuration_reader import YamlConfigurationReader


orchestrator = 'Nan'


class Bootstrapper:
    def __init__(self, conf_path=""):
        self.__routers = []
        self.__conf_path = conf_path


    def bootstrap(self):
        global orchestrator
        configuration_dict = YamlConfigurationReader(self.__conf_path).read_configuration()
        simple_router = FastApiRouter(router=api.routers.basic_router.router, router_configuration={})
        nfdump_router = FastApiRouter(router=api.routers.netflow_router.router, router_configuration={})
        self.__routers.append(simple_router)
        self.__routers.append(nfdump_router)
        api_application = FastApiApplication(self.__routers).application
        orchestrator = self.__bootstrap_core()
        return UvicornApplicationRunner(api_application)

    def __bootstrap_core(self):
        preprocess_logics = []
        process_logics = []
        command_generator = NFDumpCommandGenerator()
        serializer = JsonSerializer()
        parser = NFDumpParser(command_generator, serializer.get_type())
        handler = FileHandler("/Users/iloux/Desktop/nfdump/working/")
        preprocess_logics.append(ExtractHeadersLogic(KeepingHeadersListProvider().provide()))
        process_logics.append(ChangeHeadersLogic(HeaderNamesSubstituteProvider().provide()))
        flow_scheduler = FlowScheduler(preprocess_logics=preprocess_logics, process_logics=process_logics)
        normalizer = NetflowNormalizer(flow_scheduler)
        return BinaryFileOrchestrator(normalizer, parser, serializer, handler)