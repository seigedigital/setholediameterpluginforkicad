# ![icon](resources/icon.png) Set Hole Diameter plugin for KiCad

## Description
The `Set Hole Diameter` plugin is a KiCad action plugin that sets the hole diameter of all pads in the PCB to a unique size. The default value is 0.8mm. 

**Why?** When manufacturing and drilling PCBs by hand, it can happen that holes are drilled that are smaller than the holes in the original footprints. In this case, drilling leaves a small ring of PCB base material without copper around the hole. This will cause problems when soldering. Setting all holes to a minimum diameter will ensure that each hole is surrounded by copper.

## Installation

### Automatic Installation (recommended)

The plugin is available in KiCad's Repo. Just search for it and install it.

<img width="1034" alt="image" src="https://github.com/user-attachments/assets/2f004620-2a85-4769-84a4-ef7b8f1d953a">

### Manual Installation

1. Clone this repository or download the latest release.
2. Copy the `plugins` subdirectory to your KiCad plugins directory. eg
   
```
cp -rp plugins <your_kicad_plugin_directory>/com_github_seigedigital_setholediameterpluginforkicad
```

3. Restart KiCad or use `Tools > External Plugins > Refresh Plugins` from the PCB Editors menu

## Usage
1. Open your PCB project in the KiCad PCB editor.
2. Go to `Tools > External Plugins > Set Hole Diameter` to run the plugin.

## License
This project is licensed under the GNU GPL Version 3 License - see the [LICENSE](LICENSE) file for details.

## Author
Leander Seige, seige.digital GbR
