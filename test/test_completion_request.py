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

from wordlift_client.models.completion_request import CompletionRequest

class TestCompletionRequest(unittest.TestCase):
    """CompletionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompletionRequest:
        """Test CompletionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompletionRequest`
        """
        model = CompletionRequest()
        if include_optional:
            return CompletionRequest(
                frequency_penalty = -2,
                logit_bias = {
                    'key' : 56
                    },
                max_tokens = 1,
                min_words = 0,
                model_id = 1,
                presence_penalty = -2,
                prompt = '',
                stop = '',
                temperature = 0
            )
        else:
            return CompletionRequest(
                prompt = '',
        )
        """

    def testCompletionRequest(self):
        """Test CompletionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
