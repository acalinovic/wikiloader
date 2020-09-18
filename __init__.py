import getpass
import os

os.environ["WIKILOADER_SEARCH_LANG"] = "fr"
os.environ["WIKILOADER_WIKI_PREFIX"] = f"https://{os.environ.get('WIKILOADER_SEARCH_LANG')}.wikipedia.org/wiki"
os.environ["WIKILOADER_COMMON_PREFIX"] = "https://commons.wikimedia.org"
os.environ["WIKILOADER_ROOT_DIR"] = os.path.abspath(os.path.dirname(__file__))
os.environ["WIKILOADER_FILES_DIR"] = os.path.join(os.environ.get("WIKILOADER_ROOT_DIR"), "files")
os.environ["WIKILOADER_HTMLS_DIR"] = os.path.join(os.environ.get("WIKILOADER_ROOT_DIR"), "htmls")


def main(*args, **kwargs):
    pass


if __name__ == '__main__':
    print(f"hello, {getpass.getuser()}")
    main()
