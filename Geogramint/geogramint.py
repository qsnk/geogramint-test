# v1.4
import os
import sys
import codecs
import trio
import shutil
import json
import pandas as pd
from CLI import geogramint_cli

if __name__ == "__main__":
    shutil.rmtree("cache_telegram", ignore_errors=True)
    shutil.rmtree("cache", ignore_errors=True)

    geogramint_cli.CLI()
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log")
    print()
