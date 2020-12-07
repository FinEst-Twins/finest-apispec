# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.noise_sensors import NoiseSensors  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUC01NoiseObservationController(BaseTestCase):
    """UC01NoiseObservationController integration test stubs"""

    def test_cesva_v1_observation_get(self):
        """Test case for cesva_v1_observation_get

        
        """
        query_string = [('thing', 'thing_example'),
                        ('minresulttime', '2013-10-20'),
                        ('maxresulttime', '2013-10-20'),
                        ('minphenomtime', '2013-10-20'),
                        ('maxphenomtime', '2013-10-20')]
        headers = [('IDENTITY_KEY', 'IDENTITY_KEY_example')]
        response = self.client.open(
            '/FinEst-Twins/Finest-Platform-Services/1.0.0/cesva/v1/observation',
            method='GET',
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cesva_v1_observation_put(self):
        """Test case for cesva_v1_observation_put

        adds noise observations to UoP
        """
        Sensors = NoiseSensors()
        headers = [('IDENTITY_KEY', 'IDENTITY_KEY_example')]
        response = self.client.open(
            '/FinEst-Twins/Finest-Platform-Services/1.0.0/cesva/v1/observation',
            method='PUT',
            data=json.dumps(Sensors),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
