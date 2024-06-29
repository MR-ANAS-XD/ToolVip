import os, sys
os.system("git pull")
try:
    __import__("MR_PLC").menu()
except Exception as e:
    exit(str(e))