# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestUC06MovingVehicleController(BaseTestCase):
    """UC06MovingVehicleController integration test stubs"""

    def test_wrm247_v1_post(self):
        """Test case for wrm247_v1_post

        adds tractor movement observations to UoP
        """
        headers = [('API_KEY', 'API_KEY_example')]
        response = self.client.open(
            '/FinEst-Twins/Finest-Platform-Services/1.0.0/wrm247/v1',
            method='POST',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
