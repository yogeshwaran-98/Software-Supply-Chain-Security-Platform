# security-validation/semgrep/command_injection.py

import os

cmd = input()

os.system(cmd)