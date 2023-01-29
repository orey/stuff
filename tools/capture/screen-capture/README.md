## Screen capture small script in Python3

This file is a small screen capture script using [Python MSS](https://python-mss.readthedocs.io/index.html).

## Usage

You have to provide your root folder inside the script itself.

When launched, the script is asking you for the subfolder in which it can put the screenshots. The same of the screenshot is a time stamp with fractions of seconds, so you can shot many times.

## Versions

Version 6 is the last stable version.

Versions 8 is trying to add a thumbnail view in order to make it work better in an org-mode context, but it is not satisfying yet. The best solution I found is more to use version 6 and use the `noinlineimages` indicator in the startup section of the page:

```
#+STARTUP: noinlineimages
```

Like that, the v6 brings you the links on the clipboard that you can copy easily in Emacs org-mode file, and then using the C-C C-O command, you can access on the image quite easily on another panel. That can be interesting especially when your images are big.

