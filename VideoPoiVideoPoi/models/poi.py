# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Poi(object):
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
        'poi_id': 'str',
        'poi_name': 'str',
        'location': 'str',
        'country': 'str',
        'country_code': 'str',
        'province': 'str',
        'city': 'str',
        'city_code': 'str',
        'district': 'str',
        'address': 'str'
    }

    attribute_map = {
        'poi_id': 'poi_id',
        'poi_name': 'poi_name',
        'location': 'location',
        'country': 'country',
        'country_code': 'country_code',
        'province': 'province',
        'city': 'city',
        'city_code': 'city_code',
        'district': 'district',
        'address': 'address'
    }

    def __init__(self, poi_id=None, poi_name=None, location=None, country=None, country_code=None, province=None, city=None, city_code=None, district=None, address=None):  # noqa: E501
        """Poi - a model defined in Swagger"""  # noqa: E501
        self._poi_id = None
        self._poi_name = None
        self._location = None
        self._country = None
        self._country_code = None
        self._province = None
        self._city = None
        self._city_code = None
        self._district = None
        self._address = None
        self.discriminator = None
        self.poi_id = poi_id
        self.poi_name = poi_name
        self.location = location
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if city_code is not None:
            self.city_code = city_code
        if district is not None:
            self.district = district
        if address is not None:
            self.address = address

    @property
    def poi_id(self):
        """Gets the poi_id of this Poi.  # noqa: E501

        唯一ID  # noqa: E501

        :return: The poi_id of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._poi_id

    @poi_id.setter
    def poi_id(self, poi_id):
        """Sets the poi_id of this Poi.

        唯一ID  # noqa: E501

        :param poi_id: The poi_id of this Poi.  # noqa: E501
        :type: str
        """
        if poi_id is None:
            raise ValueError("Invalid value for `poi_id`, must not be `None`")  # noqa: E501

        self._poi_id = poi_id

    @property
    def poi_name(self):
        """Gets the poi_name of this Poi.  # noqa: E501

        名称  # noqa: E501

        :return: The poi_name of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._poi_name

    @poi_name.setter
    def poi_name(self, poi_name):
        """Sets the poi_name of this Poi.

        名称  # noqa: E501

        :param poi_name: The poi_name of this Poi.  # noqa: E501
        :type: str
        """
        if poi_name is None:
            raise ValueError("Invalid value for `poi_name`, must not be `None`")  # noqa: E501

        self._poi_name = poi_name

    @property
    def location(self):
        """Gets the location of this Poi.  # noqa: E501

        经纬度，格式：X,Y  # noqa: E501

        :return: The location of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Poi.

        经纬度，格式：X,Y  # noqa: E501

        :param location: The location of this Poi.  # noqa: E501
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def country(self):
        """Gets the country of this Poi.  # noqa: E501

        国家  # noqa: E501

        :return: The country of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Poi.

        国家  # noqa: E501

        :param country: The country of this Poi.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this Poi.  # noqa: E501

        国家编码  # noqa: E501

        :return: The country_code of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Poi.

        国家编码  # noqa: E501

        :param country_code: The country_code of this Poi.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def province(self):
        """Gets the province of this Poi.  # noqa: E501

        省份  # noqa: E501

        :return: The province of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this Poi.

        省份  # noqa: E501

        :param province: The province of this Poi.  # noqa: E501
        :type: str
        """

        self._province = province

    @property
    def city(self):
        """Gets the city of this Poi.  # noqa: E501

        城市  # noqa: E501

        :return: The city of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Poi.

        城市  # noqa: E501

        :param city: The city of this Poi.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def city_code(self):
        """Gets the city_code of this Poi.  # noqa: E501

        城市编码  # noqa: E501

        :return: The city_code of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._city_code

    @city_code.setter
    def city_code(self, city_code):
        """Sets the city_code of this Poi.

        城市编码  # noqa: E501

        :param city_code: The city_code of this Poi.  # noqa: E501
        :type: str
        """

        self._city_code = city_code

    @property
    def district(self):
        """Gets the district of this Poi.  # noqa: E501

        区域名称  # noqa: E501

        :return: The district of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this Poi.

        区域名称  # noqa: E501

        :param district: The district of this Poi.  # noqa: E501
        :type: str
        """

        self._district = district

    @property
    def address(self):
        """Gets the address of this Poi.  # noqa: E501

        地址  # noqa: E501

        :return: The address of this Poi.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Poi.

        地址  # noqa: E501

        :param address: The address of this Poi.  # noqa: E501
        :type: str
        """

        self._address = address

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
        if issubclass(Poi, dict):
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
        if not isinstance(other, Poi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other