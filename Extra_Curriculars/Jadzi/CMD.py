from subprocess import PIPE, run, call, Popen
import subprocess
import sys
import os
import threading

# creates an instance of an interpreter, is using CMD but could aso use python or other interpreters
def create_cmd_instance():
    cmd_instance = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, )
    return cmd_instance

def terminate_cmd_instance(instance):
    instance.terminate()

def quick_send(instance, command, timeout=30):
    instance.stdin.write(command+ "\n")
    instance.stdin.flush()

    output_lines = []
    def read_lines():
        while True:
            line = instance.stdout.readline()
            if not line:
                break
            output_lines.append(line)

    #create a thread to read lines while processing other things
    read_thread = threading.Thread(target=read_lines)   
    read_thread.start()

    #wait for thread to finish or timeout
    read_thread.join(timeout)



    reply = ''.join(output_lines)
    return reply



def find_admin_accounts(instance):
    command = "net user"
    netu_reply = quick_send(instance, command)
    netu_reply = netu_reply.split()
    admins = (netu_reply[netu_reply.index("Administrator"):netu_reply.index("Guest")])[1::]
    print(f"\n\nAdmins:{admins}\n\n")
    return admins

def admin_password(instance, admins):
    admin_password ={}
    for admin in admins:
        command = f"runas /user:{admin} cmd"
        runas_info = quick_send(instance, command)
        print(runas_info)
        #print(f"runas output/{admin}: {runas_info}")
        password = "password"
       # print(f"password guess ouput/{admin}: {password_guess.stdout}")
    return admin_password



def hello():
    cmd_instance = create_cmd_instance()
    print(f"\n\nCMD instance created: \n{cmd_instance}")
    admin_password(cmd_instance, find_admin_accounts(cmd_instance))
