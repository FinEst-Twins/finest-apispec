import connexion
import six

from swagger_server.models.inverter_reading import InverterReading  # noqa: E501
from swagger_server import util


def viikkisolar_observation_get(API_KEY, thing, minresulttime=None, maxresulttime=None, minphenomtime=None, maxphenomtime=None):  # noqa: E501
    """viikkisolar_observation_get

     # noqa: E501

    :param API_KEY: 
    :type API_KEY: str
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


def viikkisolar_observation_post(API_KEY=None, InverterReading=None):  # noqa: E501
    """adds observations from solar inverter to UoP

    adds observations from solar inverter to UoP # noqa: E501

    :param API_KEY: 
    :type API_KEY: str
    :param InverterReading: Observations from Sensors
    :type InverterReading: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        InverterReading = InverterReading.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
