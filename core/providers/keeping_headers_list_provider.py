from core.providers.provider import Provider


class KeepingHeadersListProvider(Provider):
    def __init__(self):
        pass

    def provide(self):
        return ["src4_addr", "dst4_addr", "t_first", "t_last", "in_packets"]
