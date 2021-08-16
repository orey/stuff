#!/bin/bash

DIR="${HOME}/Images"
DATE="$(date +%Y%m%d-%H%M%S)"
NAME="${DIR}/screenshot-${DATE}.png"
TEST="${DIR}/test-${DATE}.png"
LOG="${DIR}/screenshots.log"

# Check if the dir to store the screenshots exists, else create it:
if [ ! -d "${DIR}" ]; then mkdir -p "${DIR}"; fi

# Screenshot a selected window
if [ "$1" = "area" ];
then
    import -format png "${NAME}";
    echo "${NAME}" >> "${LOG}"
fi

# Screenshot the entire screen
if [ "$1" = "scr" ];
then
    import -format png -window root "${NAME}";
    echo "${NAME}" >> "${LOG}"
fi

# Screenshot a selected area
if [ "$1" = "special" ];
then
    import -format png -window root -crop 990x880+630+138 "${NAME}";
    echo "${NAME}" >> "${LOG}"
fi

# Tuning the special mode
if [ "$1" = "test" ];
then
    import -format png -window root -crop "$4"x"$5"+"$2"+"$3" "${TEST}";
    feh "${TEST}"
    echo "Test: $2 $3 $4 $5 - ${TEST}" >> "${LOG}"
fi

if [[ $# = 0 ]]; then
    # Display a warning if no area defined
    echo "Usage: $ ./capture-selected-area.sh [option] [otherparametersif any]"
    echo "option=area : capture an area interactively"
    echo "option=scr : capture the full screen"
    echo "option=special x y l h : capture an area in batch and crop it to a certain zone."
    echo "This option has supplementary parameters: x y l h respectively the coordinates x y for the translation of origin (top left of the screen) and the length and height to capture"
    echo "option=test x y l h : same as special except that a viewing of the image is launched with feh, which is useful to setup".
fi

