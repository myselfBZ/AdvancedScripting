import subprocess
import os
path = input("Where do you want you project to live: ") 
projectName = input("How do you wanna call your project: ")
command = f"go mod init {projectName}"
dirs = ["handlers", "types", "store", "middleware", "routes"]

middlewareFiles = ["jwt.go", "authentication.go"]

mainFileContent = """
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main(){
    mux := http.NewServeMux()
    mux.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "Hello world")
    })
    log.Fatal(http.ListenAndServe(":8080", mux))
}


"""


def main(path:str):
    try:
        os.mkdir(path)
        os.chdir(path)
        run_command(command)
        create_file("main.go")
        with open("main.go", "w") as f:
            f.write(mainFileContent)
        os.mkdir(f"{path}/pkg")
        os.chdir(f"{path}/pkg")
        for dir in dirs:
            os.mkdir(dir)
            if dir == "middleware":
                os.chdir(dir) 
                for file in middlewareFiles:
                    create_file(file)
                    with open(file, "w") as f:
                        f.write("package middleware")
                os.chdir(f"{path}/pkg")
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
