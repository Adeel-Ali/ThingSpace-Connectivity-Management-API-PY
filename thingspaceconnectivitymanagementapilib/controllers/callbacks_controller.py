# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.controllers.callbacks_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 10/05/2016
"""

from .base_controller import *

from ..models.callback_action_response import CallbackActionResponse
from ..models.callback import Callback
from ..exceptions.rest_error_response_exception import RestErrorResponseException


class CallbacksController(BaseController):

    """A Controller to access Endpoints in the thingspaceconnectivitymanagementapilib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def delete_unregister_callback_using_delete(self,
                                                vz_m_2_m_token,
                                                aname,
                                                sname):
        """Does a DELETE request to /callbacks/{aname}/name/{sname}.

        Stops the platform from sending callback messages for the specified
        account and service.

        Args:
            vz_m_2_m_token (string): M2M-MC Session Token
            aname (string): Account name
            sname (string): Service name

        Returns:
            CallbackActionResponse: Response from the API. Callback response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/callbacks/{aname}/name/{sname}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'aname': aname,
            'sname': sname
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
        _request = self.http_client.delete(_query_url, headers=_headers)

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
        return APIHelper.json_deserialize(_response.raw_body, CallbackActionResponse.from_dictionary)



    def create_register_callback_using_post(self,
                                            vz_m_2_m_token,
                                            aname,
                                            request):
        """Does a POST request to /callbacks/{aname}.

        Registers a URL where an account will receive RESTFul messages from a
        platform callback service.

        Args:
            vz_m_2_m_token (string): M2M-MC Session Token
            aname (string): Account name
            request (RegisterCallbackRequest): Request

        Returns:
            CallbackActionResponse: Response from the API. Callback response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/callbacks/{aname}'

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
        return APIHelper.json_deserialize(_response.raw_body, CallbackActionResponse.from_dictionary)



    def list_callbacks_using_get(self,
                                 vz_m_2_m_token,
                                 aname):
        """Does a GET request to /callbacks/{aname}.

        Returns the name and endpoint URL of all callback listening services
        registered for a given account.

        Args:
            vz_m_2_m_token (string): M2M-MC Session Token
            aname (string): Account name

        Returns:
            list of Callback: Response from the API. Callback response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/callbacks/{aname}'

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
        _request = self.http_client.get(_query_url, headers=_headers)

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
        return APIHelper.json_deserialize(_response.raw_body, Callback.from_dictionary)


