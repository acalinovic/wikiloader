import os

import requests
from bs4 import BeautifulSoup
from . import BaseLoader


class PageLoader(BaseLoader):

    _current_soup = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._PREFIX = os.environ.get("WIKILOADER_WIKI_PREFIX")
        self._PERSIST_DIR = os.environ.get("WIKILOADER_HTMLS_DIR")

    def get_current_soup(self) -> BeautifulSoup:
        return self._current_soup

    def load_from_suffix(
            self, suffix: str,
            timeout: float = None,
            retry: int = None,
            persist: bool = True
    ) -> BeautifulSoup:
        self._current_source = self._build_url(suffix)
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
                    self._current_soup = BeautifulSoup(self._response.text, 'html.parser')
                    if persist:
                        self._persist()
                    break
            except requests.exceptions.ConnectTimeout:
                print(f"ConnectTimeout on {self._current_source}, retries left: {retries}")
            except requests.exceptions.ReadTimeout:
                print(f"ReadTimeout on {self._current_source}, retries left: {retries}")
            retries -= 1
        return self.get_current_soup()
