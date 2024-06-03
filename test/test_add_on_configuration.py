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

from wordlift_client.models.add_on_configuration import AddOnConfiguration

class TestAddOnConfiguration(unittest.TestCase):
    """AddOnConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddOnConfiguration:
        """Test AddOnConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddOnConfiguration`
        """
        model = AddOnConfiguration()
        if include_optional:
            return AddOnConfiguration(
                can_do_content_expansion = True,
                can_import_to_wordpress = True,
                key = '',
                wp_admin = '',
                wp_json = ''
            )
        else:
            return AddOnConfiguration(
        )
        """

    def testAddOnConfiguration(self):
        """Test AddOnConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
