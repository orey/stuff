                                        ; UTILITIES

(defun mkstr (&rest args)
  (with-output-to-string (s)
                         (dolist (a args) (princ a s))))

(defun symb (&rest args)
  (values (intern (apply #'mkstr args))))

(defun consify (arg)
  (cons arg nil))

(defun increment ()
  (let ((i 0))
    ((lambda () (incf i)))))

(let ((counter 0))
  (defun my-inc ()
    (incf counter))
  (defun my-reset ()
    (setf counter 0)))

    



