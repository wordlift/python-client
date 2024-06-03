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

from wordlift-client.models.o_auth2_authorized_client_request import OAuth2AuthorizedClientRequest

class TestOAuth2AuthorizedClientRequest(unittest.TestCase):
    """OAuth2AuthorizedClientRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2AuthorizedClientRequest:
        """Test OAuth2AuthorizedClientRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2AuthorizedClientRequest`
        """
        model = OAuth2AuthorizedClientRequest()
        if include_optional:
            return OAuth2AuthorizedClientRequest(
                access_token_expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                access_token_issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                access_token_scopes = '',
                access_token_type = '',
                access_token_value = '',
                client_registration_id = '',
                principal_name = '',
                refresh_token_issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                refresh_token_value = ''
            )
        else:
            return OAuth2AuthorizedClientRequest(
        )
        """

    def testOAuth2AuthorizedClientRequest(self):
        """Test OAuth2AuthorizedClientRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()