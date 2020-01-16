# Minecraft Version

> A Home Assistant custom integration for tracking the Minecraft version

## Usage
```yaml
sensor:
  platform: minecraft-version
```

## Options
| Name         	|  Type  	|   Necessity  	|       Default       	| Description                                                                                                 	|
|--------------	|:------:	|:------------:	|:-------------------:	|-------------------------------------------------------------------------------------------------------------	|
| `platform`   	| string 	| **Required** 	| `minecraft-version` 	| The platform name                                                                                           	|
| `name`       	| string 	|   Optional   	| `Minecraft Version` 	| Custom name for the sensor                                                                                  	|
| `state_type` 	| string 	|   Optional   	|       `latest`      	| Type of version that will be displayed in the state of the sensor. Options: `latest`, `release`, `snapshot` 	|
