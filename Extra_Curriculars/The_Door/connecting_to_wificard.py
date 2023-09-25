import requests
import subprocess
from subprocess import call
import sys
import os
from subprocess import PIPE, run
import json
import urllib3


settings = '{"state":"menu"}'


def call_cmd():
    while True:
        print("Command:")
        command = input()
        try:
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            print(result.returncode, result.stdout, result.stderr)
        except:
            print(f"not a valid command")
        print("Again? Y/N")
        reply = input()
        if reply.lower() not in ["yes", 'y']:
            break


#cmd access in program
def run_cmd():
    global options
    options["state"]="cmd"
    print(options)
    print("Hey there you're in the command prompt")
    call_cmd()
    options["state"]="menu"



options = json.loads(settings)
while True:
    if options["state"]=="menu":
        print(options)
        print(f"I'm Alive,\nHow can I help you?\n1.Access the Command Prompt")
        reply = input()
        if reply == "1":
            options["state"]=="cmd"
    elif options["state"]=="cmd":
            run_cmd()
    else:
        print(f"exiting the loop")
        break