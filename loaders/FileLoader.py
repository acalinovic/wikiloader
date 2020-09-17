import os
from pathlib import Path
import requests
from . import BaseLoader


class FileLoader(BaseLoader):

    _current_file: Path = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._PREFIX = os.environ.get("WIKILOADER_COMMON_PREFIX")
        self._PERSIST_DIR = os.environ.get("WIKILOADER_FILES_DIR")

    def get_current_file(self) -> Path:
        return self._current_file

    def load_from_link(self, link: str, timeout: float = None, retry: int = None) -> Path:
        self._current_source = link
        options = {
            'headers': self._request_headers
        }
        if timeout and isinstance(timeout, float):
            options["timeout"] = timeout

        if isinstance(retry, int) and retry > 0:
            retries = retry
        else:
            retries = 0
        while retries >= 0:
            try:
                self._response = requests.get(self._current_source, **options)
                if self._response.status_code > 200:
                    print(f"request on {self._current_source} failed with {self._response.status_code} status code")
                    break
                else:
                    self._current_file = Path(os.path.join(self._PERSIST_DIR, self._current_source.split("/")[-1]))
                    self._persist()
                    break
            except requests.exceptions.ReadTimeout:
                print(f"Timeout on {self._current_source}, retries left: {retries}")
            retries -= 1
        return self.get_current_file()
