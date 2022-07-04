from core.providers.provider import Provider


class HeaderNamesSubstituteProvider(Provider):
    def __init__(self):
        pass

    def provide(self):
        return {"src4_addr": "src_ip", "dst4_addr": "dst_ip", "t_first": "session_start_time", "t_last": "session_end_time", "in_packets": "packets_count"}