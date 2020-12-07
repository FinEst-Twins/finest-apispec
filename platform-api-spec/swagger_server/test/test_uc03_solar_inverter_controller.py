# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inverter_reading import InverterReading  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUC03SolarInverterController(BaseTestCase):
    """UC03SolarInverterController integration test stubs"""

    def test_viikkisolar_observation_get(self):
        """Test case for viikkisolar_observation_get

        
        """
        query_string = [('thing', 'thing_example'),
                        ('minresulttime', '2013-10-20'),
                        ('maxresulttime', '2013-10-20'),
                        ('minphenomtime', '2013-10-20'),
                        ('maxphenomtime', '2013-10-20')]
        headers = [('API_KEY', 'API_KEY_example')]
        response = self.client.open(
            '/FinEst-Twins/Finest-Platform-Services/1.0.0/viikkisolar/observation',
            method='GET',
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_viikkisolar_observation_post(self):
        """Test case for viikkisolar_observation_post

        adds observations from solar inverter to UoP
        """
        InverterReading = InverterReading()
        headers = [('API_KEY', 'API_KEY_example')]
        response = self.client.open(
            '/FinEst-Twins/Finest-Platform-Services/1.0.0/viikkisolar/observation',
            method='POST',
            data=json.dumps(InverterReading),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
