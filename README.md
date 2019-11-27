### Usage:
```yaml
sensor:
  platform: minecraft_version
```

### Configuration variables:
Field | Default | Necessity | Description
--- | --- | --- | ---
platform | `minecraft_version` | *Required* | The platform name
name | Minecraft Version | Optional | The name of your sensor
state_type | latest | Optional | Type of version that will be displayed in the state of the sensor. **Types**: `latest`, `release`, `snapshot`
