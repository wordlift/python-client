# coding: utf-8

"""
    Embeddings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.image_to_text_request import ImageToTextRequest

class TestImageToTextRequest(unittest.TestCase):
    """ImageToTextRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageToTextRequest:
        """Test ImageToTextRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageToTextRequest`
        """
        model = ImageToTextRequest()
        if include_optional:
            return ImageToTextRequest(
                image_url = '',
                prompt_type = 'Other',
                custom_prompt = ''
            )
        else:
            return ImageToTextRequest(
                image_url = '',
                prompt_type = 'Other',
        )
        """

    def testImageToTextRequest(self):
        """Test ImageToTextRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
