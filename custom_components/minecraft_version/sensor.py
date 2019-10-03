from datetime import timedelta
import urllib.request, json

import logging
import voluptuous as vol

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)

__version__ = '0.0.1'
_LOGGER = logging.getLogger(__name__)

CONF_NAME = 'name'
CONF_STATE_TYPE = 'state_type'

SCAN_INTERVAL = timedelta(minutes=20)

DEFAULT_SCAN_INTERVAL = timedelta(minutes=20)
DEFAULT_NAME = 'Minecraft Version'
DEFAULT_STATE_TYPE = 'release'
ICON = 'mdi:minecraft'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_STATE_TYPE, default=DEFAULT_STATE_TYPE): cv.string
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([MinecraftVersionSensor(hass, config)])

class MinecraftVersionSensor(Entity):
    def __init__(self, hass, config):
        self.hass = hass
        self._name = config[CONF_NAME]
        self._stateType = config[CONF_STATE_TYPE]
        self._release = None
        self._snapshot = None
        self._state = None
        self.update()
    
    def update(self):
        with urllib.request.urlopen('https://launchermeta.mojang.com/mc/game/version_manifest.json') as url:
            data = json.loads(url.read().decode())
            self._state = data['latest'][self._stateType]
            self._release = data['latest']['release']
            self._snapshot = data['latest']['snapshot']
    
    @property
    def state(self):
        return self._stateType
    
    @property
    def name(self):
        return self._name
    
    @property
    def icon(self):
        return self.ICON
    
    @property
    def device_state_attributes(self):
        return {
            'release': self._release,
            'snapshot': self._snapshot
        }
