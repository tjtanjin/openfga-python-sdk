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


class AuthorizationModel(object):
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
        'id': 'str',
        'schema_version': 'str',
        'type_definitions': 'list[TypeDefinition]'
    }

    attribute_map = {
        'id': 'id',
        'schema_version': 'schema_version',
        'type_definitions': 'type_definitions'
    }

    def __init__(self, id=None, schema_version=None, type_definitions=None, local_vars_configuration=None):  # noqa: E501
        """AuthorizationModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._schema_version = None
        self._type_definitions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if schema_version is not None:
            self.schema_version = schema_version
        if type_definitions is not None:
            self.type_definitions = type_definitions

    @property
    def id(self):
        """Gets the id of this AuthorizationModel.  # noqa: E501


        :return: The id of this AuthorizationModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthorizationModel.


        :param id: The id of this AuthorizationModel.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def schema_version(self):
        """Gets the schema_version of this AuthorizationModel.  # noqa: E501


        :return: The schema_version of this AuthorizationModel.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this AuthorizationModel.


        :param schema_version: The schema_version of this AuthorizationModel.  # noqa: E501
        :type schema_version: str
        """

        self._schema_version = schema_version

    @property
    def type_definitions(self):
        """Gets the type_definitions of this AuthorizationModel.  # noqa: E501


        :return: The type_definitions of this AuthorizationModel.  # noqa: E501
        :rtype: list[TypeDefinition]
        """
        return self._type_definitions

    @type_definitions.setter
    def type_definitions(self, type_definitions):
        """Sets the type_definitions of this AuthorizationModel.


        :param type_definitions: The type_definitions of this AuthorizationModel.  # noqa: E501
        :type type_definitions: list[TypeDefinition]
        """

        self._type_definitions = type_definitions

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
        if not isinstance(other, AuthorizationModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthorizationModel):
            return True

        return self.to_dict() != other.to_dict()