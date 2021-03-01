import os
import sys

import argparse

from common import *
from const import *


parser = argparse.ArgumentParser()
parser.add_argument("--relay", help="Relay message from Bob to Alice.", action="store_true")
parser.add_argument("--break-heart", help="Alice is going to break Bob's heart.", action="store_true")
parser.add_argument("--custom", help="Send custom message.", action="store_true")
args = parser.parse_args()

if len(sys.argv) != 2:
    print("You must pick exactly one of the following flags: --relay, --break-heart, --custom")
    sys.exit(1)