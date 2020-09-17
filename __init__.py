import os
import getpass
from loaders import PageLoader, FileLoader

os.environ["WIKILOADER_WIKI_PREFIX"] = "https://fr.wikipedia.org/wiki"
os.environ["WIKILOADER_COMMON_PREFIX"] = "https://commons.wikimedia.org"
os.environ["WIKILOADER_ROOT_DIR"] = os.path.abspath(os.path.dirname(__file__))
os.environ["WIKILOADER_FILES_DIR"] = os.path.join(os.environ.get("WIKILOADER_ROOT_DIR"), "files")
os.environ["WIKILOADER_HTMLS_DIR"] = os.path.join(os.environ.get("WIKILOADER_ROOT_DIR"), "htmls")


def main(*args, **kwargs):
    loader = PageLoader()
    test_soup = loader.load_from_suffix("Belgique", timeout=1, retry=5)
    file_loader = FileLoader()
    file = file_loader.load_from_link("https://upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Belgium.svg")
    file2 = file_loader.load_from_link("https://upload.wikimedia.org/wikipedia/commons/8/8c/Be-map-fr.png")


if __name__ == '__main__':
    print(f"hello, {getpass.getuser()}")
    main()
