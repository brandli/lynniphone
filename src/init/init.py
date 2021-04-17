#! /usr/bin/env python
from subprocess import call
call(['espeak "Hello Lynn" 2>/dev/null'], shell=True)