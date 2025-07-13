# AI notes

## Install ollama

Better thing is to use a Linux downloader line uGet, provided in the debian environment.

Download `https://ollama.com/download/ollama-linux-amd64.tgz` and run the command (as root):

```
tar -C /usr -xzf ollama-linux-amd64.tgz
```

Installing manually is great not to have startup processes running against your will.

## Run ollama and check

```
> ollama serve
```

ollama is running by default on http://localhost:11434 . If you click you can see if ollama is running.

Or check from another terminal if ollama is running:

```
> ollama -v
```

## Get a model

```
ollama run gemma3:1b
```

Gets the model and runs it.

Look at the ollama [archive](https://ollama.com/library) for other models.

## Interact

I use https://github.com/ollama-ui/ollama-ui 

Usage:

```
> git clone https://github.com/ollama-ui/ollama-ui
> cd ollama-ui
> make
```

Then open http://localhost:8000 to have the chat window.
```



