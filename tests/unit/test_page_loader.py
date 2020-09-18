def test_load_page_from_suffix_force_timeout(page_loader, wiki_page_suffix):
    page_loader.load_from_suffix(wiki_page_suffix, timeout=0.0000001, retry=1)
    assert page_loader.get_current_soup() is None


def test_load_page_from_suffix_without_timeout(page_loader, wiki_page_suffix):
    page_loader.load_from_suffix(wiki_page_suffix)
    assert page_loader.get_current_soup().find(
        "h1", attrs={"id": "firstHeading"}
    ).text == wiki_page_suffix


def test_foreign_page_loader(foreign_page_loader):
    foreign_page_loader.load_from_suffix("Belgium")
    assert foreign_page_loader.get_current_soup().find(
        "h1", attrs={"id": "firstHeading"}
    ).text == "Belgium"


def test_page_loader_article_not_found(page_loader):
    page_loader.load_from_suffix("ThisArticleShouldNotExists")
    assert page_loader.get_current_sc() == 404
