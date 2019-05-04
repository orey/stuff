; .Emacs file for Debian 9

(setq url-proxy-services
   '(("no_proxy" . "^\\(localhost\\|10.*\\)")
     ("http" . "127.0.0.1:3128")
     ("https" . "127.0.0.1:3128")))

(setq backup-directory-alist `(("." . "C:/Tools/DEV/.emacs-saves")))

;==== For markdown support
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
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (csv-mode markdown-mode))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;=== Enabling aspell under windows from a Cygwin install
(add-to-list 'exec-path "C:/Tools/DEV/Software/cygwin64/bin/")
(setq ispell-program-name "aspell")
; Does not work
; (setq ispell-personal-dictionary "~/.ispell")
; but with a cygwin installed, stores the personal dict in /home/USER/.aspell.en.pws
(require 'ispell)
(global-set-key (kbd "<f8>") 'ispell-word)
(global-set-key (kbd "C-<f8>") 'flyspell-mode)

(require 'package)
(add-to-list 'package-archives '("org" . "https://orgmode.org/elpa/") t)

; Remove tabs and replace by spaces
(setq-default indent-tabs-mode nil)

(delete-selection-mode 1)
