import subprocess
import os
path = "/media/whoami/DATA/NodeJS/Express/"
command = "npm init -y"
files = ["server.js", 'middleware.js', 'models.js', 'router.js', 'controllers.js']
name = input("How do you wanna name your project? ")
path += name

def main(path:str):
    express = "npm install express"
    try:
        os.mkdir(path)
        os.chdir(path)
        run_command(command)
        run_command(express)
        os.mkdir(f"{path}/src")
        os.chdir(f"{path}/src")
        for file in files:
            create_file(file)
        print("You are good to go!")
    except Exception as e:
        print(e)



def create_file(file_name:str):
    with open(file_name, 'w') as f:
        f.write("")
        


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Command executed successfully:")
            print(result.stdout)
        else:
            print("Error executing command:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", e)

if __name__=="__main__":
    main(path)