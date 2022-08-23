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


class Node(object):
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
        'name': 'str',
        'leaf': 'Leaf',
        'difference': 'UsersetTreeDifference',
        'union': 'Nodes',
        'intersection': 'Nodes'
    }

    attribute_map = {
        'name': 'name',
        'leaf': 'leaf',
        'difference': 'difference',
        'union': 'union',
        'intersection': 'intersection'
    }

    def __init__(self, name=None, leaf=None, difference=None, union=None, intersection=None, local_vars_configuration=None):  # noqa: E501
        """Node - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._leaf = None
        self._difference = None
        self._union = None
        self._intersection = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if leaf is not None:
            self.leaf = leaf
        if difference is not None:
            self.difference = difference
        if union is not None:
            self.union = union
        if intersection is not None:
            self.intersection = intersection

    @property
    def name(self):
        """Gets the name of this Node.  # noqa: E501


        :return: The name of this Node.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.


        :param name: The name of this Node.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def leaf(self):
        """Gets the leaf of this Node.  # noqa: E501


        :return: The leaf of this Node.  # noqa: E501
        :rtype: Leaf
        """
        return self._leaf

    @leaf.setter
    def leaf(self, leaf):
        """Sets the leaf of this Node.


        :param leaf: The leaf of this Node.  # noqa: E501
        :type leaf: Leaf
        """

        self._leaf = leaf

    @property
    def difference(self):
        """Gets the difference of this Node.  # noqa: E501


        :return: The difference of this Node.  # noqa: E501
        :rtype: UsersetTreeDifference
        """
        return self._difference

    @difference.setter
    def difference(self, difference):
        """Sets the difference of this Node.


        :param difference: The difference of this Node.  # noqa: E501
        :type difference: UsersetTreeDifference
        """

        self._difference = difference

    @property
    def union(self):
        """Gets the union of this Node.  # noqa: E501


        :return: The union of this Node.  # noqa: E501
        :rtype: Nodes
        """
        return self._union

    @union.setter
    def union(self, union):
        """Sets the union of this Node.


        :param union: The union of this Node.  # noqa: E501
        :type union: Nodes
        """

        self._union = union

    @property
    def intersection(self):
        """Gets the intersection of this Node.  # noqa: E501


        :return: The intersection of this Node.  # noqa: E501
        :rtype: Nodes
        """
        return self._intersection

    @intersection.setter
    def intersection(self, intersection):
        """Sets the intersection of this Node.


        :param intersection: The intersection of this Node.  # noqa: E501
        :type intersection: Nodes
        """

        self._intersection = intersection

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
        if not isinstance(other, Node):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Node):
            return True

        return self.to_dict() != other.to_dict()