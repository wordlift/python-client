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

from wordlift_client.models.rank_entities import RankEntities

class TestRankEntities(unittest.TestCase):
    """RankEntities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RankEntities:
        """Test RankEntities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RankEntities`
        """
        model = RankEntities()
        if include_optional:
            return RankEntities(
                rank = 56,
                entities = [
                    wordlift_client.models.entity1.Entity1(
                        reference = '', 
                        properties = wordlift_client.models.properties1.Properties1(
                            name = '', 
                            same_as = [
                                ''
                                ], ), )
                    ]
            )
        else:
            return RankEntities(
        )
        """

    def testRankEntities(self):
        """Test RankEntities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
