# Minecraft-Version

_Minecraft latest released version checker for Home Assistant!_

## Usage:

```yaml
sensor:
  platform: minecraft_version
```

## Configuration variables:
  
Field | Value | Necessity | Description
--- | --- | --- | ---
platform | `minecraft_version` | *Required* | The platform name
name | Minecraft Version | Optional | The name of your sensor
state_type | **release** or **snapshot** | Optional | Type of version that will be displayed in the state of the sensor
