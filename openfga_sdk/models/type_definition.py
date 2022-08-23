# coding: utf-8

"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openfga_sdk.configuration import Configuration


class TypeDefinition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'relations': 'dict(str, Userset)',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'type': 'type',
        'relations': 'relations',
        'metadata': 'metadata'
    }

    def __init__(self, type=None, relations=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """TypeDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._relations = None
        self._metadata = None
        self.discriminator = None

        self.type = type
        if relations is not None:
            self.relations = relations
        if metadata is not None:
            self.metadata = metadata

    @property
    def type(self):
        """Gets the type of this TypeDefinition.  # noqa: E501


        :return: The type of this TypeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TypeDefinition.


        :param type: The type of this TypeDefinition.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def relations(self):
        """Gets the relations of this TypeDefinition.  # noqa: E501


        :return: The relations of this TypeDefinition.  # noqa: E501
        :rtype: dict(str, Userset)
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this TypeDefinition.


        :param relations: The relations of this TypeDefinition.  # noqa: E501
        :type relations: dict(str, Userset)
        """

        self._relations = relations

    @property
    def metadata(self):
        """Gets the metadata of this TypeDefinition.  # noqa: E501


        :return: The metadata of this TypeDefinition.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TypeDefinition.


        :param metadata: The metadata of this TypeDefinition.  # noqa: E501
        :type metadata: Metadata
        """

        self._metadata = metadata

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TypeDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypeDefinition):
            return True

        return self.to_dict() != other.to_dict()