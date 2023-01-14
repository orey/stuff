;;;; basic-cl-neo.asd

(asdf:defsystem #:basic-cl-neo
  :description "Describe basic-cl-neo here"
  :author "Olivier Rey <rey.olivier@gmail.com>"
  :license "Apache 2"
  :depends-on (#:cl-json
               #:drakma)
  :serial t
  :components ((:file "package")
               (:file "basic-cl-neo")
               (:file "utils")))
