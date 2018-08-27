## Introduction

These are the most basic commands I need to work with emacs.

## Basic commands

  * C-x C-r: recent files
	* To activate this option, an option must be set in the .emacs file (located at the root of the home directory in Debian 9.x)
  * C-x C-f: open file/create file
  * C-x k: close file (kill)
  * C-x C-s: save file
  * C-x C-w: save as

  * Aborting a command: esc esc esc
  * Listing all buffers: C-x C-b
  * Change size of font in Emacs: C-x C-+ / C-x C--
  
  * Visual line mode, to wrap lines not cutting words: M-x visual-line-mode
  * To remove wrapping: M-x toggle-truncate-lines
  
  * Changing the encoding of the file: C-x C-m f
  
  * Undo: C-/ or C-x u
  * Redo: C-_

  * Quit: C-x C-c

## Window management

Split windows

  * In 2 horizontally: C-x 2
  * In 2 vertically: C-x 3

  * Delete window: C-x 0
  * Delete all other windows: C-x 1

  * Go to another window: C-x o

## Copy-paste

  * Start of selection: C-space
  * Copy: M-w
  * Cut: C-w
  * Paste: C-y

## Modes

Major modes

  * Javascript: M-x js-mode
  * Line numbers: M-x linum-mode (can be automated, see <.emacs>)

### Latex mode

M-x latex-mode

Two commands to know when editing:

  * C-c C-o env-name: creates the `begin` and `end` of the environments
  * C-o C-e: ends the current not ended environment
  * C-c {: creates {}
  * C-c }: matches with the recent open {

To activate spellcheck under Linux:

  * Enter into flyspell-mode: M-X flyspell-mode
  * M-$: to enter into the dictionary recommendations

### Markdown mode

To enter the mode (is automatic when correctly installed)

  * Markdown: M-x markdown-mode
  
Insert

  * C-c C-l: Insert link
  * C-c C-i: Insert image
  * C-c C-s -: horizontal rule
  * C-c C-s f: footnote

Formatting:

  * C-c C-s i: italic
  * C-c C-s b: bold
  * C-c C-s c: online code
  * C-c C-s q: block quote
  
Headings:

  * C-c C-s h: automatic
  * C-c C-s 1 to 6: header level

-------------------------------------------------------------------------------

## Installation comments

### Markdown nstallation

Note: Markdown must be installed
https://jblevins.org/projects/markdown-mode/ for installation instructions

### Portable version of Emacs on Windows 10

Note: Under Windows 10, for a portable version of Emacs, I could not install the package automatically. Adding the Melpa source does not work. I downloaded the `markdown-2.3.el` file and did a manual install from file

  * M-x package-install-from-file FILE
  
That worked.

### Install through Cygwin

All works well for the Cywin install.

### Python mode

Under Windows 10, I had some cursor problems with Python formatting (Emacs portable installation)

To be retested with Gygwin installation.

-------------------------------------------------------------------------------

## Customizations of the .emacs file

Please see the .emacs file sample attached.




