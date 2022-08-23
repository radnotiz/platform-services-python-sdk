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
Unit Tests for PartnerCenterSellV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_platform_services.partner_center_sell_v1 import *


_service = PartnerCenterSellV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://product-lifecycle.api.cloud.ibm.com/openapi/v1'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Products
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PartnerCenterSellV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerCenterSellV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerCenterSellV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListProducts():
    """
    Test Class for list_products
    """

    @responses.activate
    def test_list_products_all_params(self):
        """
        list_products()
        """
        # Set up mock
        url = preprocess_url('/products')
        mock_response = '{"errors": [{"message": "message", "extensions": {"code": "code", "serviceName": "service_name", "exception": {"anyKey": "anyValue"}, "trid": "trid", "operationName": "operation_name"}}], "products": [{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_products()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_products_all_params_with_retries(self):
        # Enable retries and run test_list_products_all_params.
        _service.enable_retries()
        self.test_list_products_all_params()

        # Disable retries and run test_list_products_all_params.
        _service.disable_retries()
        self.test_list_products_all_params()

class TestCreateProduct():
    """
    Test Class for create_product
    """

    @responses.activate
    def test_create_product_all_params(self):
        """
        create_product()
        """
        # Set up mock
        url = preprocess_url('/products')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_name = 'testString'
        tax_assessment = 'SOFTWARE'
        product_type = 'SOFTWARE'
        material_agreement = True

        # Invoke method
        response = _service.create_product(
            product_name,
            tax_assessment,
            product_type,
            material_agreement=material_agreement,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['productName'] == 'testString'
        assert req_body['taxAssessment'] == 'SOFTWARE'
        assert req_body['productType'] == 'SOFTWARE'
        assert req_body['materialAgreement'] == True

    def test_create_product_all_params_with_retries(self):
        # Enable retries and run test_create_product_all_params.
        _service.enable_retries()
        self.test_create_product_all_params()

        # Disable retries and run test_create_product_all_params.
        _service.disable_retries()
        self.test_create_product_all_params()

    @responses.activate
    def test_create_product_value_error(self):
        """
        test_create_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_name = 'testString'
        tax_assessment = 'SOFTWARE'
        product_type = 'SOFTWARE'
        material_agreement = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_name": product_name,
            "tax_assessment": tax_assessment,
            "product_type": product_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_product(**req_copy)

    def test_create_product_value_error_with_retries(self):
        # Enable retries and run test_create_product_value_error.
        _service.enable_retries()
        self.test_create_product_value_error()

        # Disable retries and run test_create_product_value_error.
        _service.disable_retries()
        self.test_create_product_value_error()

class TestGetProduct():
    """
    Test Class for get_product
    """

    @responses.activate
    def test_get_product_all_params(self):
        """
        get_product()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.get_product(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_product_all_params_with_retries(self):
        # Enable retries and run test_get_product_all_params.
        _service.enable_retries()
        self.test_get_product_all_params()

        # Disable retries and run test_get_product_all_params.
        _service.disable_retries()
        self.test_get_product_all_params()

    @responses.activate
    def test_get_product_value_error(self):
        """
        test_get_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_product(**req_copy)

    def test_get_product_value_error_with_retries(self):
        # Enable retries and run test_get_product_value_error.
        _service.enable_retries()
        self.test_get_product_value_error()

        # Disable retries and run test_get_product_value_error.
        _service.disable_retries()
        self.test_get_product_value_error()

class TestUpdateProduct():
    """
    Test Class for update_product
    """

    @responses.activate
    def test_update_product_all_params(self):
        """
        update_product()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        material_agreement = True
        product_name = 'testString'
        tax_assessment = 'SOFTWARE'

        # Invoke method
        response = _service.update_product(
            product_id,
            material_agreement=material_agreement,
            product_name=product_name,
            tax_assessment=tax_assessment,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['materialAgreement'] == True
        assert req_body['productName'] == 'testString'
        assert req_body['taxAssessment'] == 'SOFTWARE'

    def test_update_product_all_params_with_retries(self):
        # Enable retries and run test_update_product_all_params.
        _service.enable_retries()
        self.test_update_product_all_params()

        # Disable retries and run test_update_product_all_params.
        _service.disable_retries()
        self.test_update_product_all_params()

    @responses.activate
    def test_update_product_value_error(self):
        """
        test_update_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        material_agreement = True
        product_name = 'testString'
        tax_assessment = 'SOFTWARE'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_product(**req_copy)

    def test_update_product_value_error_with_retries(self):
        # Enable retries and run test_update_product_value_error.
        _service.enable_retries()
        self.test_update_product_value_error()

        # Disable retries and run test_update_product_value_error.
        _service.disable_retries()
        self.test_update_product_value_error()

class TestDeleteProduct():
    """
    Test Class for delete_product
    """

    @responses.activate
    def test_delete_product_all_params(self):
        """
        delete_product()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = 'true'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.delete_product(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_product_all_params_with_retries(self):
        # Enable retries and run test_delete_product_all_params.
        _service.enable_retries()
        self.test_delete_product_all_params()

        # Disable retries and run test_delete_product_all_params.
        _service.disable_retries()
        self.test_delete_product_all_params()

    @responses.activate
    def test_delete_product_value_error(self):
        """
        test_delete_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = 'true'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_product(**req_copy)

    def test_delete_product_value_error_with_retries(self):
        # Enable retries and run test_delete_product_value_error.
        _service.enable_retries()
        self.test_delete_product_value_error()

        # Disable retries and run test_delete_product_value_error.
        _service.disable_retries()
        self.test_delete_product_value_error()

class TestPublishProduct():
    """
    Test Class for publish_product
    """

    @responses.activate
    def test_publish_product_all_params(self):
        """
        publish_product()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/publish')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.publish_product(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_publish_product_all_params_with_retries(self):
        # Enable retries and run test_publish_product_all_params.
        _service.enable_retries()
        self.test_publish_product_all_params()

        # Disable retries and run test_publish_product_all_params.
        _service.disable_retries()
        self.test_publish_product_all_params()

    @responses.activate
    def test_publish_product_value_error(self):
        """
        test_publish_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/publish')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.publish_product(**req_copy)

    def test_publish_product_value_error_with_retries(self):
        # Enable retries and run test_publish_product_value_error.
        _service.enable_retries()
        self.test_publish_product_value_error()

        # Disable retries and run test_publish_product_value_error.
        _service.disable_retries()
        self.test_publish_product_value_error()

class TestSuspendProduct():
    """
    Test Class for suspend_product
    """

    @responses.activate
    def test_suspend_product_all_params(self):
        """
        suspend_product()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/suspend')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        reason = 'testString'

        # Invoke method
        response = _service.suspend_product(
            product_id,
            reason,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['reason'] == 'testString'

    def test_suspend_product_all_params_with_retries(self):
        # Enable retries and run test_suspend_product_all_params.
        _service.enable_retries()
        self.test_suspend_product_all_params()

        # Disable retries and run test_suspend_product_all_params.
        _service.disable_retries()
        self.test_suspend_product_all_params()

    @responses.activate
    def test_suspend_product_value_error(self):
        """
        test_suspend_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/suspend')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        reason = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "reason": reason,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.suspend_product(**req_copy)

    def test_suspend_product_value_error_with_retries(self):
        # Enable retries and run test_suspend_product_value_error.
        _service.enable_retries()
        self.test_suspend_product_value_error()

        # Disable retries and run test_suspend_product_value_error.
        _service.disable_retries()
        self.test_suspend_product_value_error()

class TestDeprecateProduct():
    """
    Test Class for deprecate_product
    """

    @responses.activate
    def test_deprecate_product_all_params(self):
        """
        deprecate_product()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/deprecate')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        reason = 'testString'

        # Invoke method
        response = _service.deprecate_product(
            product_id,
            reason,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['reason'] == 'testString'

    def test_deprecate_product_all_params_with_retries(self):
        # Enable retries and run test_deprecate_product_all_params.
        _service.enable_retries()
        self.test_deprecate_product_all_params()

        # Disable retries and run test_deprecate_product_all_params.
        _service.disable_retries()
        self.test_deprecate_product_all_params()

    @responses.activate
    def test_deprecate_product_value_error(self):
        """
        test_deprecate_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/deprecate')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        reason = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "reason": reason,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.deprecate_product(**req_copy)

    def test_deprecate_product_value_error_with_retries(self):
        # Enable retries and run test_deprecate_product_value_error.
        _service.enable_retries()
        self.test_deprecate_product_value_error()

        # Disable retries and run test_deprecate_product_value_error.
        _service.disable_retries()
        self.test_deprecate_product_value_error()

class TestRestoreProduct():
    """
    Test Class for restore_product
    """

    @responses.activate
    def test_restore_product_all_params(self):
        """
        restore_product()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/restore')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        reason = 'testString'

        # Invoke method
        response = _service.restore_product(
            product_id,
            reason,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['reason'] == 'testString'

    def test_restore_product_all_params_with_retries(self):
        # Enable retries and run test_restore_product_all_params.
        _service.enable_retries()
        self.test_restore_product_all_params()

        # Disable retries and run test_restore_product_all_params.
        _service.disable_retries()
        self.test_restore_product_all_params()

    @responses.activate
    def test_restore_product_value_error(self):
        """
        test_restore_product_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/restore')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        reason = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "reason": reason,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.restore_product(**req_copy)

    def test_restore_product_value_error_with_retries(self):
        # Enable retries and run test_restore_product_value_error.
        _service.enable_retries()
        self.test_restore_product_value_error()

        # Disable retries and run test_restore_product_value_error.
        _service.disable_retries()
        self.test_restore_product_value_error()

class TestListBadges():
    """
    Test Class for list_badges
    """

    @responses.activate
    def test_list_badges_all_params(self):
        """
        list_badges()
        """
        # Set up mock
        url = preprocess_url('/products/badges')
        mock_response = '{"id": "id", "label": "label", "description": "description", "learnMoreLinks": {"firstParty": "first_party", "thirdParty": "third_party"}, "getStartedLink": "get_started_link", "tag": "tag"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_badges()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_badges_all_params_with_retries(self):
        # Enable retries and run test_list_badges_all_params.
        _service.enable_retries()
        self.test_list_badges_all_params()

        # Disable retries and run test_list_badges_all_params.
        _service.disable_retries()
        self.test_list_badges_all_params()

class TestGetBadge():
    """
    Test Class for get_badge
    """

    @responses.activate
    def test_get_badge_all_params(self):
        """
        get_badge()
        """
        # Set up mock
        url = preprocess_url('/products/badges/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = '{"id": "id", "label": "label", "description": "description", "learnMoreLinks": {"firstParty": "first_party", "thirdParty": "third_party"}, "getStartedLink": "get_started_link", "tag": "tag"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        badge_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.get_badge(
            badge_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_badge_all_params_with_retries(self):
        # Enable retries and run test_get_badge_all_params.
        _service.enable_retries()
        self.test_get_badge_all_params()

        # Disable retries and run test_get_badge_all_params.
        _service.disable_retries()
        self.test_get_badge_all_params()

    @responses.activate
    def test_get_badge_value_error(self):
        """
        test_get_badge_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/badges/9fab83da-98cb-4f18-a7ba-b6f0435c9673')
        mock_response = '{"id": "id", "label": "label", "description": "description", "learnMoreLinks": {"firstParty": "first_party", "thirdParty": "third_party"}, "getStartedLink": "get_started_link", "tag": "tag"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        badge_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "badge_id": badge_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_badge(**req_copy)

    def test_get_badge_value_error_with_retries(self):
        # Enable retries and run test_get_badge_value_error.
        _service.enable_retries()
        self.test_get_badge_value_error()

        # Disable retries and run test_get_badge_value_error.
        _service.disable_retries()
        self.test_get_badge_value_error()

# endregion
##############################################################################
# End of Service: Products
##############################################################################

##############################################################################
# Start of Service: Catalog
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PartnerCenterSellV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerCenterSellV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerCenterSellV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetCatalog():
    """
    Test Class for get_catalog
    """

    @responses.activate
    def test_get_catalog_all_params(self):
        """
        get_catalog()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/catalog')
        mock_response = '{"accountId": "account_id", "catalogId": "catalog_id", "deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "description": "description", "documentationUrl": "documentation_url", "editable": true, "highlights": [{"description": "description", "description_i18n": {"anyKey": "anyValue"}, "title": "title", "title_i18n": {"anyKey": "anyValue"}}], "iconUrl": "icon_url", "id": "id", "keywords": ["keywords"], "label": "label", "label_i18n": {"anyKey": "anyValue"}, "longDescription": "long_description", "long_description_i18n": {"anyKey": "anyValue"}, "media": [{"caption": "caption", "caption_i18n": {"anyKey": "anyValue"}, "thumbnail": "thumbnail", "type": "image", "url": "url"}], "name": "name", "pcManaged": true, "provider": "provider", "publishedToAccessList": true, "publishedToIBM": true, "publishedToPublic": false, "short_description_i18n": {"anyKey": "anyValue"}, "tags": ["tags"], "versions": [{"deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "id": "id", "kindFormat": "Helm chart", "kindId": "kind_id", "kindTarget": "iks", "packageVersion": "package_version", "state": "deprecated", "stateChangeTime": "state_change_time", "validatedState": "validated_state", "version": "version", "versionLocator": "version_locator", "allowlistedAccounts": ["allowlisted_accounts"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.get_catalog(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_catalog_all_params_with_retries(self):
        # Enable retries and run test_get_catalog_all_params.
        _service.enable_retries()
        self.test_get_catalog_all_params()

        # Disable retries and run test_get_catalog_all_params.
        _service.disable_retries()
        self.test_get_catalog_all_params()

    @responses.activate
    def test_get_catalog_value_error(self):
        """
        test_get_catalog_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/catalog')
        mock_response = '{"accountId": "account_id", "catalogId": "catalog_id", "deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "description": "description", "documentationUrl": "documentation_url", "editable": true, "highlights": [{"description": "description", "description_i18n": {"anyKey": "anyValue"}, "title": "title", "title_i18n": {"anyKey": "anyValue"}}], "iconUrl": "icon_url", "id": "id", "keywords": ["keywords"], "label": "label", "label_i18n": {"anyKey": "anyValue"}, "longDescription": "long_description", "long_description_i18n": {"anyKey": "anyValue"}, "media": [{"caption": "caption", "caption_i18n": {"anyKey": "anyValue"}, "thumbnail": "thumbnail", "type": "image", "url": "url"}], "name": "name", "pcManaged": true, "provider": "provider", "publishedToAccessList": true, "publishedToIBM": true, "publishedToPublic": false, "short_description_i18n": {"anyKey": "anyValue"}, "tags": ["tags"], "versions": [{"deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "id": "id", "kindFormat": "Helm chart", "kindId": "kind_id", "kindTarget": "iks", "packageVersion": "package_version", "state": "deprecated", "stateChangeTime": "state_change_time", "validatedState": "validated_state", "version": "version", "versionLocator": "version_locator", "allowlistedAccounts": ["allowlisted_accounts"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_catalog(**req_copy)

    def test_get_catalog_value_error_with_retries(self):
        # Enable retries and run test_get_catalog_value_error.
        _service.enable_retries()
        self.test_get_catalog_value_error()

        # Disable retries and run test_get_catalog_value_error.
        _service.disable_retries()
        self.test_get_catalog_value_error()

class TestUpdateCatalog():
    """
    Test Class for update_catalog
    """

    @responses.activate
    def test_update_catalog_all_params(self):
        """
        update_catalog()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/catalog')
        mock_response = '{"accountId": "account_id", "catalogId": "catalog_id", "deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "description": "description", "documentationUrl": "documentation_url", "editable": true, "highlights": [{"description": "description", "description_i18n": {"anyKey": "anyValue"}, "title": "title", "title_i18n": {"anyKey": "anyValue"}}], "iconUrl": "icon_url", "id": "id", "keywords": ["keywords"], "label": "label", "label_i18n": {"anyKey": "anyValue"}, "longDescription": "long_description", "long_description_i18n": {"anyKey": "anyValue"}, "media": [{"caption": "caption", "caption_i18n": {"anyKey": "anyValue"}, "thumbnail": "thumbnail", "type": "image", "url": "url"}], "name": "name", "pcManaged": true, "provider": "provider", "publishedToAccessList": true, "publishedToIBM": true, "publishedToPublic": false, "short_description_i18n": {"anyKey": "anyValue"}, "tags": ["tags"], "versions": [{"deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "id": "id", "kindFormat": "Helm chart", "kindId": "kind_id", "kindTarget": "iks", "packageVersion": "package_version", "state": "deprecated", "stateChangeTime": "state_change_time", "validatedState": "validated_state", "version": "version", "versionLocator": "version_locator", "allowlistedAccounts": ["allowlisted_accounts"]}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HighlightSectionInput model
        highlight_section_input_model = {}
        highlight_section_input_model['description'] = 'testString'
        highlight_section_input_model['title'] = 'testString'

        # Construct a dict representation of a MediaSectionInput model
        media_section_input_model = {}
        media_section_input_model['caption'] = 'testString'
        media_section_input_model['thumbnail'] = 'testString'
        media_section_input_model['type'] = 'image'
        media_section_input_model['url'] = 'testString'

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        catalog_id = 'testString'
        description = 'testString'
        icon_url = 'testString'
        keywords = ['testString']
        pricing_model = 'free'
        category = 'testString'
        provider_type = ['ibm_community']
        label = 'testString'
        name = 'testString'
        provider = 'testString'
        tags = ['testString']
        documentation_url = 'testString'
        highlights = [highlight_section_input_model]
        long_description = 'testString'
        media = [media_section_input_model]

        # Invoke method
        response = _service.update_catalog(
            product_id,
            catalog_id=catalog_id,
            description=description,
            icon_url=icon_url,
            keywords=keywords,
            pricing_model=pricing_model,
            category=category,
            provider_type=provider_type,
            label=label,
            name=name,
            provider=provider,
            tags=tags,
            documentation_url=documentation_url,
            highlights=highlights,
            long_description=long_description,
            media=media,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['catalogId'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['iconUrl'] == 'testString'
        assert req_body['keywords'] == ['testString']
        assert req_body['pricingModel'] == 'free'
        assert req_body['category'] == 'testString'
        assert req_body['providerType'] == ['ibm_community']
        assert req_body['label'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['provider'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['documentationUrl'] == 'testString'
        assert req_body['highlights'] == [highlight_section_input_model]
        assert req_body['longDescription'] == 'testString'
        assert req_body['media'] == [media_section_input_model]

    def test_update_catalog_all_params_with_retries(self):
        # Enable retries and run test_update_catalog_all_params.
        _service.enable_retries()
        self.test_update_catalog_all_params()

        # Disable retries and run test_update_catalog_all_params.
        _service.disable_retries()
        self.test_update_catalog_all_params()

    @responses.activate
    def test_update_catalog_value_error(self):
        """
        test_update_catalog_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/catalog')
        mock_response = '{"accountId": "account_id", "catalogId": "catalog_id", "deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "description": "description", "documentationUrl": "documentation_url", "editable": true, "highlights": [{"description": "description", "description_i18n": {"anyKey": "anyValue"}, "title": "title", "title_i18n": {"anyKey": "anyValue"}}], "iconUrl": "icon_url", "id": "id", "keywords": ["keywords"], "label": "label", "label_i18n": {"anyKey": "anyValue"}, "longDescription": "long_description", "long_description_i18n": {"anyKey": "anyValue"}, "media": [{"caption": "caption", "caption_i18n": {"anyKey": "anyValue"}, "thumbnail": "thumbnail", "type": "image", "url": "url"}], "name": "name", "pcManaged": true, "provider": "provider", "publishedToAccessList": true, "publishedToIBM": true, "publishedToPublic": false, "short_description_i18n": {"anyKey": "anyValue"}, "tags": ["tags"], "versions": [{"deprecatePending": {"deprecateDate": "deprecate_date", "deprecateState": "deprecate_state", "description": "description"}, "id": "id", "kindFormat": "Helm chart", "kindId": "kind_id", "kindTarget": "iks", "packageVersion": "package_version", "state": "deprecated", "stateChangeTime": "state_change_time", "validatedState": "validated_state", "version": "version", "versionLocator": "version_locator", "allowlistedAccounts": ["allowlisted_accounts"]}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HighlightSectionInput model
        highlight_section_input_model = {}
        highlight_section_input_model['description'] = 'testString'
        highlight_section_input_model['title'] = 'testString'

        # Construct a dict representation of a MediaSectionInput model
        media_section_input_model = {}
        media_section_input_model['caption'] = 'testString'
        media_section_input_model['thumbnail'] = 'testString'
        media_section_input_model['type'] = 'image'
        media_section_input_model['url'] = 'testString'

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        catalog_id = 'testString'
        description = 'testString'
        icon_url = 'testString'
        keywords = ['testString']
        pricing_model = 'free'
        category = 'testString'
        provider_type = ['ibm_community']
        label = 'testString'
        name = 'testString'
        provider = 'testString'
        tags = ['testString']
        documentation_url = 'testString'
        highlights = [highlight_section_input_model]
        long_description = 'testString'
        media = [media_section_input_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_catalog(**req_copy)

    def test_update_catalog_value_error_with_retries(self):
        # Enable retries and run test_update_catalog_value_error.
        _service.enable_retries()
        self.test_update_catalog_value_error()

        # Disable retries and run test_update_catalog_value_error.
        _service.disable_retries()
        self.test_update_catalog_value_error()

class TestRequestCatalogApproval():
    """
    Test Class for request_catalog_approval
    """

    @responses.activate
    def test_request_catalog_approval_all_params(self):
        """
        request_catalog_approval()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/catalog/approvals')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.request_catalog_approval(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_request_catalog_approval_all_params_with_retries(self):
        # Enable retries and run test_request_catalog_approval_all_params.
        _service.enable_retries()
        self.test_request_catalog_approval_all_params()

        # Disable retries and run test_request_catalog_approval_all_params.
        _service.disable_retries()
        self.test_request_catalog_approval_all_params()

    @responses.activate
    def test_request_catalog_approval_value_error(self):
        """
        test_request_catalog_approval_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/catalog/approvals')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.request_catalog_approval(**req_copy)

    def test_request_catalog_approval_value_error_with_retries(self):
        # Enable retries and run test_request_catalog_approval_value_error.
        _service.enable_retries()
        self.test_request_catalog_approval_value_error()

        # Disable retries and run test_request_catalog_approval_value_error.
        _service.disable_retries()
        self.test_request_catalog_approval_value_error()

# endregion
##############################################################################
# End of Service: Catalog
##############################################################################

##############################################################################
# Start of Service: Pricing
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PartnerCenterSellV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerCenterSellV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerCenterSellV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListPlans():
    """
    Test Class for list_plans
    """

    @responses.activate
    def test_list_plans_all_params(self):
        """
        list_plans()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.list_plans(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_plans_all_params_with_retries(self):
        # Enable retries and run test_list_plans_all_params.
        _service.enable_retries()
        self.test_list_plans_all_params()

        # Disable retries and run test_list_plans_all_params.
        _service.disable_retries()
        self.test_list_plans_all_params()

    @responses.activate
    def test_list_plans_value_error(self):
        """
        test_list_plans_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_plans(**req_copy)

    def test_list_plans_value_error_with_retries(self):
        # Enable retries and run test_list_plans_value_error.
        _service.enable_retries()
        self.test_list_plans_value_error()

        # Disable retries and run test_list_plans_value_error.
        _service.disable_retries()
        self.test_list_plans_value_error()

class TestCreatePlan():
    """
    Test Class for create_plan
    """

    @responses.activate
    def test_create_plan_all_params(self):
        """
        create_plan()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        description = 'testString'
        label = 'testString'
        type = 'byol'
        url = 'testString'

        # Invoke method
        response = _service.create_plan(
            product_id,
            description,
            label,
            type,
            url,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['type'] == 'byol'
        assert req_body['url'] == 'testString'

    def test_create_plan_all_params_with_retries(self):
        # Enable retries and run test_create_plan_all_params.
        _service.enable_retries()
        self.test_create_plan_all_params()

        # Disable retries and run test_create_plan_all_params.
        _service.disable_retries()
        self.test_create_plan_all_params()

    @responses.activate
    def test_create_plan_value_error(self):
        """
        test_create_plan_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        description = 'testString'
        label = 'testString'
        type = 'byol'
        url = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "description": description,
            "label": label,
            "type": type,
            "url": url,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_plan(**req_copy)

    def test_create_plan_value_error_with_retries(self):
        # Enable retries and run test_create_plan_value_error.
        _service.enable_retries()
        self.test_create_plan_value_error()

        # Disable retries and run test_create_plan_value_error.
        _service.disable_retries()
        self.test_create_plan_value_error()

class TestGetPlan():
    """
    Test Class for get_plan
    """

    @responses.activate
    def test_get_plan_all_params(self):
        """
        get_plan()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans/testString')
        mock_response = '{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        pricing_plan_id = 'testString'

        # Invoke method
        response = _service.get_plan(
            product_id,
            pricing_plan_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_plan_all_params_with_retries(self):
        # Enable retries and run test_get_plan_all_params.
        _service.enable_retries()
        self.test_get_plan_all_params()

        # Disable retries and run test_get_plan_all_params.
        _service.disable_retries()
        self.test_get_plan_all_params()

    @responses.activate
    def test_get_plan_value_error(self):
        """
        test_get_plan_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans/testString')
        mock_response = '{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        pricing_plan_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "pricing_plan_id": pricing_plan_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_plan(**req_copy)

    def test_get_plan_value_error_with_retries(self):
        # Enable retries and run test_get_plan_value_error.
        _service.enable_retries()
        self.test_get_plan_value_error()

        # Disable retries and run test_get_plan_value_error.
        _service.disable_retries()
        self.test_get_plan_value_error()

class TestUpdatePlan():
    """
    Test Class for update_plan
    """

    @responses.activate
    def test_update_plan_all_params(self):
        """
        update_plan()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans/testString')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        pricing_plan_id = 'testString'
        description = 'testString'
        label = 'testString'
        type = 'byol'
        url = 'testString'

        # Invoke method
        response = _service.update_plan(
            product_id,
            pricing_plan_id,
            description,
            label,
            type,
            url,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'
        assert req_body['label'] == 'testString'
        assert req_body['type'] == 'byol'
        assert req_body['url'] == 'testString'

    def test_update_plan_all_params_with_retries(self):
        # Enable retries and run test_update_plan_all_params.
        _service.enable_retries()
        self.test_update_plan_all_params()

        # Disable retries and run test_update_plan_all_params.
        _service.disable_retries()
        self.test_update_plan_all_params()

    @responses.activate
    def test_update_plan_value_error(self):
        """
        test_update_plan_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans/testString')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        pricing_plan_id = 'testString'
        description = 'testString'
        label = 'testString'
        type = 'byol'
        url = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "pricing_plan_id": pricing_plan_id,
            "description": description,
            "label": label,
            "type": type,
            "url": url,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_plan(**req_copy)

    def test_update_plan_value_error_with_retries(self):
        # Enable retries and run test_update_plan_value_error.
        _service.enable_retries()
        self.test_update_plan_value_error()

        # Disable retries and run test_update_plan_value_error.
        _service.disable_retries()
        self.test_update_plan_value_error()

class TestDeletePlan():
    """
    Test Class for delete_plan
    """

    @responses.activate
    def test_delete_plan_all_params(self):
        """
        delete_plan()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans/testString')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        pricing_plan_id = 'testString'

        # Invoke method
        response = _service.delete_plan(
            product_id,
            pricing_plan_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_plan_all_params_with_retries(self):
        # Enable retries and run test_delete_plan_all_params.
        _service.enable_retries()
        self.test_delete_plan_all_params()

        # Disable retries and run test_delete_plan_all_params.
        _service.disable_retries()
        self.test_delete_plan_all_params()

    @responses.activate
    def test_delete_plan_value_error(self):
        """
        test_delete_plan_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/plans/testString')
        mock_response = '{"plans": [{"description": "description", "id": "id", "label": "label", "type": "byol", "url": "url"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        pricing_plan_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "pricing_plan_id": pricing_plan_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_plan(**req_copy)

    def test_delete_plan_value_error_with_retries(self):
        # Enable retries and run test_delete_plan_value_error.
        _service.enable_retries()
        self.test_delete_plan_value_error()

        # Disable retries and run test_delete_plan_value_error.
        _service.disable_retries()
        self.test_delete_plan_value_error()

# endregion
##############################################################################
# End of Service: Pricing
##############################################################################

##############################################################################
# Start of Service: Support
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PartnerCenterSellV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerCenterSellV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerCenterSellV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetSupport():
    """
    Test Class for get_support
    """

    @responses.activate
    def test_get_support_all_params(self):
        """
        get_support()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support')
        mock_response = '{"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.get_support(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_support_all_params_with_retries(self):
        # Enable retries and run test_get_support_all_params.
        _service.enable_retries()
        self.test_get_support_all_params()

        # Disable retries and run test_get_support_all_params.
        _service.disable_retries()
        self.test_get_support_all_params()

    @responses.activate
    def test_get_support_value_error(self):
        """
        test_get_support_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support')
        mock_response = '{"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_support(**req_copy)

    def test_get_support_value_error_with_retries(self):
        # Enable retries and run test_get_support_value_error.
        _service.enable_retries()
        self.test_get_support_value_error()

        # Disable retries and run test_get_support_value_error.
        _service.disable_retries()
        self.test_get_support_value_error()

class TestUpdateSupport():
    """
    Test Class for update_support
    """

    @responses.activate
    def test_update_support_all_params(self):
        """
        update_support()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support')
        mock_response = '{"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a EscalationContactsUpdate model
        escalation_contacts_update_model = {}
        escalation_contacts_update_model['email'] = 'testString'
        escalation_contacts_update_model['name'] = 'testString'

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {}
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {}
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {}
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a dict representation of a SupportDetails model
        support_details_model = {}
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {}
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {}
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        escalation_contacts = [escalation_contacts_update_model]
        locations = ['US']
        support_details = [support_details_model]
        support_escalation = support_escalation_model
        support_type = 'third-party'
        url = 'https://my-company.com/support'

        # Invoke method
        response = _service.update_support(
            product_id,
            escalation_contacts=escalation_contacts,
            locations=locations,
            support_details=support_details,
            support_escalation=support_escalation,
            support_type=support_type,
            url=url,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['escalationContacts'] == [escalation_contacts_update_model]
        assert req_body['locations'] == ['US']
        assert req_body['support_details'] == [support_details_model]
        assert req_body['support_escalation'] == support_escalation_model
        assert req_body['support_type'] == 'third-party'
        assert req_body['url'] == 'https://my-company.com/support'

    def test_update_support_all_params_with_retries(self):
        # Enable retries and run test_update_support_all_params.
        _service.enable_retries()
        self.test_update_support_all_params()

        # Disable retries and run test_update_support_all_params.
        _service.disable_retries()
        self.test_update_support_all_params()

    @responses.activate
    def test_update_support_value_error(self):
        """
        test_update_support_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support')
        mock_response = '{"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a EscalationContactsUpdate model
        escalation_contacts_update_model = {}
        escalation_contacts_update_model['email'] = 'testString'
        escalation_contacts_update_model['name'] = 'testString'

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {}
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {}
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {}
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a dict representation of a SupportDetails model
        support_details_model = {}
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {}
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {}
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        escalation_contacts = [escalation_contacts_update_model]
        locations = ['US']
        support_details = [support_details_model]
        support_escalation = support_escalation_model
        support_type = 'third-party'
        url = 'https://my-company.com/support'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_support(**req_copy)

    def test_update_support_value_error_with_retries(self):
        # Enable retries and run test_update_support_value_error.
        _service.enable_retries()
        self.test_update_support_value_error()

        # Disable retries and run test_update_support_value_error.
        _service.disable_retries()
        self.test_update_support_value_error()

class TestListSupportChangeRequests():
    """
    Test Class for list_support_change_requests
    """

    @responses.activate
    def test_list_support_change_requests_all_params(self):
        """
        list_support_change_requests()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes')
        mock_response = '{"changes": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.list_support_change_requests(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_support_change_requests_all_params_with_retries(self):
        # Enable retries and run test_list_support_change_requests_all_params.
        _service.enable_retries()
        self.test_list_support_change_requests_all_params()

        # Disable retries and run test_list_support_change_requests_all_params.
        _service.disable_retries()
        self.test_list_support_change_requests_all_params()

    @responses.activate
    def test_list_support_change_requests_value_error(self):
        """
        test_list_support_change_requests_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes')
        mock_response = '{"changes": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_support_change_requests(**req_copy)

    def test_list_support_change_requests_value_error_with_retries(self):
        # Enable retries and run test_list_support_change_requests_value_error.
        _service.enable_retries()
        self.test_list_support_change_requests_value_error()

        # Disable retries and run test_list_support_change_requests_value_error.
        _service.disable_retries()
        self.test_list_support_change_requests_value_error()

class TestCreateSupportChangeRequest():
    """
    Test Class for create_support_change_request
    """

    @responses.activate
    def test_create_support_change_request_all_params(self):
        """
        create_support_change_request()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {}
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {}
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {}
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a dict representation of a SupportDetails model
        support_details_model = {}
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {}
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {}
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        # Construct a dict representation of a Support model
        support_model = {}
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change = support_model

        # Invoke method
        response = _service.create_support_change_request(
            product_id,
            change,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['change'] == support_model

    def test_create_support_change_request_all_params_with_retries(self):
        # Enable retries and run test_create_support_change_request_all_params.
        _service.enable_retries()
        self.test_create_support_change_request_all_params()

        # Disable retries and run test_create_support_change_request_all_params.
        _service.disable_retries()
        self.test_create_support_change_request_all_params()

    @responses.activate
    def test_create_support_change_request_value_error(self):
        """
        test_create_support_change_request_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {}
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {}
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {}
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a dict representation of a SupportDetails model
        support_details_model = {}
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {}
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {}
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        # Construct a dict representation of a Support model
        support_model = {}
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change = support_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "change": change,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_support_change_request(**req_copy)

    def test_create_support_change_request_value_error_with_retries(self):
        # Enable retries and run test_create_support_change_request_value_error.
        _service.enable_retries()
        self.test_create_support_change_request_value_error()

        # Disable retries and run test_create_support_change_request_value_error.
        _service.disable_retries()
        self.test_create_support_change_request_value_error()

class TestGetSupportChangeRequest():
    """
    Test Class for get_support_change_request
    """

    @responses.activate
    def test_get_support_change_request_all_params(self):
        """
        get_support_change_request()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString')
        mock_response = '{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Invoke method
        response = _service.get_support_change_request(
            product_id,
            change_request_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_support_change_request_all_params_with_retries(self):
        # Enable retries and run test_get_support_change_request_all_params.
        _service.enable_retries()
        self.test_get_support_change_request_all_params()

        # Disable retries and run test_get_support_change_request_all_params.
        _service.disable_retries()
        self.test_get_support_change_request_all_params()

    @responses.activate
    def test_get_support_change_request_value_error(self):
        """
        test_get_support_change_request_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString')
        mock_response = '{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "change_request_id": change_request_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_support_change_request(**req_copy)

    def test_get_support_change_request_value_error_with_retries(self):
        # Enable retries and run test_get_support_change_request_value_error.
        _service.enable_retries()
        self.test_get_support_change_request_value_error()

        # Disable retries and run test_get_support_change_request_value_error.
        _service.disable_retries()
        self.test_get_support_change_request_value_error()

class TestUpdateSupportChangeRequest():
    """
    Test Class for update_support_change_request
    """

    @responses.activate
    def test_update_support_change_request_all_params(self):
        """
        update_support_change_request()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {}
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {}
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {}
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a dict representation of a SupportDetails model
        support_details_model = {}
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {}
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {}
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        # Construct a dict representation of a Support model
        support_model = {}
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'
        change = support_model

        # Invoke method
        response = _service.update_support_change_request(
            product_id,
            change_request_id,
            change,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['change'] == support_model

    def test_update_support_change_request_all_params_with_retries(self):
        # Enable retries and run test_update_support_change_request_all_params.
        _service.enable_retries()
        self.test_update_support_change_request_all_params()

        # Disable retries and run test_update_support_change_request_all_params.
        _service.disable_retries()
        self.test_update_support_change_request_all_params()

    @responses.activate
    def test_update_support_change_request_value_error(self):
        """
        test_update_support_change_request_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model = {}
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        # Construct a dict representation of a SupportDetailsAvailability model
        support_details_availability_model = {}
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        # Construct a dict representation of a SupportResponseTimes model
        support_response_times_model = {}
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a dict representation of a SupportDetails model
        support_details_model = {}
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        # Construct a dict representation of a SupportEscalationTimes model
        support_escalation_times_model = {}
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        # Construct a dict representation of a SupportEscalation model
        support_escalation_model = {}
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        # Construct a dict representation of a Support model
        support_model = {}
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'
        change = support_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "change_request_id": change_request_id,
            "change": change,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_support_change_request(**req_copy)

    def test_update_support_change_request_value_error_with_retries(self):
        # Enable retries and run test_update_support_change_request_value_error.
        _service.enable_retries()
        self.test_update_support_change_request_value_error()

        # Disable retries and run test_update_support_change_request_value_error.
        _service.disable_retries()
        self.test_update_support_change_request_value_error()

class TestListSupportChangeRequestReviews():
    """
    Test Class for list_support_change_request_reviews
    """

    @responses.activate
    def test_list_support_change_request_reviews_all_params(self):
        """
        list_support_change_request_reviews()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString/reviews')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Invoke method
        response = _service.list_support_change_request_reviews(
            product_id,
            change_request_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_support_change_request_reviews_all_params_with_retries(self):
        # Enable retries and run test_list_support_change_request_reviews_all_params.
        _service.enable_retries()
        self.test_list_support_change_request_reviews_all_params()

        # Disable retries and run test_list_support_change_request_reviews_all_params.
        _service.disable_retries()
        self.test_list_support_change_request_reviews_all_params()

    @responses.activate
    def test_list_support_change_request_reviews_value_error(self):
        """
        test_list_support_change_request_reviews_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString/reviews')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "change_request_id": change_request_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_support_change_request_reviews(**req_copy)

    def test_list_support_change_request_reviews_value_error_with_retries(self):
        # Enable retries and run test_list_support_change_request_reviews_value_error.
        _service.enable_retries()
        self.test_list_support_change_request_reviews_value_error()

        # Disable retries and run test_list_support_change_request_reviews_value_error.
        _service.disable_retries()
        self.test_list_support_change_request_reviews_value_error()

class TestRequestSupportChangeRequestReview():
    """
    Test Class for request_support_change_request_review
    """

    @responses.activate
    def test_request_support_change_request_review_all_params(self):
        """
        request_support_change_request_review()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString/reviews')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Invoke method
        response = _service.request_support_change_request_review(
            product_id,
            change_request_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_request_support_change_request_review_all_params_with_retries(self):
        # Enable retries and run test_request_support_change_request_review_all_params.
        _service.enable_retries()
        self.test_request_support_change_request_review_all_params()

        # Disable retries and run test_request_support_change_request_review_all_params.
        _service.disable_retries()
        self.test_request_support_change_request_review_all_params()

    @responses.activate
    def test_request_support_change_request_review_value_error(self):
        """
        test_request_support_change_request_review_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString/reviews')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "change_request_id": change_request_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.request_support_change_request_review(**req_copy)

    def test_request_support_change_request_review_value_error_with_retries(self):
        # Enable retries and run test_request_support_change_request_review_value_error.
        _service.enable_retries()
        self.test_request_support_change_request_review_value_error()

        # Disable retries and run test_request_support_change_request_review_value_error.
        _service.disable_retries()
        self.test_request_support_change_request_review_value_error()

class TestMergeSupportChangeRequest():
    """
    Test Class for merge_support_change_request
    """

    @responses.activate
    def test_merge_support_change_request_all_params(self):
        """
        merge_support_change_request()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString/merge')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Invoke method
        response = _service.merge_support_change_request(
            product_id,
            change_request_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_merge_support_change_request_all_params_with_retries(self):
        # Enable retries and run test_merge_support_change_request_all_params.
        _service.enable_retries()
        self.test_merge_support_change_request_all_params()

        # Disable retries and run test_merge_support_change_request_all_params.
        _service.disable_retries()
        self.test_merge_support_change_request_all_params()

    @responses.activate
    def test_merge_support_change_request_value_error(self):
        """
        test_merge_support_change_request_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/changes/testString/merge')
        mock_response = '{"accountId": "account_id", "createdAt": "created_at", "id": "id", "materialAgreement": true, "productType": "SOFTWARE", "productName": "product_name", "publishedAt": "published_at", "taxAssessment": "SOFTWARE", "updatedAt": "updated_at", "changeRequests": [{"id": "id", "createdAt": "created_at", "initiator": "initiator", "merged": "merged", "change": {"locations": ["US"], "process": "process", "process_i18n": {"anyKey": "anyValue"}, "support_details": [{"availability": {"always_available": true, "times": [{"day": 1, "end_time": "19:30", "start_time": "10:30"}], "timezone": "America/Los_Angeles"}, "contact": "contact", "response_wait_time": {"type": "hour", "value": 2}, "type": "email"}], "support_escalation": {"contact": "contact", "escalation_wait_time": {"type": "hour", "value": 2}, "response_wait_time": {"type": "hour", "value": 2}}, "support_type": "third-party", "url": "https://my-company.com/support"}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        change_request_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
            "change_request_id": change_request_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.merge_support_change_request(**req_copy)

    def test_merge_support_change_request_value_error_with_retries(self):
        # Enable retries and run test_merge_support_change_request_value_error.
        _service.enable_retries()
        self.test_merge_support_change_request_value_error()

        # Disable retries and run test_merge_support_change_request_value_error.
        _service.disable_retries()
        self.test_merge_support_change_request_value_error()

class TestRequestSupportApproval():
    """
    Test Class for request_support_approval
    """

    @responses.activate
    def test_request_support_approval_all_params(self):
        """
        request_support_approval()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/approvals')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.request_support_approval(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_request_support_approval_all_params_with_retries(self):
        # Enable retries and run test_request_support_approval_all_params.
        _service.enable_retries()
        self.test_request_support_approval_all_params()

        # Disable retries and run test_request_support_approval_all_params.
        _service.disable_retries()
        self.test_request_support_approval_all_params()

    @responses.activate
    def test_request_support_approval_value_error(self):
        """
        test_request_support_approval_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/support/approvals')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.request_support_approval(**req_copy)

    def test_request_support_approval_value_error_with_retries(self):
        # Enable retries and run test_request_support_approval_value_error.
        _service.enable_retries()
        self.test_request_support_approval_value_error()

        # Disable retries and run test_request_support_approval_value_error.
        _service.disable_retries()
        self.test_request_support_approval_value_error()

# endregion
##############################################################################
# End of Service: Support
##############################################################################

##############################################################################
# Start of Service: Approval
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PartnerCenterSellV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PartnerCenterSellV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PartnerCenterSellV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestRequestProductApproval():
    """
    Test Class for request_product_approval
    """

    @responses.activate
    def test_request_product_approval_all_params(self):
        """
        request_product_approval()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/approvals')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.request_product_approval(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_request_product_approval_all_params_with_retries(self):
        # Enable retries and run test_request_product_approval_all_params.
        _service.enable_retries()
        self.test_request_product_approval_all_params()

        # Disable retries and run test_request_product_approval_all_params.
        _service.disable_retries()
        self.test_request_product_approval_all_params()

    @responses.activate
    def test_request_product_approval_value_error(self):
        """
        test_request_product_approval_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/approvals')
        mock_response = '{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.request_product_approval(**req_copy)

    def test_request_product_approval_value_error_with_retries(self):
        # Enable retries and run test_request_product_approval_value_error.
        _service.enable_retries()
        self.test_request_product_approval_value_error()

        # Disable retries and run test_request_product_approval_value_error.
        _service.disable_retries()
        self.test_request_product_approval_value_error()

class TestListProductApprovals():
    """
    Test Class for list_product_approvals
    """

    @responses.activate
    def test_list_product_approvals_all_params(self):
        """
        list_product_approvals()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/approvals')
        mock_response = '{"approvals": [{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Invoke method
        response = _service.list_product_approvals(
            product_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_product_approvals_all_params_with_retries(self):
        # Enable retries and run test_list_product_approvals_all_params.
        _service.enable_retries()
        self.test_list_product_approvals_all_params()

        # Disable retries and run test_list_product_approvals_all_params.
        _service.disable_retries()
        self.test_list_product_approvals_all_params()

    @responses.activate
    def test_list_product_approvals_value_error(self):
        """
        test_list_product_approvals_value_error()
        """
        # Set up mock
        url = preprocess_url('/products/9fab83da-98cb-4f18-a7ba-b6f0435c9673/approvals')
        mock_response = '{"approvals": [{"history": [{"at": "at", "displayName": "display_name", "event": "event", "reason": "reason", "username": "username"}], "id": "id", "nextEvents": ["next_events"], "state": {"name": "waitingForRequestForReview"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        product_id = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "product_id": product_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_product_approvals(**req_copy)

    def test_list_product_approvals_value_error_with_retries(self):
        # Enable retries and run test_list_product_approvals_value_error.
        _service.enable_retries()
        self.test_list_product_approvals_value_error()

        # Disable retries and run test_list_product_approvals_value_error.
        _service.disable_retries()
        self.test_list_product_approvals_value_error()

# endregion
##############################################################################
# End of Service: Approval
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_CatalogListingDetails():
    """
    Test Class for CatalogListingDetails
    """

    def test_catalog_listing_details_serialization(self):
        """
        Test serialization/deserialization for CatalogListingDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deprecate_pending_model = {} # DeprecatePending
        deprecate_pending_model['deprecateDate'] = 'testString'
        deprecate_pending_model['deprecateState'] = 'testString'
        deprecate_pending_model['description'] = 'testString'

        highlight_section_model = {} # HighlightSection
        highlight_section_model['description'] = 'testString'
        highlight_section_model['description_i18n'] = {'foo': 'bar'}
        highlight_section_model['title'] = 'testString'
        highlight_section_model['title_i18n'] = {'foo': 'bar'}

        media_section_model = {} # MediaSection
        media_section_model['caption'] = 'testString'
        media_section_model['caption_i18n'] = {'foo': 'bar'}
        media_section_model['thumbnail'] = 'testString'
        media_section_model['type'] = 'image'
        media_section_model['url'] = 'testString'

        catalog_listing_version_model = {} # CatalogListingVersion
        catalog_listing_version_model['deprecatePending'] = deprecate_pending_model
        catalog_listing_version_model['id'] = 'testString'
        catalog_listing_version_model['kindFormat'] = 'Helm chart'
        catalog_listing_version_model['kindId'] = 'testString'
        catalog_listing_version_model['kindTarget'] = 'iks'
        catalog_listing_version_model['packageVersion'] = 'testString'
        catalog_listing_version_model['state'] = 'deprecated'
        catalog_listing_version_model['stateChangeTime'] = 'testString'
        catalog_listing_version_model['validatedState'] = 'testString'
        catalog_listing_version_model['version'] = 'testString'
        catalog_listing_version_model['versionLocator'] = 'testString'
        catalog_listing_version_model['allowlistedAccounts'] = ['testString']

        # Construct a json representation of a CatalogListingDetails model
        catalog_listing_details_model_json = {}
        catalog_listing_details_model_json['accountId'] = 'testString'
        catalog_listing_details_model_json['catalogId'] = 'testString'
        catalog_listing_details_model_json['deprecatePending'] = deprecate_pending_model
        catalog_listing_details_model_json['description'] = 'testString'
        catalog_listing_details_model_json['documentationUrl'] = 'testString'
        catalog_listing_details_model_json['editable'] = True
        catalog_listing_details_model_json['highlights'] = [highlight_section_model]
        catalog_listing_details_model_json['iconUrl'] = 'testString'
        catalog_listing_details_model_json['id'] = 'testString'
        catalog_listing_details_model_json['keywords'] = ['testString']
        catalog_listing_details_model_json['label'] = 'testString'
        catalog_listing_details_model_json['label_i18n'] = {'foo': 'bar'}
        catalog_listing_details_model_json['longDescription'] = 'testString'
        catalog_listing_details_model_json['long_description_i18n'] = {'foo': 'bar'}
        catalog_listing_details_model_json['media'] = [media_section_model]
        catalog_listing_details_model_json['name'] = 'testString'
        catalog_listing_details_model_json['pcManaged'] = True
        catalog_listing_details_model_json['provider'] = 'testString'
        catalog_listing_details_model_json['publishedToAccessList'] = True
        catalog_listing_details_model_json['publishedToIBM'] = True
        catalog_listing_details_model_json['publishedToPublic'] = True
        catalog_listing_details_model_json['short_description_i18n'] = {'foo': 'bar'}
        catalog_listing_details_model_json['tags'] = ['testString']
        catalog_listing_details_model_json['versions'] = [catalog_listing_version_model]

        # Construct a model instance of CatalogListingDetails by calling from_dict on the json representation
        catalog_listing_details_model = CatalogListingDetails.from_dict(catalog_listing_details_model_json)
        assert catalog_listing_details_model != False

        # Construct a model instance of CatalogListingDetails by calling from_dict on the json representation
        catalog_listing_details_model_dict = CatalogListingDetails.from_dict(catalog_listing_details_model_json).__dict__
        catalog_listing_details_model2 = CatalogListingDetails(**catalog_listing_details_model_dict)

        # Verify the model instances are equivalent
        assert catalog_listing_details_model == catalog_listing_details_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_listing_details_model_json2 = catalog_listing_details_model.to_dict()
        assert catalog_listing_details_model_json2 == catalog_listing_details_model_json

class TestModel_CatalogListingVersion():
    """
    Test Class for CatalogListingVersion
    """

    def test_catalog_listing_version_serialization(self):
        """
        Test serialization/deserialization for CatalogListingVersion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deprecate_pending_model = {} # DeprecatePending
        deprecate_pending_model['deprecateDate'] = 'testString'
        deprecate_pending_model['deprecateState'] = 'testString'
        deprecate_pending_model['description'] = 'testString'

        # Construct a json representation of a CatalogListingVersion model
        catalog_listing_version_model_json = {}
        catalog_listing_version_model_json['deprecatePending'] = deprecate_pending_model
        catalog_listing_version_model_json['id'] = 'testString'
        catalog_listing_version_model_json['kindFormat'] = 'Helm chart'
        catalog_listing_version_model_json['kindId'] = 'testString'
        catalog_listing_version_model_json['kindTarget'] = 'iks'
        catalog_listing_version_model_json['packageVersion'] = 'testString'
        catalog_listing_version_model_json['state'] = 'deprecated'
        catalog_listing_version_model_json['stateChangeTime'] = 'testString'
        catalog_listing_version_model_json['validatedState'] = 'testString'
        catalog_listing_version_model_json['version'] = 'testString'
        catalog_listing_version_model_json['versionLocator'] = 'testString'
        catalog_listing_version_model_json['allowlistedAccounts'] = ['testString']

        # Construct a model instance of CatalogListingVersion by calling from_dict on the json representation
        catalog_listing_version_model = CatalogListingVersion.from_dict(catalog_listing_version_model_json)
        assert catalog_listing_version_model != False

        # Construct a model instance of CatalogListingVersion by calling from_dict on the json representation
        catalog_listing_version_model_dict = CatalogListingVersion.from_dict(catalog_listing_version_model_json).__dict__
        catalog_listing_version_model2 = CatalogListingVersion(**catalog_listing_version_model_dict)

        # Verify the model instances are equivalent
        assert catalog_listing_version_model == catalog_listing_version_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_listing_version_model_json2 = catalog_listing_version_model.to_dict()
        assert catalog_listing_version_model_json2 == catalog_listing_version_model_json

class TestModel_ChangeRequest():
    """
    Test Class for ChangeRequest
    """

    def test_change_request_serialization(self):
        """
        Test serialization/deserialization for ChangeRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        support_details_availability_times_model = {} # SupportDetailsAvailabilityTimes
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        support_details_availability_model = {} # SupportDetailsAvailability
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        support_response_times_model = {} # SupportResponseTimes
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        support_details_model = {} # SupportDetails
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        support_escalation_times_model = {} # SupportEscalationTimes
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        support_escalation_model = {} # SupportEscalation
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        support_model = {} # Support
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        # Construct a json representation of a ChangeRequest model
        change_request_model_json = {}
        change_request_model_json['id'] = 'testString'
        change_request_model_json['createdAt'] = 'testString'
        change_request_model_json['initiator'] = 'testString'
        change_request_model_json['merged'] = 'testString'
        change_request_model_json['change'] = support_model

        # Construct a model instance of ChangeRequest by calling from_dict on the json representation
        change_request_model = ChangeRequest.from_dict(change_request_model_json)
        assert change_request_model != False

        # Construct a model instance of ChangeRequest by calling from_dict on the json representation
        change_request_model_dict = ChangeRequest.from_dict(change_request_model_json).__dict__
        change_request_model2 = ChangeRequest(**change_request_model_dict)

        # Verify the model instances are equivalent
        assert change_request_model == change_request_model2

        # Convert model instance back to dict and verify no loss of data
        change_request_model_json2 = change_request_model.to_dict()
        assert change_request_model_json2 == change_request_model_json

class TestModel_CloudBadge():
    """
    Test Class for CloudBadge
    """

    def test_cloud_badge_serialization(self):
        """
        Test serialization/deserialization for CloudBadge
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cloud_badge_learn_more_links_model = {} # CloudBadgeLearnMoreLinks
        cloud_badge_learn_more_links_model['firstParty'] = 'testString'
        cloud_badge_learn_more_links_model['thirdParty'] = 'testString'

        # Construct a json representation of a CloudBadge model
        cloud_badge_model_json = {}
        cloud_badge_model_json['id'] = 'testString'
        cloud_badge_model_json['label'] = 'testString'
        cloud_badge_model_json['description'] = 'testString'
        cloud_badge_model_json['learnMoreLinks'] = cloud_badge_learn_more_links_model
        cloud_badge_model_json['getStartedLink'] = 'testString'
        cloud_badge_model_json['tag'] = 'testString'

        # Construct a model instance of CloudBadge by calling from_dict on the json representation
        cloud_badge_model = CloudBadge.from_dict(cloud_badge_model_json)
        assert cloud_badge_model != False

        # Construct a model instance of CloudBadge by calling from_dict on the json representation
        cloud_badge_model_dict = CloudBadge.from_dict(cloud_badge_model_json).__dict__
        cloud_badge_model2 = CloudBadge(**cloud_badge_model_dict)

        # Verify the model instances are equivalent
        assert cloud_badge_model == cloud_badge_model2

        # Convert model instance back to dict and verify no loss of data
        cloud_badge_model_json2 = cloud_badge_model.to_dict()
        assert cloud_badge_model_json2 == cloud_badge_model_json

class TestModel_CloudBadgeLearnMoreLinks():
    """
    Test Class for CloudBadgeLearnMoreLinks
    """

    def test_cloud_badge_learn_more_links_serialization(self):
        """
        Test serialization/deserialization for CloudBadgeLearnMoreLinks
        """

        # Construct a json representation of a CloudBadgeLearnMoreLinks model
        cloud_badge_learn_more_links_model_json = {}
        cloud_badge_learn_more_links_model_json['firstParty'] = 'testString'
        cloud_badge_learn_more_links_model_json['thirdParty'] = 'testString'

        # Construct a model instance of CloudBadgeLearnMoreLinks by calling from_dict on the json representation
        cloud_badge_learn_more_links_model = CloudBadgeLearnMoreLinks.from_dict(cloud_badge_learn_more_links_model_json)
        assert cloud_badge_learn_more_links_model != False

        # Construct a model instance of CloudBadgeLearnMoreLinks by calling from_dict on the json representation
        cloud_badge_learn_more_links_model_dict = CloudBadgeLearnMoreLinks.from_dict(cloud_badge_learn_more_links_model_json).__dict__
        cloud_badge_learn_more_links_model2 = CloudBadgeLearnMoreLinks(**cloud_badge_learn_more_links_model_dict)

        # Verify the model instances are equivalent
        assert cloud_badge_learn_more_links_model == cloud_badge_learn_more_links_model2

        # Convert model instance back to dict and verify no loss of data
        cloud_badge_learn_more_links_model_json2 = cloud_badge_learn_more_links_model.to_dict()
        assert cloud_badge_learn_more_links_model_json2 == cloud_badge_learn_more_links_model_json

class TestModel_CreatePlanResponse():
    """
    Test Class for CreatePlanResponse
    """

    def test_create_plan_response_serialization(self):
        """
        Test serialization/deserialization for CreatePlanResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        license_model = {} # License
        license_model['description'] = 'testString'
        license_model['id'] = 'testString'
        license_model['label'] = 'testString'
        license_model['type'] = 'byol'
        license_model['url'] = 'testString'

        # Construct a json representation of a CreatePlanResponse model
        create_plan_response_model_json = {}
        create_plan_response_model_json['plans'] = [license_model]

        # Construct a model instance of CreatePlanResponse by calling from_dict on the json representation
        create_plan_response_model = CreatePlanResponse.from_dict(create_plan_response_model_json)
        assert create_plan_response_model != False

        # Construct a model instance of CreatePlanResponse by calling from_dict on the json representation
        create_plan_response_model_dict = CreatePlanResponse.from_dict(create_plan_response_model_json).__dict__
        create_plan_response_model2 = CreatePlanResponse(**create_plan_response_model_dict)

        # Verify the model instances are equivalent
        assert create_plan_response_model == create_plan_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_plan_response_model_json2 = create_plan_response_model.to_dict()
        assert create_plan_response_model_json2 == create_plan_response_model_json

class TestModel_DeprecatePending():
    """
    Test Class for DeprecatePending
    """

    def test_deprecate_pending_serialization(self):
        """
        Test serialization/deserialization for DeprecatePending
        """

        # Construct a json representation of a DeprecatePending model
        deprecate_pending_model_json = {}
        deprecate_pending_model_json['deprecateDate'] = 'testString'
        deprecate_pending_model_json['deprecateState'] = 'testString'
        deprecate_pending_model_json['description'] = 'testString'

        # Construct a model instance of DeprecatePending by calling from_dict on the json representation
        deprecate_pending_model = DeprecatePending.from_dict(deprecate_pending_model_json)
        assert deprecate_pending_model != False

        # Construct a model instance of DeprecatePending by calling from_dict on the json representation
        deprecate_pending_model_dict = DeprecatePending.from_dict(deprecate_pending_model_json).__dict__
        deprecate_pending_model2 = DeprecatePending(**deprecate_pending_model_dict)

        # Verify the model instances are equivalent
        assert deprecate_pending_model == deprecate_pending_model2

        # Convert model instance back to dict and verify no loss of data
        deprecate_pending_model_json2 = deprecate_pending_model.to_dict()
        assert deprecate_pending_model_json2 == deprecate_pending_model_json

class TestModel_Error():
    """
    Test Class for Error
    """

    def test_error_serialization(self):
        """
        Test serialization/deserialization for Error
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_extensions_model = {} # ErrorExtensions
        error_extensions_model['code'] = 'testString'
        error_extensions_model['serviceName'] = 'testString'
        error_extensions_model['exception'] = {'foo': 'bar'}
        error_extensions_model['trid'] = 'testString'
        error_extensions_model['operationName'] = 'testString'

        # Construct a json representation of a Error model
        error_model_json = {}
        error_model_json['message'] = 'testString'
        error_model_json['extensions'] = error_extensions_model

        # Construct a model instance of Error by calling from_dict on the json representation
        error_model = Error.from_dict(error_model_json)
        assert error_model != False

        # Construct a model instance of Error by calling from_dict on the json representation
        error_model_dict = Error.from_dict(error_model_json).__dict__
        error_model2 = Error(**error_model_dict)

        # Verify the model instances are equivalent
        assert error_model == error_model2

        # Convert model instance back to dict and verify no loss of data
        error_model_json2 = error_model.to_dict()
        assert error_model_json2 == error_model_json

class TestModel_ErrorExtensions():
    """
    Test Class for ErrorExtensions
    """

    def test_error_extensions_serialization(self):
        """
        Test serialization/deserialization for ErrorExtensions
        """

        # Construct a json representation of a ErrorExtensions model
        error_extensions_model_json = {}
        error_extensions_model_json['code'] = 'testString'
        error_extensions_model_json['serviceName'] = 'testString'
        error_extensions_model_json['exception'] = {'foo': 'bar'}
        error_extensions_model_json['trid'] = 'testString'
        error_extensions_model_json['operationName'] = 'testString'

        # Construct a model instance of ErrorExtensions by calling from_dict on the json representation
        error_extensions_model = ErrorExtensions.from_dict(error_extensions_model_json)
        assert error_extensions_model != False

        # Construct a model instance of ErrorExtensions by calling from_dict on the json representation
        error_extensions_model_dict = ErrorExtensions.from_dict(error_extensions_model_json).__dict__
        error_extensions_model2 = ErrorExtensions(**error_extensions_model_dict)

        # Verify the model instances are equivalent
        assert error_extensions_model == error_extensions_model2

        # Convert model instance back to dict and verify no loss of data
        error_extensions_model_json2 = error_extensions_model.to_dict()
        assert error_extensions_model_json2 == error_extensions_model_json

class TestModel_EscalationContactsUpdate():
    """
    Test Class for EscalationContactsUpdate
    """

    def test_escalation_contacts_update_serialization(self):
        """
        Test serialization/deserialization for EscalationContactsUpdate
        """

        # Construct a json representation of a EscalationContactsUpdate model
        escalation_contacts_update_model_json = {}
        escalation_contacts_update_model_json['email'] = 'testString'
        escalation_contacts_update_model_json['name'] = 'testString'

        # Construct a model instance of EscalationContactsUpdate by calling from_dict on the json representation
        escalation_contacts_update_model = EscalationContactsUpdate.from_dict(escalation_contacts_update_model_json)
        assert escalation_contacts_update_model != False

        # Construct a model instance of EscalationContactsUpdate by calling from_dict on the json representation
        escalation_contacts_update_model_dict = EscalationContactsUpdate.from_dict(escalation_contacts_update_model_json).__dict__
        escalation_contacts_update_model2 = EscalationContactsUpdate(**escalation_contacts_update_model_dict)

        # Verify the model instances are equivalent
        assert escalation_contacts_update_model == escalation_contacts_update_model2

        # Convert model instance back to dict and verify no loss of data
        escalation_contacts_update_model_json2 = escalation_contacts_update_model.to_dict()
        assert escalation_contacts_update_model_json2 == escalation_contacts_update_model_json

class TestModel_HighlightSection():
    """
    Test Class for HighlightSection
    """

    def test_highlight_section_serialization(self):
        """
        Test serialization/deserialization for HighlightSection
        """

        # Construct a json representation of a HighlightSection model
        highlight_section_model_json = {}
        highlight_section_model_json['description'] = 'testString'
        highlight_section_model_json['description_i18n'] = {'foo': 'bar'}
        highlight_section_model_json['title'] = 'testString'
        highlight_section_model_json['title_i18n'] = {'foo': 'bar'}

        # Construct a model instance of HighlightSection by calling from_dict on the json representation
        highlight_section_model = HighlightSection.from_dict(highlight_section_model_json)
        assert highlight_section_model != False

        # Construct a model instance of HighlightSection by calling from_dict on the json representation
        highlight_section_model_dict = HighlightSection.from_dict(highlight_section_model_json).__dict__
        highlight_section_model2 = HighlightSection(**highlight_section_model_dict)

        # Verify the model instances are equivalent
        assert highlight_section_model == highlight_section_model2

        # Convert model instance back to dict and verify no loss of data
        highlight_section_model_json2 = highlight_section_model.to_dict()
        assert highlight_section_model_json2 == highlight_section_model_json

class TestModel_HighlightSectionInput():
    """
    Test Class for HighlightSectionInput
    """

    def test_highlight_section_input_serialization(self):
        """
        Test serialization/deserialization for HighlightSectionInput
        """

        # Construct a json representation of a HighlightSectionInput model
        highlight_section_input_model_json = {}
        highlight_section_input_model_json['description'] = 'testString'
        highlight_section_input_model_json['title'] = 'testString'

        # Construct a model instance of HighlightSectionInput by calling from_dict on the json representation
        highlight_section_input_model = HighlightSectionInput.from_dict(highlight_section_input_model_json)
        assert highlight_section_input_model != False

        # Construct a model instance of HighlightSectionInput by calling from_dict on the json representation
        highlight_section_input_model_dict = HighlightSectionInput.from_dict(highlight_section_input_model_json).__dict__
        highlight_section_input_model2 = HighlightSectionInput(**highlight_section_input_model_dict)

        # Verify the model instances are equivalent
        assert highlight_section_input_model == highlight_section_input_model2

        # Convert model instance back to dict and verify no loss of data
        highlight_section_input_model_json2 = highlight_section_input_model.to_dict()
        assert highlight_section_input_model_json2 == highlight_section_input_model_json

class TestModel_HistoryItem():
    """
    Test Class for HistoryItem
    """

    def test_history_item_serialization(self):
        """
        Test serialization/deserialization for HistoryItem
        """

        # Construct a json representation of a HistoryItem model
        history_item_model_json = {}
        history_item_model_json['at'] = 'testString'
        history_item_model_json['displayName'] = 'testString'
        history_item_model_json['event'] = 'testString'
        history_item_model_json['reason'] = 'testString'
        history_item_model_json['username'] = 'testString'

        # Construct a model instance of HistoryItem by calling from_dict on the json representation
        history_item_model = HistoryItem.from_dict(history_item_model_json)
        assert history_item_model != False

        # Construct a model instance of HistoryItem by calling from_dict on the json representation
        history_item_model_dict = HistoryItem.from_dict(history_item_model_json).__dict__
        history_item_model2 = HistoryItem(**history_item_model_dict)

        # Verify the model instances are equivalent
        assert history_item_model == history_item_model2

        # Convert model instance back to dict and verify no loss of data
        history_item_model_json2 = history_item_model.to_dict()
        assert history_item_model_json2 == history_item_model_json

class TestModel_License():
    """
    Test Class for License
    """

    def test_license_serialization(self):
        """
        Test serialization/deserialization for License
        """

        # Construct a json representation of a License model
        license_model_json = {}
        license_model_json['description'] = 'testString'
        license_model_json['id'] = 'testString'
        license_model_json['label'] = 'testString'
        license_model_json['type'] = 'byol'
        license_model_json['url'] = 'testString'

        # Construct a model instance of License by calling from_dict on the json representation
        license_model = License.from_dict(license_model_json)
        assert license_model != False

        # Construct a model instance of License by calling from_dict on the json representation
        license_model_dict = License.from_dict(license_model_json).__dict__
        license_model2 = License(**license_model_dict)

        # Verify the model instances are equivalent
        assert license_model == license_model2

        # Convert model instance back to dict and verify no loss of data
        license_model_json2 = license_model.to_dict()
        assert license_model_json2 == license_model_json

class TestModel_ListPlansResponse():
    """
    Test Class for ListPlansResponse
    """

    def test_list_plans_response_serialization(self):
        """
        Test serialization/deserialization for ListPlansResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        license_model = {} # License
        license_model['description'] = 'testString'
        license_model['id'] = 'testString'
        license_model['label'] = 'testString'
        license_model['type'] = 'byol'
        license_model['url'] = 'testString'

        # Construct a json representation of a ListPlansResponse model
        list_plans_response_model_json = {}
        list_plans_response_model_json['plans'] = [license_model]

        # Construct a model instance of ListPlansResponse by calling from_dict on the json representation
        list_plans_response_model = ListPlansResponse.from_dict(list_plans_response_model_json)
        assert list_plans_response_model != False

        # Construct a model instance of ListPlansResponse by calling from_dict on the json representation
        list_plans_response_model_dict = ListPlansResponse.from_dict(list_plans_response_model_json).__dict__
        list_plans_response_model2 = ListPlansResponse(**list_plans_response_model_dict)

        # Verify the model instances are equivalent
        assert list_plans_response_model == list_plans_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_plans_response_model_json2 = list_plans_response_model.to_dict()
        assert list_plans_response_model_json2 == list_plans_response_model_json

class TestModel_ListProductApprovalsResponse():
    """
    Test Class for ListProductApprovalsResponse
    """

    def test_list_product_approvals_response_serialization(self):
        """
        Test serialization/deserialization for ListProductApprovalsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        history_item_model = {} # HistoryItem
        history_item_model['at'] = 'testString'
        history_item_model['displayName'] = 'testString'
        history_item_model['event'] = 'testString'
        history_item_model['reason'] = 'testString'
        history_item_model['username'] = 'testString'

        state_model = {} # State
        state_model['name'] = 'waitingForRequestForReview'

        resource_model = {} # Resource
        resource_model['history'] = [history_item_model]
        resource_model['id'] = 'testString'
        resource_model['nextEvents'] = ['testString']
        resource_model['state'] = state_model

        # Construct a json representation of a ListProductApprovalsResponse model
        list_product_approvals_response_model_json = {}
        list_product_approvals_response_model_json['approvals'] = [resource_model]

        # Construct a model instance of ListProductApprovalsResponse by calling from_dict on the json representation
        list_product_approvals_response_model = ListProductApprovalsResponse.from_dict(list_product_approvals_response_model_json)
        assert list_product_approvals_response_model != False

        # Construct a model instance of ListProductApprovalsResponse by calling from_dict on the json representation
        list_product_approvals_response_model_dict = ListProductApprovalsResponse.from_dict(list_product_approvals_response_model_json).__dict__
        list_product_approvals_response_model2 = ListProductApprovalsResponse(**list_product_approvals_response_model_dict)

        # Verify the model instances are equivalent
        assert list_product_approvals_response_model == list_product_approvals_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_product_approvals_response_model_json2 = list_product_approvals_response_model.to_dict()
        assert list_product_approvals_response_model_json2 == list_product_approvals_response_model_json

class TestModel_ListProductsResponse():
    """
    Test Class for ListProductsResponse
    """

    def test_list_products_response_serialization(self):
        """
        Test serialization/deserialization for ListProductsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_extensions_model = {} # ErrorExtensions
        error_extensions_model['code'] = 'testString'
        error_extensions_model['serviceName'] = 'testString'
        error_extensions_model['exception'] = {'foo': 'bar'}
        error_extensions_model['trid'] = 'testString'
        error_extensions_model['operationName'] = 'testString'

        error_model = {} # Error
        error_model['message'] = 'testString'
        error_model['extensions'] = error_extensions_model

        support_details_availability_times_model = {} # SupportDetailsAvailabilityTimes
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        support_details_availability_model = {} # SupportDetailsAvailability
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        support_response_times_model = {} # SupportResponseTimes
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        support_details_model = {} # SupportDetails
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        support_escalation_times_model = {} # SupportEscalationTimes
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        support_escalation_model = {} # SupportEscalation
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        support_model = {} # Support
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        change_request_model = {} # ChangeRequest
        change_request_model['id'] = 'testString'
        change_request_model['createdAt'] = 'testString'
        change_request_model['initiator'] = 'testString'
        change_request_model['merged'] = 'testString'
        change_request_model['change'] = support_model

        product_details_model = {} # ProductDetails
        product_details_model['accountId'] = 'testString'
        product_details_model['createdAt'] = 'testString'
        product_details_model['id'] = 'testString'
        product_details_model['materialAgreement'] = True
        product_details_model['productType'] = 'SOFTWARE'
        product_details_model['productName'] = 'testString'
        product_details_model['publishedAt'] = 'testString'
        product_details_model['taxAssessment'] = 'SOFTWARE'
        product_details_model['updatedAt'] = 'testString'
        product_details_model['changeRequests'] = [change_request_model]

        # Construct a json representation of a ListProductsResponse model
        list_products_response_model_json = {}
        list_products_response_model_json['errors'] = [error_model]
        list_products_response_model_json['products'] = [product_details_model]

        # Construct a model instance of ListProductsResponse by calling from_dict on the json representation
        list_products_response_model = ListProductsResponse.from_dict(list_products_response_model_json)
        assert list_products_response_model != False

        # Construct a model instance of ListProductsResponse by calling from_dict on the json representation
        list_products_response_model_dict = ListProductsResponse.from_dict(list_products_response_model_json).__dict__
        list_products_response_model2 = ListProductsResponse(**list_products_response_model_dict)

        # Verify the model instances are equivalent
        assert list_products_response_model == list_products_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_products_response_model_json2 = list_products_response_model.to_dict()
        assert list_products_response_model_json2 == list_products_response_model_json

class TestModel_ListSupportChangeRequestsResponse():
    """
    Test Class for ListSupportChangeRequestsResponse
    """

    def test_list_support_change_requests_response_serialization(self):
        """
        Test serialization/deserialization for ListSupportChangeRequestsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        support_details_availability_times_model = {} # SupportDetailsAvailabilityTimes
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        support_details_availability_model = {} # SupportDetailsAvailability
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        support_response_times_model = {} # SupportResponseTimes
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        support_details_model = {} # SupportDetails
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        support_escalation_times_model = {} # SupportEscalationTimes
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        support_escalation_model = {} # SupportEscalation
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        support_model = {} # Support
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        change_request_model = {} # ChangeRequest
        change_request_model['id'] = 'testString'
        change_request_model['createdAt'] = 'testString'
        change_request_model['initiator'] = 'testString'
        change_request_model['merged'] = 'testString'
        change_request_model['change'] = support_model

        # Construct a json representation of a ListSupportChangeRequestsResponse model
        list_support_change_requests_response_model_json = {}
        list_support_change_requests_response_model_json['changes'] = [change_request_model]

        # Construct a model instance of ListSupportChangeRequestsResponse by calling from_dict on the json representation
        list_support_change_requests_response_model = ListSupportChangeRequestsResponse.from_dict(list_support_change_requests_response_model_json)
        assert list_support_change_requests_response_model != False

        # Construct a model instance of ListSupportChangeRequestsResponse by calling from_dict on the json representation
        list_support_change_requests_response_model_dict = ListSupportChangeRequestsResponse.from_dict(list_support_change_requests_response_model_json).__dict__
        list_support_change_requests_response_model2 = ListSupportChangeRequestsResponse(**list_support_change_requests_response_model_dict)

        # Verify the model instances are equivalent
        assert list_support_change_requests_response_model == list_support_change_requests_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_support_change_requests_response_model_json2 = list_support_change_requests_response_model.to_dict()
        assert list_support_change_requests_response_model_json2 == list_support_change_requests_response_model_json

class TestModel_MediaSection():
    """
    Test Class for MediaSection
    """

    def test_media_section_serialization(self):
        """
        Test serialization/deserialization for MediaSection
        """

        # Construct a json representation of a MediaSection model
        media_section_model_json = {}
        media_section_model_json['caption'] = 'testString'
        media_section_model_json['caption_i18n'] = {'foo': 'bar'}
        media_section_model_json['thumbnail'] = 'testString'
        media_section_model_json['type'] = 'image'
        media_section_model_json['url'] = 'testString'

        # Construct a model instance of MediaSection by calling from_dict on the json representation
        media_section_model = MediaSection.from_dict(media_section_model_json)
        assert media_section_model != False

        # Construct a model instance of MediaSection by calling from_dict on the json representation
        media_section_model_dict = MediaSection.from_dict(media_section_model_json).__dict__
        media_section_model2 = MediaSection(**media_section_model_dict)

        # Verify the model instances are equivalent
        assert media_section_model == media_section_model2

        # Convert model instance back to dict and verify no loss of data
        media_section_model_json2 = media_section_model.to_dict()
        assert media_section_model_json2 == media_section_model_json

class TestModel_MediaSectionInput():
    """
    Test Class for MediaSectionInput
    """

    def test_media_section_input_serialization(self):
        """
        Test serialization/deserialization for MediaSectionInput
        """

        # Construct a json representation of a MediaSectionInput model
        media_section_input_model_json = {}
        media_section_input_model_json['caption'] = 'testString'
        media_section_input_model_json['thumbnail'] = 'testString'
        media_section_input_model_json['type'] = 'image'
        media_section_input_model_json['url'] = 'testString'

        # Construct a model instance of MediaSectionInput by calling from_dict on the json representation
        media_section_input_model = MediaSectionInput.from_dict(media_section_input_model_json)
        assert media_section_input_model != False

        # Construct a model instance of MediaSectionInput by calling from_dict on the json representation
        media_section_input_model_dict = MediaSectionInput.from_dict(media_section_input_model_json).__dict__
        media_section_input_model2 = MediaSectionInput(**media_section_input_model_dict)

        # Verify the model instances are equivalent
        assert media_section_input_model == media_section_input_model2

        # Convert model instance back to dict and verify no loss of data
        media_section_input_model_json2 = media_section_input_model.to_dict()
        assert media_section_input_model_json2 == media_section_input_model_json

class TestModel_ProductDetails():
    """
    Test Class for ProductDetails
    """

    def test_product_details_serialization(self):
        """
        Test serialization/deserialization for ProductDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        support_details_availability_times_model = {} # SupportDetailsAvailabilityTimes
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        support_details_availability_model = {} # SupportDetailsAvailability
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        support_response_times_model = {} # SupportResponseTimes
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        support_details_model = {} # SupportDetails
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        support_escalation_times_model = {} # SupportEscalationTimes
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        support_escalation_model = {} # SupportEscalation
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        support_model = {} # Support
        support_model['locations'] = ['US']
        support_model['process'] = 'testString'
        support_model['process_i18n'] = {'foo': 'bar'}
        support_model['support_details'] = [support_details_model]
        support_model['support_escalation'] = support_escalation_model
        support_model['support_type'] = 'third-party'
        support_model['url'] = 'https://my-company.com/support'

        change_request_model = {} # ChangeRequest
        change_request_model['id'] = 'testString'
        change_request_model['createdAt'] = 'testString'
        change_request_model['initiator'] = 'testString'
        change_request_model['merged'] = 'testString'
        change_request_model['change'] = support_model

        # Construct a json representation of a ProductDetails model
        product_details_model_json = {}
        product_details_model_json['accountId'] = 'testString'
        product_details_model_json['createdAt'] = 'testString'
        product_details_model_json['id'] = 'testString'
        product_details_model_json['materialAgreement'] = True
        product_details_model_json['productType'] = 'SOFTWARE'
        product_details_model_json['productName'] = 'testString'
        product_details_model_json['publishedAt'] = 'testString'
        product_details_model_json['taxAssessment'] = 'SOFTWARE'
        product_details_model_json['updatedAt'] = 'testString'
        product_details_model_json['changeRequests'] = [change_request_model]

        # Construct a model instance of ProductDetails by calling from_dict on the json representation
        product_details_model = ProductDetails.from_dict(product_details_model_json)
        assert product_details_model != False

        # Construct a model instance of ProductDetails by calling from_dict on the json representation
        product_details_model_dict = ProductDetails.from_dict(product_details_model_json).__dict__
        product_details_model2 = ProductDetails(**product_details_model_dict)

        # Verify the model instances are equivalent
        assert product_details_model == product_details_model2

        # Convert model instance back to dict and verify no loss of data
        product_details_model_json2 = product_details_model.to_dict()
        assert product_details_model_json2 == product_details_model_json

class TestModel_Resource():
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        history_item_model = {} # HistoryItem
        history_item_model['at'] = 'testString'
        history_item_model['displayName'] = 'testString'
        history_item_model['event'] = 'testString'
        history_item_model['reason'] = 'testString'
        history_item_model['username'] = 'testString'

        state_model = {} # State
        state_model['name'] = 'waitingForRequestForReview'

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['history'] = [history_item_model]
        resource_model_json['id'] = 'testString'
        resource_model_json['nextEvents'] = ['testString']
        resource_model_json['state'] = state_model

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model = Resource.from_dict(resource_model_json)
        assert resource_model != False

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model_dict = Resource.from_dict(resource_model_json).__dict__
        resource_model2 = Resource(**resource_model_dict)

        # Verify the model instances are equivalent
        assert resource_model == resource_model2

        # Convert model instance back to dict and verify no loss of data
        resource_model_json2 = resource_model.to_dict()
        assert resource_model_json2 == resource_model_json

class TestModel_State():
    """
    Test Class for State
    """

    def test_state_serialization(self):
        """
        Test serialization/deserialization for State
        """

        # Construct a json representation of a State model
        state_model_json = {}
        state_model_json['name'] = 'waitingForRequestForReview'

        # Construct a model instance of State by calling from_dict on the json representation
        state_model = State.from_dict(state_model_json)
        assert state_model != False

        # Construct a model instance of State by calling from_dict on the json representation
        state_model_dict = State.from_dict(state_model_json).__dict__
        state_model2 = State(**state_model_dict)

        # Verify the model instances are equivalent
        assert state_model == state_model2

        # Convert model instance back to dict and verify no loss of data
        state_model_json2 = state_model.to_dict()
        assert state_model_json2 == state_model_json

class TestModel_Support():
    """
    Test Class for Support
    """

    def test_support_serialization(self):
        """
        Test serialization/deserialization for Support
        """

        # Construct dict forms of any model objects needed in order to build this model.

        support_details_availability_times_model = {} # SupportDetailsAvailabilityTimes
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        support_details_availability_model = {} # SupportDetailsAvailability
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        support_response_times_model = {} # SupportResponseTimes
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        support_details_model = {} # SupportDetails
        support_details_model['availability'] = support_details_availability_model
        support_details_model['contact'] = 'testString'
        support_details_model['response_wait_time'] = support_response_times_model
        support_details_model['type'] = 'email'

        support_escalation_times_model = {} # SupportEscalationTimes
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        support_escalation_model = {} # SupportEscalation
        support_escalation_model['contact'] = 'testString'
        support_escalation_model['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model['response_wait_time'] = support_response_times_model

        # Construct a json representation of a Support model
        support_model_json = {}
        support_model_json['locations'] = ['US']
        support_model_json['process'] = 'testString'
        support_model_json['process_i18n'] = {'foo': 'bar'}
        support_model_json['support_details'] = [support_details_model]
        support_model_json['support_escalation'] = support_escalation_model
        support_model_json['support_type'] = 'third-party'
        support_model_json['url'] = 'https://my-company.com/support'

        # Construct a model instance of Support by calling from_dict on the json representation
        support_model = Support.from_dict(support_model_json)
        assert support_model != False

        # Construct a model instance of Support by calling from_dict on the json representation
        support_model_dict = Support.from_dict(support_model_json).__dict__
        support_model2 = Support(**support_model_dict)

        # Verify the model instances are equivalent
        assert support_model == support_model2

        # Convert model instance back to dict and verify no loss of data
        support_model_json2 = support_model.to_dict()
        assert support_model_json2 == support_model_json

class TestModel_SupportDetails():
    """
    Test Class for SupportDetails
    """

    def test_support_details_serialization(self):
        """
        Test serialization/deserialization for SupportDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        support_details_availability_times_model = {} # SupportDetailsAvailabilityTimes
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        support_details_availability_model = {} # SupportDetailsAvailability
        support_details_availability_model['always_available'] = True
        support_details_availability_model['times'] = [support_details_availability_times_model]
        support_details_availability_model['timezone'] = 'America/Los_Angeles'

        support_response_times_model = {} # SupportResponseTimes
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a json representation of a SupportDetails model
        support_details_model_json = {}
        support_details_model_json['availability'] = support_details_availability_model
        support_details_model_json['contact'] = 'testString'
        support_details_model_json['response_wait_time'] = support_response_times_model
        support_details_model_json['type'] = 'email'

        # Construct a model instance of SupportDetails by calling from_dict on the json representation
        support_details_model = SupportDetails.from_dict(support_details_model_json)
        assert support_details_model != False

        # Construct a model instance of SupportDetails by calling from_dict on the json representation
        support_details_model_dict = SupportDetails.from_dict(support_details_model_json).__dict__
        support_details_model2 = SupportDetails(**support_details_model_dict)

        # Verify the model instances are equivalent
        assert support_details_model == support_details_model2

        # Convert model instance back to dict and verify no loss of data
        support_details_model_json2 = support_details_model.to_dict()
        assert support_details_model_json2 == support_details_model_json

class TestModel_SupportDetailsAvailability():
    """
    Test Class for SupportDetailsAvailability
    """

    def test_support_details_availability_serialization(self):
        """
        Test serialization/deserialization for SupportDetailsAvailability
        """

        # Construct dict forms of any model objects needed in order to build this model.

        support_details_availability_times_model = {} # SupportDetailsAvailabilityTimes
        support_details_availability_times_model['day'] = 1
        support_details_availability_times_model['end_time'] = '19:30'
        support_details_availability_times_model['start_time'] = '10:30'

        # Construct a json representation of a SupportDetailsAvailability model
        support_details_availability_model_json = {}
        support_details_availability_model_json['always_available'] = True
        support_details_availability_model_json['times'] = [support_details_availability_times_model]
        support_details_availability_model_json['timezone'] = 'America/Los_Angeles'

        # Construct a model instance of SupportDetailsAvailability by calling from_dict on the json representation
        support_details_availability_model = SupportDetailsAvailability.from_dict(support_details_availability_model_json)
        assert support_details_availability_model != False

        # Construct a model instance of SupportDetailsAvailability by calling from_dict on the json representation
        support_details_availability_model_dict = SupportDetailsAvailability.from_dict(support_details_availability_model_json).__dict__
        support_details_availability_model2 = SupportDetailsAvailability(**support_details_availability_model_dict)

        # Verify the model instances are equivalent
        assert support_details_availability_model == support_details_availability_model2

        # Convert model instance back to dict and verify no loss of data
        support_details_availability_model_json2 = support_details_availability_model.to_dict()
        assert support_details_availability_model_json2 == support_details_availability_model_json

class TestModel_SupportDetailsAvailabilityTimes():
    """
    Test Class for SupportDetailsAvailabilityTimes
    """

    def test_support_details_availability_times_serialization(self):
        """
        Test serialization/deserialization for SupportDetailsAvailabilityTimes
        """

        # Construct a json representation of a SupportDetailsAvailabilityTimes model
        support_details_availability_times_model_json = {}
        support_details_availability_times_model_json['day'] = 1
        support_details_availability_times_model_json['end_time'] = '19:30'
        support_details_availability_times_model_json['start_time'] = '10:30'

        # Construct a model instance of SupportDetailsAvailabilityTimes by calling from_dict on the json representation
        support_details_availability_times_model = SupportDetailsAvailabilityTimes.from_dict(support_details_availability_times_model_json)
        assert support_details_availability_times_model != False

        # Construct a model instance of SupportDetailsAvailabilityTimes by calling from_dict on the json representation
        support_details_availability_times_model_dict = SupportDetailsAvailabilityTimes.from_dict(support_details_availability_times_model_json).__dict__
        support_details_availability_times_model2 = SupportDetailsAvailabilityTimes(**support_details_availability_times_model_dict)

        # Verify the model instances are equivalent
        assert support_details_availability_times_model == support_details_availability_times_model2

        # Convert model instance back to dict and verify no loss of data
        support_details_availability_times_model_json2 = support_details_availability_times_model.to_dict()
        assert support_details_availability_times_model_json2 == support_details_availability_times_model_json

class TestModel_SupportEscalation():
    """
    Test Class for SupportEscalation
    """

    def test_support_escalation_serialization(self):
        """
        Test serialization/deserialization for SupportEscalation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        support_escalation_times_model = {} # SupportEscalationTimes
        support_escalation_times_model['type'] = 'hour'
        support_escalation_times_model['value'] = 2

        support_response_times_model = {} # SupportResponseTimes
        support_response_times_model['type'] = 'hour'
        support_response_times_model['value'] = 2

        # Construct a json representation of a SupportEscalation model
        support_escalation_model_json = {}
        support_escalation_model_json['contact'] = 'testString'
        support_escalation_model_json['escalation_wait_time'] = support_escalation_times_model
        support_escalation_model_json['response_wait_time'] = support_response_times_model

        # Construct a model instance of SupportEscalation by calling from_dict on the json representation
        support_escalation_model = SupportEscalation.from_dict(support_escalation_model_json)
        assert support_escalation_model != False

        # Construct a model instance of SupportEscalation by calling from_dict on the json representation
        support_escalation_model_dict = SupportEscalation.from_dict(support_escalation_model_json).__dict__
        support_escalation_model2 = SupportEscalation(**support_escalation_model_dict)

        # Verify the model instances are equivalent
        assert support_escalation_model == support_escalation_model2

        # Convert model instance back to dict and verify no loss of data
        support_escalation_model_json2 = support_escalation_model.to_dict()
        assert support_escalation_model_json2 == support_escalation_model_json

class TestModel_SupportEscalationTimes():
    """
    Test Class for SupportEscalationTimes
    """

    def test_support_escalation_times_serialization(self):
        """
        Test serialization/deserialization for SupportEscalationTimes
        """

        # Construct a json representation of a SupportEscalationTimes model
        support_escalation_times_model_json = {}
        support_escalation_times_model_json['type'] = 'hour'
        support_escalation_times_model_json['value'] = 2

        # Construct a model instance of SupportEscalationTimes by calling from_dict on the json representation
        support_escalation_times_model = SupportEscalationTimes.from_dict(support_escalation_times_model_json)
        assert support_escalation_times_model != False

        # Construct a model instance of SupportEscalationTimes by calling from_dict on the json representation
        support_escalation_times_model_dict = SupportEscalationTimes.from_dict(support_escalation_times_model_json).__dict__
        support_escalation_times_model2 = SupportEscalationTimes(**support_escalation_times_model_dict)

        # Verify the model instances are equivalent
        assert support_escalation_times_model == support_escalation_times_model2

        # Convert model instance back to dict and verify no loss of data
        support_escalation_times_model_json2 = support_escalation_times_model.to_dict()
        assert support_escalation_times_model_json2 == support_escalation_times_model_json

class TestModel_SupportResponseTimes():
    """
    Test Class for SupportResponseTimes
    """

    def test_support_response_times_serialization(self):
        """
        Test serialization/deserialization for SupportResponseTimes
        """

        # Construct a json representation of a SupportResponseTimes model
        support_response_times_model_json = {}
        support_response_times_model_json['type'] = 'hour'
        support_response_times_model_json['value'] = 2

        # Construct a model instance of SupportResponseTimes by calling from_dict on the json representation
        support_response_times_model = SupportResponseTimes.from_dict(support_response_times_model_json)
        assert support_response_times_model != False

        # Construct a model instance of SupportResponseTimes by calling from_dict on the json representation
        support_response_times_model_dict = SupportResponseTimes.from_dict(support_response_times_model_json).__dict__
        support_response_times_model2 = SupportResponseTimes(**support_response_times_model_dict)

        # Verify the model instances are equivalent
        assert support_response_times_model == support_response_times_model2

        # Convert model instance back to dict and verify no loss of data
        support_response_times_model_json2 = support_response_times_model.to_dict()
        assert support_response_times_model_json2 == support_response_times_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
