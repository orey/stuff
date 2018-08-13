# Environment

  * Install rlwrap for better command line editing
  * Install SBCL
  * Install Quicklisp

For a good editor, install Atom.

# Project creation

  * (ql:quickload "quickproject")
  * (quickproject:make-project "src/lisp/basic-cl-neo/" :depends-on '(json json-rpc drakma))

# Project load

 * (ql:quickload "basic-cl-neo")

# Interesting commands

## Change directory

```
CL-USER> (sb-posix:chdir "/home/apugachev")
0
CL-USER> (sb-posix:getcwd)
"/home/apugachev"
CL-USER> (sb-posix:chdir "/tmp/")
0
CL-USER> (sb-posix:getcwd)
"/tmp"
```

## Make a snapshot of the Docker container

```
sudo docker commit --message="Container with data"  CONTAINER-ID IMAGE_snapshot:TAG
```

TAG can be YYMMDD.
