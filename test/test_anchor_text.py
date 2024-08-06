# coding: utf-8

"""
    Manager

    Subscription management and related services.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wordlift_client.models.anchor_text import AnchorText

class TestAnchorText(unittest.TestCase):
    """AnchorText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnchorText:
        """Test AnchorText
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnchorText`
        """
        model = AnchorText()
        if include_optional:
            return AnchorText(
                actual_prompt_template = '',
                enabled = True,
                max_characters = 56,
                model = '',
                prompt_template = ''
            )
        else:
            return AnchorText(
        )
        """

    def testAnchorText(self):
        """Test AnchorText"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
