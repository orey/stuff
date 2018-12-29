; .Emacs file for Debian 9

;==== For markdown support
; If it does not work: apt install elpa-markdown-mode markdown
(require 'package)
(add-to-list 'package-archives
    '("melpa-stable" . "https://stable.melpa.org/packages/"))
(package-initialize)

;=== Enabling line numbers globally to emacs
(when (version<= "26.0.50" emacs-version )
    (global-display-line-numbers-mode))

;=== Enabling recent files
(recentf-mode 1)
(setq recentf-max-menu-items 25)
(global-set-key "\C-x\ \C-r" 'recentf-open-files)

;=== Default fonts
(add-to-list 'default-frame-alist '(font . "DejaVu Sans Mono-9"))
(set-face-attribute 'default t :font "DejaVu Sans Mono-9")

(set-face-attribute 'default nil :font "DejaVu Sans Mono-9")
(set-frame-font "DejaVu Sans Mono-9" nil t)

(set-default-font "DejaVu Sans Mono-9")