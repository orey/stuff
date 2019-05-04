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

;;;
;; n3 mode
;;

;(add-to-list 'load-path "~/.emacs.d/n3-mode.el")
(add-to-list 'load-path "~/.emacs.d/vendor")
(autoload 'n3-mode "n3-mode" "Major mode for OWL or N3 files" t)

;; Turn on font lock when in n3 mode
(add-hook 'n3-mode-hook
          'turn-on-font-lock)

(setq auto-mode-alist
      (append
       (list
        '("\\.n3" . n3-mode)
        '("\\.owl" . n3-mode))
       auto-mode-alist))

;; Replace {path} with the full path to n3-mode.el on your system.

;; If you want to make it load just a little faster;
;; C-x f n3-mode.el
;; M-x byte-compile-file n3-mode.el
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (markdown-mode))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(setq backup-directory-alist `(("." . "/home/olivier/.emacs-saves")))

; Remove tabs and replace by spaces
(setq-default indent-tabs-mode nil)

(delete-selection-mode 1)