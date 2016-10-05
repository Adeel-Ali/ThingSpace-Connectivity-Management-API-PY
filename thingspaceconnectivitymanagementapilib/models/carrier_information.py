# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.models.carrier_information
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 10/05/2016
"""
from .base_model import BaseModel

class CarrierInformation(BaseModel):

    """Implementation of the 'CarrierInformation' model.

    TODO: type model description here.

    Attributes:
        carrier_name (string): TODO: type description here.
        service_plan (string): TODO: type description here.
        state (string): TODO: type description here.

    """

    def __init__(self, 
                 carrier_name = None,
                 service_plan = None,
                 state = None):
        """Constructor for the CarrierInformation class"""
        
        # Initialize members of the class
        self.carrier_name = carrier_name
        self.service_plan = service_plan
        self.state = state

        # Create a mapping from Model property names to API property names
        self.names = {
            "carrier_name" : "carrierName",
            "service_plan" : "servicePlan",
            "state" : "state",
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
            carrier_name = dictionary.get("carrierName")
            service_plan = dictionary.get("servicePlan")
            state = dictionary.get("state")
            # Return an object of this model
            return cls(carrier_name,
                       service_plan,
                       state)
