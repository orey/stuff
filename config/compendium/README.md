# Comments on the build of Compendium

## Source code

  * Source code: https://github.com/CompendiumNG/CompendiumNG
  * Wiki: https://github.com/CompendiumNG/CompendiumNG/wiki
  
## Complements

### Java

First of all, see the README file in the `stuff/config/java` folder.


### Gradle files

  * Compendium must have `tools.jar` in the class path to be built. The last built realized on my laptop was done with Open JDK 1.8 (see the java config section).
  * Think about the firewall by adding the ``gradle.properties` file with proxy information ([px](https://github.com/genotrance/px) would be a good choice).
  * In case of a problem downloading, there may be a certificate to add to the `cacerts` of the JRE you are using, at least the one related to the URL of the repo that fails

## Installer

The installer is pointing to the right JDK (`install-compendium.bat`).

