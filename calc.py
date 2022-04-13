#!/usr/bin/env python3
import sys
import json
import pandas as pd

# Deserializing JSON to dict
with open("masterlist.json") as json_file:
    data = json.load(json_file)
    print(data)
