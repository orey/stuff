# split-and-convert-ape-and-flac-to-mp3
Linux script to split and convert APE and Flac big files files to MP3

## Usage

Type the script name for the usage

```
$ ./convert.sh
```

Will output:

```
convert.sh: Script version 2 - take in charge big ape or flac files
Usage : convert.sh [name-of-cue-without-extension] [type]
- type can be [ape] or [flac]
Try not to use spaces in parameters
```

## Script functionality

The script expects:

 * The APE/FLAC name of the file to be the same than the name of the CUE file
 * The APE/FLAC and CUE files to be located here (.)
 
It will:

 * Create or reuse a "\_converted" directory
 * Split the APE/FLAC big file with the CUE file
 * Convert all the files to WAV
 * Convert all the files to MP3

## Dependencies

Packages required:

 * cuetools
 * flac
 * lame
 * shntool
 * and the monkeys audio codec [mac](http://www.deb-multimedia.org/)

## Installation of mac

1. Update your /etc/apt/sources.list with:

```
deb https://www.deb-multimedia.org sid main non-free
```

2. Update list of packages and install codec

The update must be done with the insecure option because the source repo does not provide any public key.

```
$ sudo apt update -oAcquire::AllowInsecureRepositories=true
$ sudo apt install monkeys-audio
```

3. Then remove the source from your sources.list

```
# deb https://www.deb-multimedia.org sid main non-free
```

