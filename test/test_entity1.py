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

from wordlift_client.models.entity1 import Entity1

class TestEntity1(unittest.TestCase):
    """Entity1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Entity1:
        """Test Entity1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Entity1`
        """
        model = Entity1()
        if include_optional:
            return Entity1(
                reference = '',
                properties = wordlift_client.models.properties1.Properties1(
                    name = '', 
                    same_as = [
                        ''
                        ], )
            )
        else:
            return Entity1(
        )
        """

    def testEntity1(self):
        """Test Entity1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
