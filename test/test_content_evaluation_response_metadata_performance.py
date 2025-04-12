# coding: utf-8

"""
    Embeddings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.content_evaluation_response_metadata_performance import ContentEvaluationResponseMetadataPerformance

class TestContentEvaluationResponseMetadataPerformance(unittest.TestCase):
    """ContentEvaluationResponseMetadataPerformance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentEvaluationResponseMetadataPerformance:
        """Test ContentEvaluationResponseMetadataPerformance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentEvaluationResponseMetadataPerformance`
        """
        model = ContentEvaluationResponseMetadataPerformance()
        if include_optional:
            return ContentEvaluationResponseMetadataPerformance(
                automated_metrics = 1.337,
                keyword_analysis = 1.337,
                llm_evaluation = 1.337,
                combine_metrics = 56,
                quality_score = 56
            )
        else:
            return ContentEvaluationResponseMetadataPerformance(
                automated_metrics = 1.337,
                keyword_analysis = 1.337,
                llm_evaluation = 1.337,
                combine_metrics = 56,
                quality_score = 56,
        )
        """

    def testContentEvaluationResponseMetadataPerformance(self):
        """Test ContentEvaluationResponseMetadataPerformance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
