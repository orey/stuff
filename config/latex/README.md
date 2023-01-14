# LATEX

## Latex on Windows with no installation rights

### Miktex

Use the portable version. To set the firewall, set the following variable:

```
set ALL_PROXY="http://user:pasword@firewall.com:8080"
```

### TexStudio

Could be useful to add the path to Miktex in the PATH (generally in install/miktex/bin).

## Recipes for documents

### Include header and footer in page geometry

```
\usepackage[a5paper,margin=1.5cm,includehead,includefoot,portrait]{geometry}
```

### No line in header and footer

```
\usepackage{fancyhdr}
\pagestyle{fancy}

% No line
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
```

### Double line in header

With `fancyhdr`.

The points between `[` enable to position the rule.

```
\usepackage{fancyhdr}
\pagestyle{fancy}

\renewcommand{\headrule}{
{\color{black!60}\rule[2pt]{\linewidth}{4pt}}
{\color{gray!60}\rule[20pt]{\linewidth}{1.5pt}}
}
```





