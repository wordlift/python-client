# coding: utf-8

"""
    WordLift API

    WordLift API

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.kg_embedding_response import KgEmbeddingResponse

class TestKgEmbeddingResponse(unittest.TestCase):
    """KgEmbeddingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KgEmbeddingResponse:
        """Test KgEmbeddingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KgEmbeddingResponse`
        """
        model = KgEmbeddingResponse()
        if include_optional:
            return KgEmbeddingResponse(
                id = '',
                model = ''
            )
        else:
            return KgEmbeddingResponse(
                id = '',
                model = '',
        )
        """

    def testKgEmbeddingResponse(self):
        """Test KgEmbeddingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
