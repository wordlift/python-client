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

from wordlift-client.models.account_subscription import AccountSubscription

class TestAccountSubscription(unittest.TestCase):
    """AccountSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountSubscription:
        """Test AccountSubscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountSubscription`
        """
        model = AccountSubscription()
        if include_optional:
            return AccountSubscription(
                email = '',
                first_name = '',
                last_name = '',
                order_id = 56,
                sku = ''
            )
        else:
            return AccountSubscription(
        )
        """

    def testAccountSubscription(self):
        """Test AccountSubscription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()