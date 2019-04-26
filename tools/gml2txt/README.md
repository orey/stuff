# README

## GML format

[GML](https://en.wikipedia.org/wiki/Graph_Modelling_Language) format is a way to represent graphs. It is used as an export format by products like [Yed](https://www.yworks.com/products/yed) for instance.

## Extracting labels from GML

In enterprise architecture daily works, it is common to have a draft of architecture in products like [Yed](https://www.yworks.com/products/yed) and to realize the real work afterwards using tools like [Archi](https://archimatetool.com).

For that purpose, extracting labels from GML files can be interesting.

## Programs

Two versions of the label extract program was very quickly developed:

  * The first version `gml2txt.py` uses the `networkx` Python package. It does not work because of many problems raised by the GML parser in this library (problems that are not supposed to be problems). This version was abandonned because of time to analyze in details the problems.
  * The second version `gml2txt2.py` is doing a very brutal extraction of labels in the GML file.
    * Warning: The extractor may not work with multi-line labels (i.e. labels with a `\n` in their content).

## Usage

```
Usage:
> python3 gml2txt2.py [finame.gml]
```

Generates a `filename.txt` will all the labels in it.


