# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.models.session_reset_password_response
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 10/05/2016
"""
from .base_model import BaseModel

class SessionResetPasswordResponse(BaseModel):

    """Implementation of the 'SessionResetPasswordResponse' model.

    TODO: type model description here.

    Attributes:
        new_password (string): TODO: type description here.

    """

    def __init__(self, 
                 new_password = None):
        """Constructor for the SessionResetPasswordResponse class"""
        
        # Initialize members of the class
        self.new_password = new_password

        # Create a mapping from Model property names to API property names
        self.names = {
            "new_password" : "newPassword",
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
            new_password = dictionary.get("newPassword")
            # Return an object of this model
            return cls(new_password)
