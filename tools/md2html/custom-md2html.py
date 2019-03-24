#================================
# Personal md to html converter
# Author: O. Rey
# Date: March 22 2019
# License: GPL V3
#================================
#!/bin/python3
import os, sys

def format_header(title):
    return "<html><title>" + title + "</title><body>\n"

def format_trailer():
    return "</body></html>"

def format_title1(str):
    # #-X
    # 012
    return "<h1>" + str[2:] + "</h1>\n"

def format_title2(str):
    # ##-X
    # 0123
    return "<h2>" + str[3:] + "</h2>\n"

def format_title3(str):
    # ###-X
    # 01234
    return "<h3>" + str[4:] + "</h3>\n"

def format_title4(str):
    # ####-X
    # 012345
    return "<h4>" + str[5:] + "</h4>\n"

def format_title5(str):
    # #####-X
    # 0123456
    return "<h5>" + str[6:] +" </h5>\n"

def format_list_begin():
    return "<ul>\n"

def format_list_end():
    return "</ul>\n"

def format_list_line_level1(str):
    # --* X
    # 01234
    return "<li>" + str[4:] + "</li>\n"

def format_list_line_level2(str):
    # ----* X
    # 0123456
    return "<li>" + str[6:] + "</li>\n"
    
def format_image(text, image):
    return '<p><img alt="' + text + '" src="' + image + '" width="800"/></p>\n'

def format_line(line):
    return "<p>" + line + "</p>"

#------------------

def parse_line(inlist, insublist, line):
    # Title1
    if (line[0:2] == "# "):
        return False, False, format_title1(line)
    # Title2
    if (line[0:3] == "## "):
        return False, False, format_title2(line)
    # Title3
    if (line[0:4] == "### "):
        return False, False, format_title3(line)
    # Title4
    if (line[0:5] == "#### "):
        return False, False, format_title4(line)
    # Title5
    if (line[0:6] == "##### "):
        return False, False, format_title5(line)

    # List line level 1
    if (line[0:4] == "  * "):
        if inlist and not insublist:
            # continue the list
            return True, False, format_list_line_level1(line)
        elif inlist and insublist:
            # close the sublist, continue the list
            return True, False, format_list_end() + format_list_line_level1(line)
        elif not inlist and insublist:
            # strange : we begin by closing the sublist
            return True, True, format_list_end() + format_list_line_level2(line)
        elif not inlist and not insublist:
            #beginning of list
            return True, False, format_list_begin() + format_list_line_level1(line)
            
    # List line level 2
    if (line[0:6] == "    * "):
        if inlist and insublist:
            # continue the sublist
            return True, True, format_list_line_level2(line)
        if inlist and not insublist:
            # beginnig of sublist
            return True, True, format_list_begin() + format_list_line_level2(line)
        if not inlist and insublist:
            # strange: continue the level 2 list
            return True, True, format_list_line_level2(line)
        if not inlist and not insublist:
            # start a double list
            return True, True, format_list_begin() + format_list_begin() + format_list_line_level2(line)

    if line[0:2] == "![":
        tab = line[2:].split(']')
        name = tab[0]
        image = tab[1].replace('(', "").replace(')','')
        return False, False, format_image(name, image)

    if inlist and insublist:
        # close both lists
        return False, False, format_list_end() + format_list_end() + format_line(line)
    if inlist and not insublist:
        # close list
        return False, False, format_list_end() + format_line(line)
    if not inlist and insublist:
        # strange : close both lists
        return False, False, format_list_end() + format_list_end() + format_line(line)
    if not inlist and not insublist:
        return False, False, format_line(line)

    print("We never should reach this point")


if __name__ ==  "__main__":
    if len(sys.argv) == 1:
        print("Usage: custom-md2html.py [file_to_convert_without_md_extention]")
        sys.exit(0);
    filename = sys.argv[1]
    print(filename)
    with open(filename + ".html", 'w') as fwrite:
        fwrite.write(format_header(filename))
        with open(filename + ".md", 'r') as fread:
            print(fread)
            inlist = False
            insublist = False
            str = ""
            for line in fread:
                print(line)
                inlist, insublist, str = parse_line(inlist, insublist, line)
                fwrite.write(str)
        fwrite.write(format_trailer())
        fwrite.close()


