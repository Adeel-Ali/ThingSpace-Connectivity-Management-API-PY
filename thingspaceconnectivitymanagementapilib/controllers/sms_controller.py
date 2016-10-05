# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.controllers.sms_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 10/05/2016
"""

from .base_controller import *

from ..models.rest_success_response import RestSuccessResponse
from ..models.sms_messages_response import SmsMessagesResponse
from ..models.request_response import RequestResponse
from ..exceptions.rest_error_response_exception import RestErrorResponseException


class SmsController(BaseController):

    """A Controller to access Endpoints in the thingspaceconnectivitymanagementapilib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def update_start_sms_callback_using_put(self,
                                            aname,
                                            vz_m_2_m_token):
        """Does a PUT request to /sms/{aname}/startCallbacks.

        Starts delivery of queued SMS messages for the specific account.

        Args:
            aname (string): Account name
            vz_m_2_m_token (string): M2M-MC Session Token

        Returns:
            RestSuccessResponse: Response from the API. Request Success
                Message

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/sms/{aname}/startCallbacks'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'aname': aname
        })
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'accept': 'application/json',
            'api_key': Configuration.api_key,
            'VZ-M2M-Token': vz_m_2_m_token,
            'api_key': Configuration.api_key
        }

        # Prepare the API call.
        _request = self.http_client.put(_query_url, headers=_headers)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 400:
            raise RestErrorResponseException('400 - Error Response', _context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, RestSuccessResponse.from_dictionary)



    def get_sms_messages_using_get(self,
                                   aname,
                                   vz_m_2_m_token,
                                   next = None):
        """Does a GET request to /sms/{aname}/history.

        Retrieves queued SMS messages sent by all M2M MC devices associated
        with an account.

        Args:
            aname (string): Account name
            vz_m_2_m_token (string): M2M-MC Session Token
            next (long|int, optional): Continue the previous query from the
                URL in Location Header

        Returns:
            SmsMessagesResponse: Response from the API. Successful response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/sms/{aname}/history'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'aname': aname
        })

        # Process optional query parameters
        _query_parameters = {
            'next': next
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'accept': 'application/json',
            'api_key': Configuration.api_key,
            'VZ-M2M-Token': vz_m_2_m_token,
            'api_key': Configuration.api_key
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 400:
            raise RestErrorResponseException('400 - Error Response', _context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, SmsMessagesResponse.from_dictionary)



    def create_send_sms_message_using_post(self,
                                           request,
                                           vz_m_2_m_token):
        """Does a POST request to /sms.

        Sends an SMS message to one or more devices.

        Args:
            request (SMSSendRequest): SMS Request
            vz_m_2_m_token (string): M2M-MC Session Token

        Returns:
            RequestResponse: Response from the API. Request ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/sms'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'api_key': Configuration.api_key,
            'VZ-M2M-Token': vz_m_2_m_token,
            'api_key': Configuration.api_key
        }

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 400:
            raise RestErrorResponseException('400 - Error Response', _context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, RequestResponse.from_dictionary)


