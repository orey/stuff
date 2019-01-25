#!/bin/python3

import markdown

MINUTES = "minutes.md"

if __name__ ==  "__main__":
    input_file = codecs.open(MINUTES, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    output_file = codecs.open("some_file.html", "w",
                              encoding="utf-8",
                              errors="xmlcharrefreplace")
    output_file.write(html)

