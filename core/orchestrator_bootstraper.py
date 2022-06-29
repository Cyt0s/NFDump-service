from core.parsers.nfdump_parser import NFDumpParser
from core.parsers.command_generators.nfdump_command_generator import NFDumpCommandGenerator
from core.models.file import File
from core.serializers.json_serializer import JsonSerializer
from core.normalizers.netflow_normalizer import NetflowNormalizer
from core.models.flow_scheduler import FlowScheduler
from core.binary_file_orchestrator import BinaryFileOrchestrator
from core.normalizers.logics.extract_headers_logic import ExtractHeadersLogic
from core.normalizers.logics.change_headers_logic import ChangeHeadersLogic


def bootstrap():
    preprocess_logics = []
    process_logics = []
    command_generator = NFDumpCommandGenerator()
    serializer = JsonSerializer()
    parser = NFDumpParser(command_generator, serializer.get_type())
    preprocess_logics.append(ExtractHeadersLogic(["src4_addr", "dst4_addr", "t_first", "t_last", "in_packets"]))
    process_logics.append(ChangeHeadersLogic({"src4_addr": "src_ip", "dst4_addr": "dst_ip", "t_first": "session_start_time", "t_last": "session_end_time", "in_packets": "packets_count"}))
    flow_scheduler = FlowScheduler(preprocess_logics=preprocess_logics, process_logics=process_logics)
    normalizer = NetflowNormalizer(flow_scheduler)
    return BinaryFileOrchestrator(normalizer, parser, serializer)


orchestrator = bootstrap()
