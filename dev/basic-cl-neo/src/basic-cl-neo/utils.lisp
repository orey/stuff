;(in-package #:basic-cl-neo)

(ql:quickload :drakma)
(ql:quickload :cl-json)

(defvar *DB-CRED* '("neo4j" "lovecraf"))
(defvar *URL-ROOT* "http://localhost:7474/db/data/")

;------------------------- Test for loading

(defun test ()
  (format t "Loaded"))

(test)

;------------------------- Request function

(defun request (verb uri)
  (let* ((response (drakma:http-request (concatenate 'string *URL-ROOT* uri)
                                       :method verb
                                       :basic-authorization *DB-CRED*))
        (jsonstr (flexi-streams:octets-to-string response)))
    ;(format nil response)
    (format t jsonstr)
    ;(with-input-from-string
    (let ((l (json:decode-json-from-string jsonstr)))
      l)))

(request :GET "")
          
