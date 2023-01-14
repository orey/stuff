# README

## Problem statement

The fact is in TexStudio, recent `oxt` linguistic resources for French seem not to work under Windows, which is quite ennoying. Indeed, the structure of recent French oxt files changed and is not recognized by TexStudio.

## Solution

A work around is this one:

* Get the last version of `hunspell` French dictionary. It will be a zip file.
* Rename it with `oxt` extension. Even is there is no manifest, te fact that the dictionary files are at the root of the zip seems of for TexSudio.
* Go to `TexStudio/Options/Configure TexStudio/Language Settings/Import Dictionary` and import the hunspell zip with `oxt` extension.
* Exit TexStudio and relaunch it.

Note: You can use the files attached in this folder.

