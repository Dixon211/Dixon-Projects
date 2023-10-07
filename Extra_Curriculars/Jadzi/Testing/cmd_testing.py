import subprocess

class CMD_instance:
    def __init__(self, name=""):
        self.name = name
        self.process = subprocess.Popen(
            ["cmd.exe"],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )



def interact_with_cmd(command):
    try:
        #create a process on the computer running the shell
        process = subprocess.Popen(
            command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        #read the initial output
        while True:
            line = process.stdout.readline()
            if not line:
                break
            print(line.strip())
    except Exception as e:
        print("Error:", str(e))

cmd = interact_with_cmd("""runas /user:Assoc "cmd" """)
