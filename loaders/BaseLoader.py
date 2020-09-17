import os
import re
from io import StringIO, BytesIO
from pathlib import Path
from PIL import Image


class BaseLoader:
    _PREFIX = None
    _PERSIST_DIR = None
    _current_source = None
    _response = None

    def __init__(self, *args, **kwargs):
        if args or kwargs:
            print(*args)
            raise NotImplementedError(f"{__name__} called with arg: {[arg for arg in args]}-{kwargs}")
        self._request_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        }

    def _build_url(self, suffix: str) -> str:
        return f"{self._PREFIX}/{suffix}"

    def _persist(self):
        content_type, file_type = re.split("[/;+]", self._response.headers.get("Content-Type"))[:2]
        ext = f".{file_type}"
        file_name = f'{self._current_source.split("/")[-1].split(".")[0]}{ext}'
        file_path = Path(os.path.join(self._PERSIST_DIR, file_name))
        with open(file_path, "wb") as file:
            file.write(self._response.content)

    def get_current_source(self) -> str:
        return self._current_source
