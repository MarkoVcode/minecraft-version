[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

## Usage:
```yaml
sensor:
  platform: minecraft-version
```

## Configuration variables:
Field | Default | Necessity | Description
--- | --- | --- | ---
platform | `minecraft-version` | *Required* | The platform name
name | Minecraft Version | Optional | The name of your sensor
state_type | latest | Optional | Type of version that will be displayed in the state of the sensor. **Types**: `latest`, `release`, `snapshot`
