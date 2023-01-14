# Firefox installation in hostile environment

Let's suppose you have to install FF in an hostile environment, e.g. without admin rights.

## Basic actions

Here are some actions that may work :

* Download FF setup executable file and unzip the executable file.
* Launch the `setup.exe` file inside and say `no` to the admin right questions.
* Choose `custom installation` and target a folder from where you can execute programs.

## Overriding the user agent

If an "official" browser is allowed in your environment, the firewall may block any different user agent. You'll have to make FF look as another browser by overriding the user agent.

You can check your used agent by going to numerous websites such as [this one](https://www.whatismybrowser.com/)

The procedure is the following :

* Type `about:config` in the address bar and say OK.
* Search for `general.useragent.override` key. Create it as a `String` if it does not exist.
* Go to [whatismybrowser.com](https://developers.whatismybrowser.com/useragents/?utm_source=whatismybrowsercom&utm_medium=internal&utm_campaign=breadcrumbs) or a site like this to get the user agent of the official browser. Paste it as the value of the key.

That should do the trick.

## Very hostile environment

You may have to use a local proxy to inherit from your Windows rights. In that context, you can use https://github.com/genotrance/px proxy and configure it in the setup of your FF.


