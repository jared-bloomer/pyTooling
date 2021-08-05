#!/usr/bin/env python3

import os
from logger import logs

l=logs(os.path.basename(__file__))

l.write_log("info", "test message")
l.write_log("warn", "WARNING")
l.write_log("error", "This is an ERROR")
l.write_log("critical", "THIS IS CRITICAL")

