import sys
import subprocess

def run_script(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr


code, output, stderr = run_script([sys.executable, 'main.py user.py'])  

print(code)
print(output)  
print(stderr)  