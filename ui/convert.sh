#!/usr/bin/bash

uic="pyside6-uic"
src_path="../src/ui"

# Get the absolute path of the script file with symbolic links resolved
SCRIPT_PATH="$(realpath -s "${BASH_SOURCE[0]}")"

# Define the output directory
OUT_DIR="$(dirname "$SCRIPT_PATH")/$src_path"

# Find all .ui files in the directory and its subdirectories,
# and print their paths relative to the script's path
find "$(dirname "$SCRIPT_PATH")" -name "*.ui" -type f -print0 | while read -d $'\0' FILE; do
    # Get the absolute path of the file with symbolic links resolved
    ABS_PATH="$(realpath -s "$FILE")"

    # Get the relative path of the file with respect to the directory of the script file
    REL_PATH="$(realpath --relative-to="$(dirname "$SCRIPT_PATH")" "$ABS_PATH")"

    # Define the output file path and create the necessary directories
    OUT_FILE="$OUT_DIR/$REL_PATH"
    echo "$OUT_FILE"
    OUT_DIR_PATH="$(dirname "$OUT_FILE")"
    mkdir -p "$OUT_DIR_PATH"

    # # Copy the file to the output directory
    # cp "$ABS_PATH" "$OUT_FILE"

    $uic "$ABS_PATH" | install -D /dev/stdin "$(echo "$OUT_FILE" | sed s/\.ui$/\.py/)"

done
