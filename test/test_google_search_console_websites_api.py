# coding: utf-8

"""
    Events

    An API to record and query events raised by clients in order to facilitate KPI tracking.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.api.google_search_console_websites_api import GoogleSearchConsoleWebsitesApi


class TestGoogleSearchConsoleWebsitesApi(unittest.TestCase):
    """GoogleSearchConsoleWebsitesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GoogleSearchConsoleWebsitesApi()

    def tearDown(self) -> None:
        pass

    def test_get_gsc_sites(self) -> None:
        """Test case for get_gsc_sites

        Get Google Search Console sites
        """
        pass


if __name__ == '__main__':
    unittest.main()
