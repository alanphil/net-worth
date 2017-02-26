#!/usr/bin/python
#
# Simple Python program for calculating
# net worth. It reads a YAML file of
# data and runs net worth calculations 
# based on the data.
#

import yaml
import sys

input_file = sys.argv[1]

with open(input_file, 'r') as f:
  finance = yaml.load(f)

total_assets = sum(finance["assets"].itervalues())
print 'Assets:', total_assets

total_lib = sum(finance["liabilities"].itervalues())
print 'Liabilities:', total_lib

networth = total_assets - total_lib

print 'Networth is', networth
