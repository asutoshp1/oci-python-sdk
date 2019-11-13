# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .rule_condition import RuleCondition
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PathMatchCondition(RuleCondition):
    """
    The path string and match condition to apply when evaluating an incoming URI for redirection.
    """

    #: A constant which can be used with the operator property of a PathMatchCondition.
    #: This constant has a value of "EXACT_MATCH"
    OPERATOR_EXACT_MATCH = "EXACT_MATCH"

    #: A constant which can be used with the operator property of a PathMatchCondition.
    #: This constant has a value of "FORCE_LONGEST_PREFIX_MATCH"
    OPERATOR_FORCE_LONGEST_PREFIX_MATCH = "FORCE_LONGEST_PREFIX_MATCH"

    #: A constant which can be used with the operator property of a PathMatchCondition.
    #: This constant has a value of "PREFIX_MATCH"
    OPERATOR_PREFIX_MATCH = "PREFIX_MATCH"

    #: A constant which can be used with the operator property of a PathMatchCondition.
    #: This constant has a value of "SUFFIX_MATCH"
    OPERATOR_SUFFIX_MATCH = "SUFFIX_MATCH"

    def __init__(self, **kwargs):
        """
        Initializes a new PathMatchCondition object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.PathMatchCondition.attribute_name` attribute
        of this class is ``PATH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this PathMatchCondition.
            Allowed values for this property are: "SOURCE_IP_ADDRESS", "SOURCE_VCN_ID", "SOURCE_VCN_IP_ADDRESS", "PATH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attribute_name: str

        :param attribute_value:
            The value to assign to the attribute_value property of this PathMatchCondition.
        :type attribute_value: str

        :param operator:
            The value to assign to the operator property of this PathMatchCondition.
            Allowed values for this property are: "EXACT_MATCH", "FORCE_LONGEST_PREFIX_MATCH", "PREFIX_MATCH", "SUFFIX_MATCH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operator: str

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_value': 'str',
            'operator': 'str'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName',
            'attribute_value': 'attributeValue',
            'operator': 'operator'
        }

        self._attribute_name = None
        self._attribute_value = None
        self._operator = None
        self._attribute_name = 'PATH'

    @property
    def attribute_value(self):
        """
        **[Required]** Gets the attribute_value of this PathMatchCondition.
        The path string that the redirection rule applies to.

        Example: `/example`


        :return: The attribute_value of this PathMatchCondition.
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """
        Sets the attribute_value of this PathMatchCondition.
        The path string that the redirection rule applies to.

        Example: `/example`


        :param attribute_value: The attribute_value of this PathMatchCondition.
        :type: str
        """
        self._attribute_value = attribute_value

    @property
    def operator(self):
        """
        **[Required]** Gets the operator of this PathMatchCondition.
        A string that specifies how to compare the PathMatchCondition object's `attributeValue` string to the
        incoming URI.

        *  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string.

        *  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best,
           longest match of the beginning portion of the incoming URI path.

        *  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the
           `attributeValue` string.

        *  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue`
           string.

        Allowed values for this property are: "EXACT_MATCH", "FORCE_LONGEST_PREFIX_MATCH", "PREFIX_MATCH", "SUFFIX_MATCH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operator of this PathMatchCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this PathMatchCondition.
        A string that specifies how to compare the PathMatchCondition object's `attributeValue` string to the
        incoming URI.

        *  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string.

        *  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best,
           longest match of the beginning portion of the incoming URI path.

        *  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the
           `attributeValue` string.

        *  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue`
           string.


        :param operator: The operator of this PathMatchCondition.
        :type: str
        """
        allowed_values = ["EXACT_MATCH", "FORCE_LONGEST_PREFIX_MATCH", "PREFIX_MATCH", "SUFFIX_MATCH"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            operator = 'UNKNOWN_ENUM_VALUE'
        self._operator = operator

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
