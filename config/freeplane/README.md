# FreePlane tools

## Introduction

Those files are resources for [FreePlane](https://www.freeplane.org).

Root folder for FreePlane configuration: `C:\Users\Toto\AppData\Roaming\Freeplane\1.8.x\`

## Freeplane template

The template contains some styles that can be useful to structure large FreePlane files. Just put it in the `template` folder and the template will be proposed when creating a new file.

## Freeplane shortcuts

The `KeySet.properties` file must be included into a subfolder of the FreePlane installation. Under Windows, put in the `accelerator` folder:

```
C:\Users\Toto\AppData\Roaming\Freeplane\1.6.x\accelerators\KeySet.properties
```

You can create it if it does not exist. Then, in the UI, go to `Tools/Hot key preset/load/Thefile.properties`. That whould be good. See `OlivierKeySet.properties` as a sample.

## Customization for better ergonomy

* `Tools/Preferences/Appearance tab/Selection colors/Display selection nodes in bubbles`: check the box
* `Tools/Preferences/Behavior/Selection method/Selection method`: Select `By click`.

See the file `OlivierOptions.freeplane` loadable from  `Tools/Preferences`.
