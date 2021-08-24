;========================
; Config file for orgmode
;========================


;=== Custom faces for titles in org
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(org-level-1 ((t (:background "aquamarine"))))
 '(org-level-2 ((t (:background "yellow"))))
 '(org-level-3 ((t (:background "pale green"))))
 '(org-level-4 ((t (:background "bisque")))))


;== Get the standard selection of emacs with S-arrows
(setq org-support-shift-select t)


;=== Personal variables for orgmode project customization
(setf src-mypath "C:/Users/a876246/Documents/oreyboulot-NHI/_notes/")
(setf src-mypath-org (concat src-mypath "org/"))
(setf src-mypath-images (concat src-mypath "images/"))
(setf src-mypath-other (concat src-mypath "other/"))

(setf tgt-mypath "C:/Users/a876246/Documents/oreyboulot-NHI/_notes/")
(setf tgt-mypath-html (concat tgt-mypath "html/"))
(setf tgt-mypath-images (concat tgt-mypath "html/images/"))
(setf tgt-mypath-other (concat tgt-mypath "html/other/"))


;== Publishing template
(setq org-publish-project-alist
      `(("nhi"
         :base-directory ,src-mypath-org
         :base-extension "org"
         :publishing-directory ,tgt-mypath-html
         :publishing-function org-html-publish-to-html
         :exclude "PrivatePage.org" ;; regexp
         :headline-levels 3
         :section-numbers t
         :makeindex t
         :with-toc t
         :html-head "<link rel=\"stylesheet\ href=\"../other/styles.css\" type=\"text/css\"/>"
         :html-preamble t)

        ("images"
         :base-directory ,src-mypath-images
         :base-extension "jpg\\|gif\\|png"
         :publishing-directory ,tgt-mypath-images
         :publishing-function org-publish-attachment)

        ("other"
         :base-directory ,src-mypath-other
         :base-extension "css\\|el\\|pdf"
         :publishing-directory ,tgt-mypath-other
         :publishing-function org-publish-attachment)
        ("notes_nhi" :components ("nhi" "images" "other"))))


;=== Publish project shortcut
(global-set-key (kbd "<f6>") 
   '(lambda () 
      (interactive) 
      (org-publish-all t)))


;=== Remove automatic indentation for orgmode
(add-hook 'org-mode-hook
          (lambda ()
            (set (make-local-variable 'electric-indent-functions)
                 (list (lambda (arg) 'no-indent)))))

