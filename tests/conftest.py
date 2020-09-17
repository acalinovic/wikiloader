from pytest import fixture
from loaders import PageLoader, FileLoader


@fixture
def wiki_page_suffix():
    return "Belgique"


@fixture
def wiki_png_url():
    return "https://upload.wikimedia.org/wikipedia/commons/8/8c/Be-map-fr.png"


@fixture
def wiki_svg_url():
    return "https://upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Belgium.svg"


@fixture
def page_loader():
    return PageLoader()


@fixture
def file_loader():
    return FileLoader()
