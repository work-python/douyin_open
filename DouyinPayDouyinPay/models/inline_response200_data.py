# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse200Data(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ret_code': 'int',
        'ret_msg': 'str',
        'sub_code': 'int',
        'sub_msg': 'str',
        'pay_order_no': 'str',
        'remark': 'str',
        'pay_create_time': 'int',
        'pay_finish_time': 'int'
    }

    attribute_map = {
        'ret_code': 'ret_code',
        'ret_msg': 'ret_msg',
        'sub_code': 'sub_code',
        'sub_msg': 'sub_msg',
        'pay_order_no': 'pay_order_no',
        'remark': 'remark',
        'pay_create_time': 'pay_create_time',
        'pay_finish_time': 'pay_finish_time'
    }

    def __init__(self, ret_code=None, ret_msg=None, sub_code=None, sub_msg=None, pay_order_no=None, remark=None, pay_create_time=None, pay_finish_time=None):  # noqa: E501
        """InlineResponse200Data - a model defined in Swagger"""  # noqa: E501
        self._ret_code = None
        self._ret_msg = None
        self._sub_code = None
        self._sub_msg = None
        self._pay_order_no = None
        self._remark = None
        self._pay_create_time = None
        self._pay_finish_time = None
        self.discriminator = None
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.sub_code = sub_code
        self.sub_msg = sub_msg
        self.pay_order_no = pay_order_no
        self.remark = remark
        self.pay_create_time = pay_create_time
        self.pay_finish_time = pay_finish_time

    @property
    def ret_code(self):
        """Gets the ret_code of this InlineResponse200Data.  # noqa: E501

        返回码  # noqa: E501

        :return: The ret_code of this InlineResponse200Data.  # noqa: E501
        :rtype: int
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        """Sets the ret_code of this InlineResponse200Data.

        返回码  # noqa: E501

        :param ret_code: The ret_code of this InlineResponse200Data.  # noqa: E501
        :type: int
        """
        if ret_code is None:
            raise ValueError("Invalid value for `ret_code`, must not be `None`")  # noqa: E501

        self._ret_code = ret_code

    @property
    def ret_msg(self):
        """Gets the ret_msg of this InlineResponse200Data.  # noqa: E501

        返回信息  # noqa: E501

        :return: The ret_msg of this InlineResponse200Data.  # noqa: E501
        :rtype: str
        """
        return self._ret_msg

    @ret_msg.setter
    def ret_msg(self, ret_msg):
        """Sets the ret_msg of this InlineResponse200Data.

        返回信息  # noqa: E501

        :param ret_msg: The ret_msg of this InlineResponse200Data.  # noqa: E501
        :type: str
        """
        if ret_msg is None:
            raise ValueError("Invalid value for `ret_msg`, must not be `None`")  # noqa: E501

        self._ret_msg = ret_msg

    @property
    def sub_code(self):
        """Gets the sub_code of this InlineResponse200Data.  # noqa: E501

        返回码  # noqa: E501

        :return: The sub_code of this InlineResponse200Data.  # noqa: E501
        :rtype: int
        """
        return self._sub_code

    @sub_code.setter
    def sub_code(self, sub_code):
        """Sets the sub_code of this InlineResponse200Data.

        返回码  # noqa: E501

        :param sub_code: The sub_code of this InlineResponse200Data.  # noqa: E501
        :type: int
        """
        if sub_code is None:
            raise ValueError("Invalid value for `sub_code`, must not be `None`")  # noqa: E501

        self._sub_code = sub_code

    @property
    def sub_msg(self):
        """Gets the sub_msg of this InlineResponse200Data.  # noqa: E501

        返回信息  # noqa: E501

        :return: The sub_msg of this InlineResponse200Data.  # noqa: E501
        :rtype: str
        """
        return self._sub_msg

    @sub_msg.setter
    def sub_msg(self, sub_msg):
        """Sets the sub_msg of this InlineResponse200Data.

        返回信息  # noqa: E501

        :param sub_msg: The sub_msg of this InlineResponse200Data.  # noqa: E501
        :type: str
        """
        if sub_msg is None:
            raise ValueError("Invalid value for `sub_msg`, must not be `None`")  # noqa: E501

        self._sub_msg = sub_msg

    @property
    def pay_order_no(self):
        """Gets the pay_order_no of this InlineResponse200Data.  # noqa: E501

        内部订单号  # noqa: E501

        :return: The pay_order_no of this InlineResponse200Data.  # noqa: E501
        :rtype: str
        """
        return self._pay_order_no

    @pay_order_no.setter
    def pay_order_no(self, pay_order_no):
        """Sets the pay_order_no of this InlineResponse200Data.

        内部订单号  # noqa: E501

        :param pay_order_no: The pay_order_no of this InlineResponse200Data.  # noqa: E501
        :type: str
        """
        if pay_order_no is None:
            raise ValueError("Invalid value for `pay_order_no`, must not be `None`")  # noqa: E501

        self._pay_order_no = pay_order_no

    @property
    def remark(self):
        """Gets the remark of this InlineResponse200Data.  # noqa: E501

        标记，长度小于512  # noqa: E501

        :return: The remark of this InlineResponse200Data.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this InlineResponse200Data.

        标记，长度小于512  # noqa: E501

        :param remark: The remark of this InlineResponse200Data.  # noqa: E501
        :type: str
        """
        if remark is None:
            raise ValueError("Invalid value for `remark`, must not be `None`")  # noqa: E501

        self._remark = remark

    @property
    def pay_create_time(self):
        """Gets the pay_create_time of this InlineResponse200Data.  # noqa: E501

        开始时间  # noqa: E501

        :return: The pay_create_time of this InlineResponse200Data.  # noqa: E501
        :rtype: int
        """
        return self._pay_create_time

    @pay_create_time.setter
    def pay_create_time(self, pay_create_time):
        """Sets the pay_create_time of this InlineResponse200Data.

        开始时间  # noqa: E501

        :param pay_create_time: The pay_create_time of this InlineResponse200Data.  # noqa: E501
        :type: int
        """
        if pay_create_time is None:
            raise ValueError("Invalid value for `pay_create_time`, must not be `None`")  # noqa: E501

        self._pay_create_time = pay_create_time

    @property
    def pay_finish_time(self):
        """Gets the pay_finish_time of this InlineResponse200Data.  # noqa: E501

        结束时间  # noqa: E501

        :return: The pay_finish_time of this InlineResponse200Data.  # noqa: E501
        :rtype: int
        """
        return self._pay_finish_time

    @pay_finish_time.setter
    def pay_finish_time(self, pay_finish_time):
        """Sets the pay_finish_time of this InlineResponse200Data.

        结束时间  # noqa: E501

        :param pay_finish_time: The pay_finish_time of this InlineResponse200Data.  # noqa: E501
        :type: int
        """
        if pay_finish_time is None:
            raise ValueError("Invalid value for `pay_finish_time`, must not be `None`")  # noqa: E501

        self._pay_finish_time = pay_finish_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse200Data, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
