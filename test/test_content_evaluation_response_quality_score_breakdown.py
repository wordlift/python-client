# coding: utf-8

"""
    Embeddings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.content_evaluation_response_quality_score_breakdown import ContentEvaluationResponseQualityScoreBreakdown

class TestContentEvaluationResponseQualityScoreBreakdown(unittest.TestCase):
    """ContentEvaluationResponseQualityScoreBreakdown unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentEvaluationResponseQualityScoreBreakdown:
        """Test ContentEvaluationResponseQualityScoreBreakdown
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentEvaluationResponseQualityScoreBreakdown`
        """
        model = ContentEvaluationResponseQualityScoreBreakdown()
        if include_optional:
            return ContentEvaluationResponseQualityScoreBreakdown(
                content = wordlift_client.models.content_evaluation_response_quality_score_breakdown_content.ContentEvaluationResponse_quality_score_breakdown_content(
                    purpose = 56, 
                    accuracy = 56, 
                    depth = 56, ),
                readability = wordlift_client.models.content_evaluation_response_quality_score_breakdown_readability.ContentEvaluationResponse_quality_score_breakdown_readability(
                    score = 1.337, 
                    grade_level = 56, 
                    complex_sentences = wordlift_client.models.content_evaluation_response_quality_score_breakdown_readability_complex_sentences.ContentEvaluationResponse_quality_score_breakdown_readability_complex_sentences(
                        hard = 56, 
                        very_hard = 56, 
                        total = 56, ), ),
                seo = wordlift_client.models.content_evaluation_response_quality_score_breakdown_seo.ContentEvaluationResponse_quality_score_breakdown_seo(
                    keyword_density = {
                        'key' : 1.337
                        }, 
                    top_entities = {
                        'key' : [
                            wordlift_client.models.content_evaluation_response_quality_score_breakdown_seo_top_entities_value_inner.ContentEvaluationResponse_quality_score_breakdown_seo_top_entities_value_inner(
                                text = '', 
                                count = 56, )
                            ]
                        }, 
                    score = 56, )
            )
        else:
            return ContentEvaluationResponseQualityScoreBreakdown(
                content = wordlift_client.models.content_evaluation_response_quality_score_breakdown_content.ContentEvaluationResponse_quality_score_breakdown_content(
                    purpose = 56, 
                    accuracy = 56, 
                    depth = 56, ),
                readability = wordlift_client.models.content_evaluation_response_quality_score_breakdown_readability.ContentEvaluationResponse_quality_score_breakdown_readability(
                    score = 1.337, 
                    grade_level = 56, 
                    complex_sentences = wordlift_client.models.content_evaluation_response_quality_score_breakdown_readability_complex_sentences.ContentEvaluationResponse_quality_score_breakdown_readability_complex_sentences(
                        hard = 56, 
                        very_hard = 56, 
                        total = 56, ), ),
                seo = wordlift_client.models.content_evaluation_response_quality_score_breakdown_seo.ContentEvaluationResponse_quality_score_breakdown_seo(
                    keyword_density = {
                        'key' : 1.337
                        }, 
                    top_entities = {
                        'key' : [
                            wordlift_client.models.content_evaluation_response_quality_score_breakdown_seo_top_entities_value_inner.ContentEvaluationResponse_quality_score_breakdown_seo_top_entities_value_inner(
                                text = '', 
                                count = 56, )
                            ]
                        }, 
                    score = 56, ),
        )
        """

    def testContentEvaluationResponseQualityScoreBreakdown(self):
        """Test ContentEvaluationResponseQualityScoreBreakdown"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
