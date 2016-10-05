# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.models.sms_message
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 10/05/2016
"""
from .device_id import DeviceId
from .base_model import BaseModel

class SmsMessage(BaseModel):

    """Implementation of the 'SmsMessage' model.

    TODO: type model description here.

    Attributes:
        device_ids (list of DeviceId): TODO: type description here.
        message (string): TODO: type description here.
        timestamp (string): TODO: type description here.

    """

    def __init__(self, 
                 device_ids = None,
                 message = None,
                 timestamp = None):
        """Constructor for the SmsMessage class"""
        
        # Initialize members of the class
        self.device_ids = device_ids
        self.message = message
        self.timestamp = timestamp

        # Create a mapping from Model property names to API property names
        self.names = {
            "device_ids" : "deviceIds",
            "message" : "message",
            "timestamp" : "timestamp",
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
            device_ids = None
            if dictionary.get("deviceIds") != None:
                device_ids = list()
                for structure in dictionary.get("deviceIds"):
                    device_ids.append(DeviceId.from_dictionary(structure))
            message = dictionary.get("message")
            timestamp = dictionary.get("timestamp")
            # Return an object of this model
            return cls(device_ids,
                       message,
                       timestamp)
