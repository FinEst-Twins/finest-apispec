import connexion
import six

from swagger_server.models.noise_sensors import NoiseSensors  # noqa: E501
from swagger_server import util


def cesva_v1_observation_get(IDENTITY_KEY, thing, minresulttime=None, maxresulttime=None, minphenomtime=None, maxphenomtime=None):  # noqa: E501
    """cesva_v1_observation_get

     # noqa: E501

    :param IDENTITY_KEY: 
    :type IDENTITY_KEY: str
    :param thing: name of the device
    :type thing: str
    :param minresulttime: time at which observation data was received at the data platform
    :type minresulttime: str
    :param maxresulttime: time at which observation data was received at the data platform
    :type maxresulttime: str
    :param minphenomtime: sampling time recorded and received with observation data
    :type minphenomtime: str
    :param maxphenomtime: sampling time recorded and received with observation data
    :type maxphenomtime: str

    :rtype: None
    """
    minresulttime = util.deserialize_date(minresulttime)
    maxresulttime = util.deserialize_date(maxresulttime)
    minphenomtime = util.deserialize_date(minphenomtime)
    maxphenomtime = util.deserialize_date(maxphenomtime)
    return 'do some magic!'


def cesva_v1_observation_put(IDENTITY_KEY=None, Sensors=None):  # noqa: E501
    """adds noise observations to UoP

     # noqa: E501

    :param IDENTITY_KEY: 
    :type IDENTITY_KEY: str
    :param Sensors: Observations from Sensors
    :type Sensors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Sensors = NoiseSensors.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
