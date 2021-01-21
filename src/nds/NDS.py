from .Banner import Banner
from .Header import Header


class NDS:
    header: Header
    banner: Banner

    def __init__(self) -> None:
        super().__init__()
        self.header = Header()
        self.banner = Banner()
