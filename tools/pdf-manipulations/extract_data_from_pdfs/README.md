# README

This is a stable version of `get_data_from_pdf_dain.py`.

## Principle

Use the executable + the `config.json` file. This files contains 2 grammars to deal with 2 kinds of DAIN files.

If you run the executable without parameters, here is what it says:

```
C:\Programs>get_data_from_pdf_dain.exe

|--------------------------------------------------------------------------------------|
| Tool to extract data from DAINs. This tool takes 1 parameter, the folder to analyze. |
| It manages 2 kinds of DAINs (1 page DAIN and 3 pages DAIN). If you have other types  |
| if DAINs to manage, please contact the NHI IT department.                            |
| Usage:                                                                               |
| C:\a_folder\another_folder> get_data_from_pdf_dain.exe "R:\folder1\folder2"          |
|--------------------------------------------------------------------------------------|

C:\Programs>
```

## Grammars

The grammars are located in the `config.json` file.

Hereafter is the start of the config file:

```
{
    "encoding" : "latin_1",
    "debugmode" : "False",
    "configs" : [
        {
            "name" : "=== Configuration: DAIN LH NOS ===",
            "start" : "10.Part N°/MFC",
            "dain_number" : [
                "MIDDLE",
                "4.CoC/DAIN N°",
                "5.Customer Order N°",
                "FIRST_X",
                "10"
            ],
            "date": [
                "MIDDLE",
                "Printed Date",
                "28.",
                "DATA"
            ],
```

The 2 first parameters are general to the program:

* `encoding` is used to open the DAIN files,
* `debugmode` if `True` makes the program verbose + generates a text file per analyzed PDF. This can be useful to tune the grammar.

The third important tag is `configs`. This tag is an array of configurations. Each kind of DAIN is supposed to have its own configuration because data are not formatted the same way in the PDFs.

A configuration starts with some data :

* `name` used to identify the configuration,
* `start` contains the string that starts all files of this configuration. Indeed, as Dain PDFs are produced by programs, they are starting always by the same characters. This is the identifier of configuration.

The last point is important. When the program runs, it opens every file, reads the first string and tries to match it with a configuration inside `config.json`. If it is not found, the file name will be put in a log file as "not treated".

### Structure of a configuration

In order to get data inside the data of the PDF, the program uses several strategies that are parameterized in the configuration file.

If you look at the sample above, you can see that the `dain_number` field is considered as being in the `MIDDLE` of the text, which means that we can find it between two tags : a start tag, `4.CoC/DAIN N°` and a end tag `5.Customer Order N°`.

Once we have the text, we may have to process it a bit more. Here, we will take the `FIRST_X` characters, the value of X being `10`.

`MIDDLE` is very frequent and the most easy way to get some data inside the PDF. But unfortunately, that does not cover every case. If you look a bit further in the second configuration of `config.json`, you can see `AFTER` and `BEFORE`

```
            ],
            "date": [
                "AFTER",
                "validated by electronic signature",
                "13"
            ],
            "contract": [
```

`AFTER` means that you only have a starting tag, and after the starting tag, you have the data you want to get, but after the data, you have various things depending on the DAIN. As the following elements are not constant, we can only grab a number of characters, here `13`.

```
            ],
            "case_number" :[
                "BEFORE",
                "1  /",
                "SPLIT_FIRST",
                " "
            ],
            "dimensions": [
```


The same thing occur with `BEFORE`. You want to grap a text that is before a constant zone, but before that text is preceded by variable texts. Note that this verb takes the previous line in totality, and not just a number of characters like we do for `AFTER`. We could implement something more precise but the samples of DAINs that were provided were not necessiting another kind of treatment.

### Once the string of data is obtained

Once the string is obtained, several treatments of the chain can be done. Some treatments do not not paramaters (like `DATA`). Some others need them (the other functions).

The exhaustive list is below:

* `DATA` means that no treatment will be done,
* `SPLIT_FIRST` means that the obtained text has a separator and you want to get the characters before the separator. We have in the grammar two cases of separator, the slash `/` and the space ` `, but it could be another character.
* `SPLIT_SECOND` means you want the second part of the text, after the separator.
* `SPLIT_LAST` means that you have a complex string and you want the last string. If the separator is ` `, that means you will get the last word, of the last amount.
* `FIRST_X` means you want only the first `X` characters, we saw already this treatment a bit above.
* `REMOVE_FIRST_LAST` is a bit more complex. You set a separator and you want what is the middle, so you want the full string but not the first token and not the last token. For sure the string in the middle may also have the separator.

## Extensibility

This program is quite compact and very generic. It can used not only for DAIN parsing but for whatever PDFs that are not image PDFs.

