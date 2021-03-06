"""Tests to ensure that the lxml tree builder generates good trees."""

from beautifulsoup.testing import (
    BuilderInvalidMarkupSmokeTest,
    BuilderSmokeTest,
)

class TestLXMLBuilder(BuilderSmokeTest):
    """See `BuilderSmokeTest`."""

    def test_bare_string(self):
        # lxml puts a <p> tag around the bare string.
        self.assertSoupEquals(
            "A bare string", "<p>A bare string</p>")

    def test_foo(self):
        isolatin = """<html><meta http-equiv="Content-type" content="text/html; charset=ISO-Latin-1" />Sacr\xe9 bleu!</html>"""
        soup = self.soup(isolatin)

        utf8 = isolatin.replace("ISO-Latin-1".encode(), "utf-8".encode())
        utf8 = utf8.replace("\xe9", "\xc3\xa9")

        print soup


class TestLXMLBuilderInvalidMarkup(BuilderInvalidMarkupSmokeTest):
    """See `BuilderInvalidMarkupSmokeTest`."""

