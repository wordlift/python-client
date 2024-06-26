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

from wordlift_client.models.smart_content import SmartContent

class TestSmartContent(unittest.TestCase):
    """SmartContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartContent:
        """Test SmartContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SmartContent`
        """
        model = SmartContent()
        if include_optional:
            return SmartContent(
                account_id = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                model_id = 1
            )
        else:
            return SmartContent(
                account_id = 56,
        )
        """

    def testSmartContent(self):
        """Test SmartContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
