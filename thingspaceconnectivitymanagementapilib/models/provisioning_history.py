# -*- coding: utf-8 -*-

"""
    thingspaceconnectivitymanagementapilib.models.provisioning_history
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 10/05/2016
"""
from .kv_pair import KvPair
from .base_model import BaseModel

class ProvisioningHistory(BaseModel):

    """Implementation of the 'ProvisioningHistory' model.

    TODO: type model description here.

    Attributes:
        event_by (string): TODO: type description here.
        event_type (string): TODO: type description here.
        extended_attributes (list of KvPair): TODO: type description here.
        mdn (string): TODO: type description here.
        msisdn (string): TODO: type description here.
        occurred_at (string): TODO: type description here.
        service_plan (string): TODO: type description here.
        status (string): TODO: type description here.

    """

    def __init__(self, 
                 event_by = None,
                 event_type = None,
                 extended_attributes = None,
                 mdn = None,
                 msisdn = None,
                 occurred_at = None,
                 service_plan = None,
                 status = None):
        """Constructor for the ProvisioningHistory class"""
        
        # Initialize members of the class
        self.event_by = event_by
        self.event_type = event_type
        self.extended_attributes = extended_attributes
        self.mdn = mdn
        self.msisdn = msisdn
        self.occurred_at = occurred_at
        self.service_plan = service_plan
        self.status = status

        # Create a mapping from Model property names to API property names
        self.names = {
            "event_by" : "eventBy",
            "event_type" : "eventType",
            "extended_attributes" : "extendedAttributes",
            "mdn" : "mdn",
            "msisdn" : "msisdn",
            "occurred_at" : "occurredAt",
            "service_plan" : "servicePlan",
            "status" : "status",
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
            event_by = dictionary.get("eventBy")
            event_type = dictionary.get("eventType")
            extended_attributes = None
            if dictionary.get("extendedAttributes") != None:
                extended_attributes = list()
                for structure in dictionary.get("extendedAttributes"):
                    extended_attributes.append(KvPair.from_dictionary(structure))
            mdn = dictionary.get("mdn")
            msisdn = dictionary.get("msisdn")
            occurred_at = dictionary.get("occurredAt")
            service_plan = dictionary.get("servicePlan")
            status = dictionary.get("status")
            # Return an object of this model
            return cls(event_by,
                       event_type,
                       extended_attributes,
                       mdn,
                       msisdn,
                       occurred_at,
                       service_plan,
                       status)
