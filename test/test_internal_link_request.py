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

from wordlift_client.models.internal_link_request import InternalLinkRequest

class TestInternalLinkRequest(unittest.TestCase):
    """InternalLinkRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalLinkRequest:
        """Test InternalLinkRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalLinkRequest`
        """
        model = InternalLinkRequest()
        if include_optional:
            return InternalLinkRequest(
                items = [
                    wordlift_client.models.item.Item(
                        query = wordlift_client.models.vector_search_query_request.VectorSearchQueryRequest(
                            fields = [
                                ''
                                ], 
                            filters = [
                                wordlift_client.models.filter.Filter(
                                    key = '', 
                                    operator = 'EQ', 
                                    value = wordlift_client.models.filter_value.Filter_value(), )
                                ], 
                            query_embedding = [
                                1.337
                                ], 
                            query_string = '', 
                            query_uri = '', 
                            query_url = '', 
                            similarity_top_k = 1, ), 
                        source_name = '', )
                    ],
                template = ''
            )
        else:
            return InternalLinkRequest(
        )
        """

    def testInternalLinkRequest(self):
        """Test InternalLinkRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
