# coding: utf-8

"""
    GraphQL support

    GraphQL endpoint to query Knowledge Graphs

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.ask_request import AskRequest

class TestAskRequest(unittest.TestCase):
    """AskRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AskRequest:
        """Test AskRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AskRequest`
        """
        model = AskRequest()
        if include_optional:
            return AskRequest(
                message = '',
                model = '',
                security = True
            )
        else:
            return AskRequest(
                message = '',
        )
        """

    def testAskRequest(self):
        """Test AskRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
