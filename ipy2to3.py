#!/usr/bin/env python3
# Converts an IPython notebook written in python2 to python3.

import io
import json
import os
import subprocess
import tempfile


def convert_ipy2to3(json_to_convert):
    if 'worksheets' in json_to_convert:
        for worksheet in json_to_convert['worksheets']:
            convert_a_worksheet_ipy2to3(worksheet, "new")
    elif 'cells' in json_to_convert:
        convert_a_worksheet_ipy2to3(json_to_convert, "old")
    else:
        import sys
        print("cells or worksheets not found in the json of ".format(sys.argv[1]))
        sys.exit(1)


def is_python_code_cell(cell):
    return cell['cell_type'] == "code" and cell['language'] == "python"


def is_python_code_cell_old(cell):
    return cell['cell_type'] == "code"  # and cell['language'] == "python"


def convert_a_worksheet_ipy2to3(worksheet, version):
    if version is "old":
        code_cells = filter(is_python_code_cell_old, worksheet['cells'])
    else:
        code_cells = filter(is_python_code_cell, worksheet['cells'])

    for cell in code_cells:
        convert_a_cell_ipy2to3(cell, version)


def is_magic(line):
    line = line.strip()
    if len(line) == 0: return False
    return line[0] in ['%', '!', '?'] or line[-1] == '?'


# Empties magic lines and returns where they were and what they are
def replace_magic_lines(lines):
    magic_lines = []
    for i, line in enumerate(lines):
        if is_magic(line):
            magic_lines.append((i, lines[i]))
            lines[i] = "\n"
    return magic_lines


def convert_a_cell_ipy2to3(cell, version):
    magic = replace_magic_lines(cell['source' if version is "old" else 'input'])

    file_name = None

    # save cell to file, and have the filename:
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as ostream:
        ostream.writelines(cell['source' if version is "old" else 'input'])
        file_name = ostream.name

    # convert python2 to python3 by executing 2to3:
    # cmd2to3 = ["C:/Anaconda3_64/Scripts/2to3.exe", "--nobackups", "--write", file_name]  # windows example
    cmd2to3 = ["2to3", "--nobackups", "--write", file_name]
    with io.open(os.devnull, "w") as nulls:
        subprocess.check_call(cmd2to3, stdout=nulls, stderr=nulls)

    # read converted file back to cell
    with io.open(file_name, mode="r") as istream:
        cell['source' if version is "old" else 'input'] = istream.readlines()

    # remove the file
    os.remove(file_name)
    for i, line in magic:
        cell['source' if version is "old" else 'input'][i] = line


def main(argv):
    if len(argv) != 3:
        print("Usage: {} fromfile.ipynb tofile.ipynb".format(argv[0]))
        return 1
    ipy_json = None
    with io.open(argv[1], mode="r") as istream:
        ipy_json = json.load(istream)
    convert_ipy2to3(ipy_json)
    with io.open(argv[2], mode="w") as ostream:
        json.dump(ipy_json, ostream)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
