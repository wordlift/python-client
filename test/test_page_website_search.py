# coding: utf-8

"""
    Analysis

    Analyse content using Linked Data and Knowledge Graphs.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.page_website_search import PageWebsiteSearch

class TestPageWebsiteSearch(unittest.TestCase):
    """PageWebsiteSearch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageWebsiteSearch:
        """Test PageWebsiteSearch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageWebsiteSearch`
        """
        model = PageWebsiteSearch()
        if include_optional:
            return PageWebsiteSearch(
                first = '',
                items = [
                    wordlift_client.models.website_search.WebsiteSearch(
                        clicks = 56, 
                        ctr = 1.337, 
                        id = 56, 
                        impressions = 56, 
                        keys = [
                            ''
                            ], 
                        position = 1.337, 
                        score = 1.337, )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = ''
            )
        else:
            return PageWebsiteSearch(
                first = '',
                items = [
                    wordlift_client.models.website_search.WebsiteSearch(
                        clicks = 56, 
                        ctr = 1.337, 
                        id = 56, 
                        impressions = 56, 
                        keys = [
                            ''
                            ], 
                        position = 1.337, 
                        score = 1.337, )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = '',
        )
        """

    def testPageWebsiteSearch(self):
        """Test PageWebsiteSearch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
