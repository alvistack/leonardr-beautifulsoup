"""Helper classes for tests."""

import unittest
from beautifulsoup import BeautifulSoup
from beautifulsoup.element import Comment, SoupStrainer
from beautifulsoup.builder import LXMLTreeBuilder

class SoupTest(unittest.TestCase):

    @property
    def default_builder(self):
        return LXMLTreeBuilder()

    def soup(self, markup, **kwargs):
        """Build a Beautiful Soup object from markup."""
        builder = kwargs.pop('builder', self.default_builder)
        return BeautifulSoup(markup, builder=builder, **kwargs)

    def document_for(self, markup):
        """Turn an HTML fragment into a document.

        The details depend on the builder.
        """
        return self.default_builder.test_fragment_to_document(markup)

    def assertSoupEquals(self, to_parse, compare_parsed_to=None):
        builder = self.default_builder
        obj = BeautifulSoup(to_parse, builder=builder)
        if compare_parsed_to is None:
            compare_parsed_to = to_parse

        self.assertEquals(obj.decode(), self.document_for(compare_parsed_to))





