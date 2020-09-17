def test_load_svg_from_link_with_force_timeout(file_loader, wiki_svg_url):
    file_loader.load_from_link(
        wiki_svg_url,
        timeout=0.0000001,
        retry=1
    )
    print(file_loader.get_current_file())
    assert file_loader.get_current_file() is None


def test_load_svg_from_link(file_loader, wiki_svg_url):
    file_loader.load_from_link(
        wiki_svg_url,
        timeout=1.0,
        retry=1
    )
    assert file_loader.get_current_file() is not None


def test_load_png_from_link(file_loader, wiki_png_url):
    file_loader.load_from_link(
        wiki_png_url,
        timeout=1.0,
        retry=1
    )
    assert file_loader.get_current_file() is not None
