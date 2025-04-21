# Termtitle

## To integrate into your .bashrc at the end

```
# Macro pour nommer les terminaux
function termtitle() {
  if [[ -z "$ORIG" ]]; then
    ORIG=$PS1
  fi
  TITLE="\[\e]2;$*\a\]"
  PS1=${ORIG}${TITLE}
}
```

## Usage

```
> termtitle test
> termtitle "git stuff"
```

