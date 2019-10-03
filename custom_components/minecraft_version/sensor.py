from datetime import timedelta
import urllib.request, json

import voluptuous as vol

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)

__version__ = '0.0.1'

CONF_NAME = 'name'
CONF_STATE_TYPE = 'state_type'

SCAN_INTERVAL = timedelta(minutes=20)

DEFAULT_SCAN_INTERVAL = timedelta(minutes=20)
DEFAULT_NAME = 'Minecraft Version'
DEFAULT_STATE_TYPE = 'latest'
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
        
        if (self._stateType == 'latest'):
            self._state = data['versions'][0]['id']
        elif (self._stateType == 'release' or self._stateType == 'snapshot'):
            self._state = data['latest'][self._stateType]
        else:
            self._state = 'Error'
        
        self._release = data['latest']['release']
        self._snapshot = data['latest']['snapshot']
    
    @property
    def state(self):
        return self._state
    
    @property
    def name(self):
        return self._name
    
    @property
    def icon(self):
        return ICON
    
    @property
    def device_state_attributes(self):
        return {
            'release': self._release,
            'snapshot': self._snapshot
        }
