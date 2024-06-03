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

from wordlift-client.models.page_merchant_view import PageMerchantView

class TestPageMerchantView(unittest.TestCase):
    """PageMerchantView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageMerchantView:
        """Test PageMerchantView
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageMerchantView`
        """
        model = PageMerchantView()
        if include_optional:
            return PageMerchantView(
                first = '',
                items = [
                    wordlift-client.models.merchant_view.MerchantView(
                        access_token = '', 
                        account_id = 56, 
                        automatic_synchronization = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        dataset_domain = '', 
                        dataset_name = '', 
                        deleted = True, 
                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        google_merchant_id = 56, 
                        id = 56, 
                        ignore_brand = True, 
                        ignore_image = True, 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        publisher_name = '', 
                        refresh_token = '', 
                        sid = '', 
                        sync_has_errors = True, 
                        sync_id = 56, 
                        sync_products_created = 56, 
                        sync_products_deleted = 56, 
                        sync_products_errored = 56, 
                        sync_products_skipped = 56, 
                        sync_products_total = 56, 
                        sync_products_updated = 56, 
                        sync_started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sync_stopped_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        writer_service = '', )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = ''
            )
        else:
            return PageMerchantView(
                first = '',
                items = [
                    wordlift-client.models.merchant_view.MerchantView(
                        access_token = '', 
                        account_id = 56, 
                        automatic_synchronization = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        dataset_domain = '', 
                        dataset_name = '', 
                        deleted = True, 
                        deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        google_merchant_id = 56, 
                        id = 56, 
                        ignore_brand = True, 
                        ignore_image = True, 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        publisher_name = '', 
                        refresh_token = '', 
                        sid = '', 
                        sync_has_errors = True, 
                        sync_id = 56, 
                        sync_products_created = 56, 
                        sync_products_deleted = 56, 
                        sync_products_errored = 56, 
                        sync_products_skipped = 56, 
                        sync_products_total = 56, 
                        sync_products_updated = 56, 
                        sync_started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sync_stopped_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        writer_service = '', )
                    ],
                last = '',
                next = '',
                prev = '',
                var_self = '',
        )
        """

    def testPageMerchantView(self):
        """Test PageMerchantView"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()