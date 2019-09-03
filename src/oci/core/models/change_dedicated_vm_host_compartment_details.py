# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeDedicatedVmHostCompartmentDetails(object):
    """
    Contains details indicating which compartment the resource should move to
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeDedicatedVmHostCompartmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ChangeDedicatedVmHostCompartmentDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId'
        }

        self._compartment_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ChangeDedicatedVmHostCompartmentDetails.
        The `OCID`__ of the compartment
        into which the resource should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ChangeDedicatedVmHostCompartmentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ChangeDedicatedVmHostCompartmentDetails.
        The `OCID`__ of the compartment
        into which the resource should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ChangeDedicatedVmHostCompartmentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other