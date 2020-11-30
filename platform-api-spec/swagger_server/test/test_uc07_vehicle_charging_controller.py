# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestUC07VehicleChargingController(BaseTestCase):
    """UC07VehicleChargingController integration test stubs"""

    def test_ocpp_v16_observation_post(self):
        """Test case for ocpp_v16_observation_post

        adds observations from bus charging to UoP
        """
        headers = [('API_KEY', 'API_KEY_example')]
        response = self.client.open(
            '/FinEst-Twins/Finest-Platform-Services/1.0.0/ocpp/v16/observation',
            method='POST',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
