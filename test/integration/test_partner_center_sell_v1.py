# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for PartnerCenterSellV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_platform_services.partner_center_sell_v1 import *

# Config file name
config_file = 'partner_center_sell_v1.env'

class TestPartnerCenterSellV1():
    """
    Integration Test Class for PartnerCenterSellV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.partner_center_sell_service = PartnerCenterSellV1.new_instance(
            )
            assert cls.partner_center_sell_service is not None

            cls.config = read_external_sources(
                PartnerCenterSellV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.partner_center_sell_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_products(self):

        list_products_response = self.partner_center_sell_service.list_products()

        assert list_products_response.get_status_code() == 200
        list_products_response = list_products_response.get_result()
        assert list_products_response is not None

    @needscredentials
    def test_create_product(self):

        create_product_response = self.partner_center_sell_service.create_product(
            product_name='testString',
            tax_assessment='SOFTWARE',
            product_type='SOFTWARE',
            material_agreement=True
        )

        assert create_product_response.get_status_code() == 200
        product_details = create_product_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_get_product(self):

        get_product_response = self.partner_center_sell_service.get_product(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert get_product_response.get_status_code() == 200
        product_details = get_product_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_update_product(self):

        update_product_response = self.partner_center_sell_service.update_product(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            material_agreement=True,
            product_name='testString',
            tax_assessment='SOFTWARE'
        )

        assert update_product_response.get_status_code() == 200
        product_details = update_product_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_publish_product(self):

        publish_product_response = self.partner_center_sell_service.publish_product(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert publish_product_response.get_status_code() == 200
        product_details = publish_product_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_suspend_product(self):

        suspend_product_response = self.partner_center_sell_service.suspend_product(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            reason='testString'
        )

        assert suspend_product_response.get_status_code() == 200
        product_details = suspend_product_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_deprecate_product(self):

        deprecate_product_response = self.partner_center_sell_service.deprecate_product(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            reason='testString'
        )

        assert deprecate_product_response.get_status_code() == 200
        product_details = deprecate_product_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_restore_product(self):

        restore_product_response = self.partner_center_sell_service.restore_product(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            reason='testString'
        )

        assert restore_product_response.get_status_code() == 200
        product_details = restore_product_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_list_badges(self):

        list_badges_response = self.partner_center_sell_service.list_badges()

        assert list_badges_response.get_status_code() == 200
        cloud_badge = list_badges_response.get_result()
        assert cloud_badge is not None

    @needscredentials
    def test_get_badge(self):

        get_badge_response = self.partner_center_sell_service.get_badge(
            badge_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert get_badge_response.get_status_code() == 200
        cloud_badge = get_badge_response.get_result()
        assert cloud_badge is not None

    @needscredentials
    def test_get_catalog(self):

        get_catalog_response = self.partner_center_sell_service.get_catalog(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert get_catalog_response.get_status_code() == 200
        catalog_listing_details = get_catalog_response.get_result()
        assert catalog_listing_details is not None

    @needscredentials
    def test_update_catalog(self):

        # Construct a dict representation of a HighlightSectionInput model
        highlight_section_input_model = {
            'description': 'testString',
            'title': 'testString',
        }

        # Construct a dict representation of a MediaSectionInput model
        media_section_input_model = {
            'caption': 'testString',
            'thumbnail': 'testString',
            'type': 'image',
            'url': 'testString',
        }

        update_catalog_response = self.partner_center_sell_service.update_catalog(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            catalog_id='testString',
            description='testString',
            icon_url='testString',
            keywords=['testString'],
            pricing_model='free',
            category='testString',
            provider_type=['ibm_community'],
            label='testString',
            name='testString',
            provider='testString',
            tags=['testString'],
            documentation_url='testString',
            highlights=[highlight_section_input_model],
            long_description='testString',
            media=[media_section_input_model]
        )

        assert update_catalog_response.get_status_code() == 200
        catalog_listing_details = update_catalog_response.get_result()
        assert catalog_listing_details is not None

    @needscredentials
    def test_request_catalog_approval(self):

        request_catalog_approval_response = self.partner_center_sell_service.request_catalog_approval(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert request_catalog_approval_response.get_status_code() == 200
        resource = request_catalog_approval_response.get_result()
        assert resource is not None

    @needscredentials
    def test_list_plans(self):

        list_plans_response = self.partner_center_sell_service.list_plans(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert list_plans_response.get_status_code() == 200
        list_plans_response = list_plans_response.get_result()
        assert list_plans_response is not None

    @needscredentials
    def test_create_plan(self):

        create_plan_response = self.partner_center_sell_service.create_plan(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            description='testString',
            label='testString',
            type='byol',
            url='testString'
        )

        assert create_plan_response.get_status_code() == 200
        create_plan_response = create_plan_response.get_result()
        assert create_plan_response is not None

    @needscredentials
    def test_get_plan(self):

        get_plan_response = self.partner_center_sell_service.get_plan(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            pricing_plan_id='testString'
        )

        assert get_plan_response.get_status_code() == 200
        license = get_plan_response.get_result()
        assert license is not None

    @needscredentials
    def test_update_plan(self):

        update_plan_response = self.partner_center_sell_service.update_plan(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            pricing_plan_id='testString',
            description='testString',
            label='testString',
            type='byol',
            url='testString'
        )

        assert update_plan_response.get_status_code() == 200
        create_plan_response = update_plan_response.get_result()
        assert create_plan_response is not None

    @needscredentials
    def test_get_support(self):

        get_support_response = self.partner_center_sell_service.get_support(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert get_support_response.get_status_code() == 200
        support = get_support_response.get_result()
        assert support is not None

    @needscredentials
    def test_update_support(self):

        # Construct a dict representation of a EscalationContactsUpdate model
        escalation_contacts_update_model = {
            'email': 'testString',
            'name': 'testString',
        }

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {
            'day': 1,
            'end_time': '19:30',
            'start_time': '10:30',
        }

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {
            'always_available': True,
            'times': [support_details_availability_times_model],
            'timezone': 'America/Los_Angeles',
        }

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {
            'type': 'hour',
            'value': 2,
        }

        # Construct a dict representation of a SupportDetails model
        support_details_model = {
            'availability': support_details_availability_model,
            'contact': 'testString',
            'response_wait_time': support_response_times_model,
            'type': 'email',
        }

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {
            'type': 'hour',
            'value': 2,
        }

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {
            'contact': 'testString',
            'escalation_wait_time': support_escalation_times_model,
            'response_wait_time': support_response_times_model,
        }

        update_support_response = self.partner_center_sell_service.update_support(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            escalation_contacts=[escalation_contacts_update_model],
            locations=['US'],
            support_details=[support_details_model],
            support_escalation=support_escalation_model,
            support_type='third-party',
            url='https://my-company.com/support'
        )

        assert update_support_response.get_status_code() == 200
        support = update_support_response.get_result()
        assert support is not None

    @needscredentials
    def test_list_support_change_requests(self):

        list_support_change_requests_response = self.partner_center_sell_service.list_support_change_requests(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert list_support_change_requests_response.get_status_code() == 200
        list_support_change_requests_response = list_support_change_requests_response.get_result()
        assert list_support_change_requests_response is not None

    @needscredentials
    def test_create_support_change_request(self):

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {
            'day': 1,
            'end_time': '19:30',
            'start_time': '10:30',
        }

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {
            'always_available': True,
            'times': [support_details_availability_times_model],
            'timezone': 'America/Los_Angeles',
        }

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {
            'type': 'hour',
            'value': 2,
        }

        # Construct a dict representation of a SupportDetails model
        support_details_model = {
            'availability': support_details_availability_model,
            'contact': 'testString',
            'response_wait_time': support_response_times_model,
            'type': 'email',
        }

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {
            'type': 'hour',
            'value': 2,
        }

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {
            'contact': 'testString',
            'escalation_wait_time': support_escalation_times_model,
            'response_wait_time': support_response_times_model,
        }

        # Construct a dict representation of a Support model
        support_model = {
            'locations': ['US'],
            'process': 'testString',
            'process_i18n': {'foo': 'bar'},
            'support_details': [support_details_model],
            'support_escalation': support_escalation_model,
            'support_type': 'third-party',
            'url': 'https://my-company.com/support',
        }

        create_support_change_request_response = self.partner_center_sell_service.create_support_change_request(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            change=support_model
        )

        assert create_support_change_request_response.get_status_code() == 200
        product_details = create_support_change_request_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_get_support_change_request(self):

        get_support_change_request_response = self.partner_center_sell_service.get_support_change_request(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            change_request_id='testString'
        )

        assert get_support_change_request_response.get_status_code() == 200
        change_request = get_support_change_request_response.get_result()
        assert change_request is not None

    @needscredentials
    def test_update_support_change_request(self):

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {
            'day': 1,
            'end_time': '19:30',
            'start_time': '10:30',
        }

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {
            'always_available': True,
            'times': [support_details_availability_times_model],
            'timezone': 'America/Los_Angeles',
        }

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {
            'type': 'hour',
            'value': 2,
        }

        # Construct a dict representation of a SupportDetails model
        support_details_model = {
            'availability': support_details_availability_model,
            'contact': 'testString',
            'response_wait_time': support_response_times_model,
            'type': 'email',
        }

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {
            'type': 'hour',
            'value': 2,
        }

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {
            'contact': 'testString',
            'escalation_wait_time': support_escalation_times_model,
            'response_wait_time': support_response_times_model,
        }

        # Construct a dict representation of a Support model
        support_model = {
            'locations': ['US'],
            'process': 'testString',
            'process_i18n': {'foo': 'bar'},
            'support_details': [support_details_model],
            'support_escalation': support_escalation_model,
            'support_type': 'third-party',
            'url': 'https://my-company.com/support',
        }

        update_support_change_request_response = self.partner_center_sell_service.update_support_change_request(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            change_request_id='testString',
            change=support_model
        )

        assert update_support_change_request_response.get_status_code() == 200
        product_details = update_support_change_request_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_list_support_change_request_reviews(self):

        list_support_change_request_reviews_response = self.partner_center_sell_service.list_support_change_request_reviews(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            change_request_id='testString'
        )

        assert list_support_change_request_reviews_response.get_status_code() == 200
        resource = list_support_change_request_reviews_response.get_result()
        assert resource is not None

    @needscredentials
    def test_request_support_change_request_review(self):

        request_support_change_request_review_response = self.partner_center_sell_service.request_support_change_request_review(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            change_request_id='testString'
        )

        assert request_support_change_request_review_response.get_status_code() == 200
        resource = request_support_change_request_review_response.get_result()
        assert resource is not None

    @needscredentials
    def test_merge_support_change_request(self):

        merge_support_change_request_response = self.partner_center_sell_service.merge_support_change_request(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            change_request_id='testString'
        )

        assert merge_support_change_request_response.get_status_code() == 200
        product_details = merge_support_change_request_response.get_result()
        assert product_details is not None

    @needscredentials
    def test_request_support_approval(self):

        request_support_approval_response = self.partner_center_sell_service.request_support_approval(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert request_support_approval_response.get_status_code() == 200
        resource = request_support_approval_response.get_result()
        assert resource is not None

    @needscredentials
    def test_request_product_approval(self):

        request_product_approval_response = self.partner_center_sell_service.request_product_approval(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert request_product_approval_response.get_status_code() == 200
        resource = request_product_approval_response.get_result()
        assert resource is not None

    @needscredentials
    def test_list_product_approvals(self):

        list_product_approvals_response = self.partner_center_sell_service.list_product_approvals(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert list_product_approvals_response.get_status_code() == 200
        list_product_approvals_response = list_product_approvals_response.get_result()
        assert list_product_approvals_response is not None

    @needscredentials
    def test_delete_product(self):

        delete_product_response = self.partner_center_sell_service.delete_product(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        )

        assert delete_product_response.get_status_code() == 200
        result = delete_product_response.get_result()
        assert result is not None

    @needscredentials
    def test_delete_plan(self):

        delete_plan_response = self.partner_center_sell_service.delete_plan(
            product_id='9fab83da-98cb-4f18-a7ba-b6f0435c9673',
            pricing_plan_id='testString'
        )

        assert delete_plan_response.get_status_code() == 200
        create_plan_response = delete_plan_response.get_result()
        assert create_plan_response is not None
