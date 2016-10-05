# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.models.callback
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 10/05/2016
"""
from .base_model import BaseModel

class Callback(BaseModel):

    """Implementation of the 'Callback' model.

    TODO: type model description here.

    Attributes:
        account_name (string): TODO: type description here.
        password (string): TODO: type description here.
        service_name (string): TODO: type description here.
        url (string): TODO: type description here.
        username (string): TODO: type description here.

    """

    def __init__(self, 
                 account_name = None,
                 password = None,
                 service_name = None,
                 url = None,
                 username = None):
        """Constructor for the Callback class"""
        
        # Initialize members of the class
        self.account_name = account_name
        self.password = password
        self.service_name = service_name
        self.url = url
        self.username = username

        # Create a mapping from Model property names to API property names
        self.names = {
            "account_name" : "accountName",
            "password" : "password",
            "service_name" : "serviceName",
            "url" : "url",
            "username" : "username",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            account_name = dictionary.get("accountName")
            password = dictionary.get("password")
            service_name = dictionary.get("serviceName")
            url = dictionary.get("url")
            username = dictionary.get("username")
            # Return an object of this model
            return cls(account_name,
                       password,
                       service_name,
                       url,
                       username)
