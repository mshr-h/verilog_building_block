#!python
#-*- encoding:utf-8 -*-

import sys
import os
import math

out_template = """-- Copyright (C) 1991-2010 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions
-- and other software and tools, and its AMPP partner logic
-- functions, and any output files from any of the foregoing
-- (including device programming or simulation files), and any
-- associated documentation or information are expressly subject
-- to the terms and conditions of the Altera Program License
-- Subscription Agreement, Altera MegaCore Function License
-- Agreement, or other applicable license agreement, including,
-- without limitation, that your use is for the sole purpose of
-- programming logic devices manufactured by Altera and sold by
-- Altera or its authorized distributors.  Please refer to the
-- applicable agreement for further details.

-- Quartus II generated Memory Initialization File (.mif)

WIDTH=8;
DEPTH={0};

ADDRESS_RADIX=UNS;
DATA_RADIX=UNS;

CONTENT BEGIN
{1}
END;
"""

def read_file(filename):
    content = []
    for item in open(filename, "r"):
        line = item.rstrip()
        if line:
            content.append(int(line, 16))
    return content

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: python {0} input.txt output.mif".format(sys.argv[0])
        exit(1)

    in_file  = os.path.abspath(sys.argv[1])
    out_file = os.path.abspath(sys.argv[2])
    content = read_file(in_file)
    address = 2**int(math.ceil(math.log(len(content), 2)))
    data = ""
    for word, i in zip(content, range(len(content))):
        data += "\t{0} : {1};\n".format(i, word)
    output = out_template.format(address, data)
    f = open(out_file, 'w')
    f.write(output)
    f.close()
