import sys
import subprocess

def test_hola_mundo(output):
    assert output == 'Hola mundo!', "Should be Hola mundo!"

def test_len_hola_mundo(output):
    assert len(output) == 11, "Should be 11"

tests = [
    test_hola_mundo,
    test_len_hola_mundo
]

def validate_error(function):
    def wrapper(*args, **kwargs):
        code, output, err = function(*args, **kwargs)
        output, err = output.decode("utf-8"), err.decode("utf-8")

        if err:
            raise Exception(err)

        if code != 0:
            raise Exception('Hubo un error al intentar ejecutar el programa.')

        return code, output.split("\n")[:1][0]
    
    return wrapper

@validate_error
def run_script(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr
 
def execute_test(output):
    try:
        [test(output) for test in tests]
    except Exception as err:
        print(err)
        exit(1)

if __name__ == '__main__':
    script = sys.argv[1]
    code, output = run_script([sys.executable, script])

    execute_test(output)