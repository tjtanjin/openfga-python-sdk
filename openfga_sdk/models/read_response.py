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


class ReadResponse(object):
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
        'tuples': 'list[Tuple]',
        'continuation_token': 'str'
    }

    attribute_map = {
        'tuples': 'tuples',
        'continuation_token': 'continuation_token'
    }

    def __init__(self, tuples=None, continuation_token=None, local_vars_configuration=None):  # noqa: E501
        """ReadResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tuples = None
        self._continuation_token = None
        self.discriminator = None

        if tuples is not None:
            self.tuples = tuples
        if continuation_token is not None:
            self.continuation_token = continuation_token

    @property
    def tuples(self):
        """Gets the tuples of this ReadResponse.  # noqa: E501


        :return: The tuples of this ReadResponse.  # noqa: E501
        :rtype: list[Tuple]
        """
        return self._tuples

    @tuples.setter
    def tuples(self, tuples):
        """Sets the tuples of this ReadResponse.


        :param tuples: The tuples of this ReadResponse.  # noqa: E501
        :type tuples: list[Tuple]
        """

        self._tuples = tuples

    @property
    def continuation_token(self):
        """Gets the continuation_token of this ReadResponse.  # noqa: E501


        :return: The continuation_token of this ReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this ReadResponse.


        :param continuation_token: The continuation_token of this ReadResponse.  # noqa: E501
        :type continuation_token: str
        """

        self._continuation_token = continuation_token

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
        if not isinstance(other, ReadResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadResponse):
            return True

        return self.to_dict() != other.to_dict()