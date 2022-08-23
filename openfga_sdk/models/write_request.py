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


class WriteRequest(object):
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
        'writes': 'TupleKeys',
        'deletes': 'TupleKeys',
        'authorization_model_id': 'str'
    }

    attribute_map = {
        'writes': 'writes',
        'deletes': 'deletes',
        'authorization_model_id': 'authorization_model_id'
    }

    def __init__(self, writes=None, deletes=None, authorization_model_id=None, local_vars_configuration=None):  # noqa: E501
        """WriteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._writes = None
        self._deletes = None
        self._authorization_model_id = None
        self.discriminator = None

        if writes is not None:
            self.writes = writes
        if deletes is not None:
            self.deletes = deletes
        if authorization_model_id is not None:
            self.authorization_model_id = authorization_model_id

    @property
    def writes(self):
        """Gets the writes of this WriteRequest.  # noqa: E501


        :return: The writes of this WriteRequest.  # noqa: E501
        :rtype: TupleKeys
        """
        return self._writes

    @writes.setter
    def writes(self, writes):
        """Sets the writes of this WriteRequest.


        :param writes: The writes of this WriteRequest.  # noqa: E501
        :type writes: TupleKeys
        """

        self._writes = writes

    @property
    def deletes(self):
        """Gets the deletes of this WriteRequest.  # noqa: E501


        :return: The deletes of this WriteRequest.  # noqa: E501
        :rtype: TupleKeys
        """
        return self._deletes

    @deletes.setter
    def deletes(self, deletes):
        """Sets the deletes of this WriteRequest.


        :param deletes: The deletes of this WriteRequest.  # noqa: E501
        :type deletes: TupleKeys
        """

        self._deletes = deletes

    @property
    def authorization_model_id(self):
        """Gets the authorization_model_id of this WriteRequest.  # noqa: E501


        :return: The authorization_model_id of this WriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorization_model_id

    @authorization_model_id.setter
    def authorization_model_id(self, authorization_model_id):
        """Sets the authorization_model_id of this WriteRequest.


        :param authorization_model_id: The authorization_model_id of this WriteRequest.  # noqa: E501
        :type authorization_model_id: str
        """

        self._authorization_model_id = authorization_model_id

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
        if not isinstance(other, WriteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WriteRequest):
            return True

        return self.to_dict() != other.to_dict()