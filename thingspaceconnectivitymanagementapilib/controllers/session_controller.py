# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.controllers.session_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 10/05/2016
"""

from .base_controller import *

from ..models.session_reset_password_response import SessionResetPasswordResponse
from ..models.log_out_request import LogOutRequest
from ..models.log_in_response import LogInResponse
from ..exceptions.rest_error_response_exception import RestErrorResponseException


class SessionController(BaseController):

    """A Controller to access Endpoints in the thingspaceconnectivitymanagementapilib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def update_reset_using_put(self,
                               request,
                               vz_m_2_m_token):
        """Does a PUT request to /session/password/actions/reset.

        Returns a new, randomly generated password for the current username

        Args:
            request (SessionResetPasswordRequest): Current Password
            vz_m_2_m_token (string): M2M-MC Session Token

        Returns:
            SessionResetPasswordResponse: Response from the API. Returns a
                new, randomly generated password for the current username.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/session/password/actions/reset'
        
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
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))

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
        return APIHelper.json_deserialize(_response.raw_body, SessionResetPasswordResponse.from_dictionary)



    def create_logout_using_post(self,
                                 vz_m_2_m_token):
        """Does a POST request to /session/logout.

        Ends a Connectivity Management session.

        Args:
            vz_m_2_m_token (string): M2M-MC Session Token

        Returns:
            LogOutRequest: Response from the API. M2M-MC Session Token

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/session/logout'
        
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
        _request = self.http_client.post(_query_url, headers=_headers)

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
        return APIHelper.json_deserialize(_response.raw_body, LogOutRequest.from_dictionary)



    def create_login_using_post(self,
                                request = None):
        """Does a POST request to /session/login.

        Initiates a Connectivity Management session and returns a session
        token required in subsequent API requests.

        Args:
            request (LogInRequest, optional): request

        Returns:
            LogInResponse: Response from the API. M2M-MC Session Token

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += '/session/login'
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'user-agent': 'APIMATIC 2.0',
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'api_key': Configuration.api_key,
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
        return APIHelper.json_deserialize(_response.raw_body, LogInResponse.from_dictionary)


