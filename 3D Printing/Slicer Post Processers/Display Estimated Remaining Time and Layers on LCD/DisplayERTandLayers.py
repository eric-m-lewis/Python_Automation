""" Display ERT and Layers
This program is a post-processor for PrusaSlicer
that estimates the remaining time in the print and
modifies the G Code to display the layer number and
estimated remaining time on the LCD of the machine.

Created by Eric Lewis
Last Modified: 01/30/2024 """

### Import Modules ###

import re, sys, ntpath
from shutil import *
from os import path, remove, getenv
import argparse
import configparser
from datetime import datetime

# datetime object containing current date and time
NOW = datetime.now()

# global regex
RGX_FIND_NUMBER = r"-?\d*\.?\d+"

# config file full path; where _THIS_ file is
CONFIG_FILE = ntpath.join(f'{path.dirname(path.abspath(__file__))}', 'DTL_config.cfg')

### Define Functions ###
def fileInputArgParser():
    """
    Argument Parser
    :return: file path as string
    """
    parser = argparse.ArgumentParser(
        prog=path.basename(__file__),
        description="** PrusaSlicer Post Processing Script ** \n"
        "Display Estimated Remaining Time and Current Layer on LCD",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('input_file',metavar='gcode-files',type=str,nargs='+',
                        help='One or more GCode file(s) to be processed - at least one is required')

    try:
        args = parser.parse_args()
        return args.input_file[0]
    except IOError as msg:
        parser.error(str(msg))

def openGCodeInReadOnly(fileName):
    with open(fileName, 'r') as f_gcode:
        data = f_gcode.read()
        return data


def getTotalTimeEstimateFromGCode(data):
    totalTimeEstimateRegex = re.search(r'estimated printing time \(normal mode\) = (.*)', data)
    return totalTimeEstimateRegex[1]


def getTotalLayerCountFromGCode(data):
    totalLayerCountRegex = re.search(r'LAYER COUNT: (.*)', data)
    layerCountRegex = re.split(r"\s", totalLayerCountRegex[1])
    return layerCountRegex[2]


def main():
    """
    Main Function
    """
    filePath = fileInputArgParser()
    print(filePath)


if __name__ == "__main__":
    main()