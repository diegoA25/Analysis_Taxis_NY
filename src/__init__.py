# init for the src directory

import os
import sys

# Add the 'src' directory to the path and MYPATH
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
os.environ["MYPYPATH"] = os.path.dirname(os.path.realpath(__file__))