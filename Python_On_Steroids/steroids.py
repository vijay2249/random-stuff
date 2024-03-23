from print_data import print_heading
from optparse import OptionParser

def get_function_to_execute():
    parser = OptionParser()
    parser.add_option("-f", dest="function", help="Function to execute")
    parser.add_option("--args", dest="args", help="Arguments needed for functions to execute", default={})
    return parser.parse_args()

def current_directory():
    print_heading("Print current directory content")

    import os

    pwd = os.getcwd() #get current working directory path

    list_directory = os.listdir(pwd) # list all directory contents (return list)
    for directory in list_directory:
        print(f"[+] {directory}")


#os.system() #execute shell commands
'''
    os.walk(path) 
navigates all the directories in the provided path directory, and
returns three values: _the path directory_, _the names of sub-directories_, _list of filenames in
the current directory path
'''

def os_walk():
    print_heading("Checkout os.walk() function")

    import os
    file_count = 0
    for root, directories, files in os.walk(".", topdown=False):
        file_count += len(files)
        for file in files:
            print(f"[+] {os.path.join(root, file)}")
            for sub_folder in directories:
                print(f"[+][+] {sub_folder}")
    print(f"[=] Total files in the current directory: {file_count}")


def counter_collections():
    print_heading("Checkout Counter method")

    import os
    from collections import Counter
    counts = Counter()
    for current_dir, sub_folders, files in os.walk("."):
        for file in files:
            first_part, extension = os.path.splitext(file)
            counts[extension] += 1

    for extension, count in counts.items():
        print(f"{extension}: {count}")

def sys_info():
    print_heading("Some system information")

    import os
    print(f"current directory: {os.getcwd()}")
    print(f"Uid: {os.getuid()}")
    print(f"PATH env: {os.getenv('PATH')}")
    print(f"os.environ: {os.environ}")
    print("----")
    print("Echo environ details")
    for environ in os.environ:
        print(environ)
    print("---")
    print("Environ items one by one")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

def working_with_file_system():
    print_heading("Working with file system")

    import os

    #os.path.isfile(path) # return True if path is file, else False
    #os.path.exists(path) # check if file/directory exists or not

    if not os.path.exists("test_directory"):
        try:
            os.makedirs("test_directory")
        except OSError as error:
            print(error)

def file_status():
    print_heading("Working with files")

    import os
    import time
    file = "module_2.py"
    st = os.stat(file)
    print(f"File stats: {file}")
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print(f"\t [=] created: {time.ctime(ctime)}")
    print(f"\t [=] last accessed: {time.ctime(atime)}")
    print(f"\t [=] last modified: {time.ctime(mtime)}")
    print(f"\t [=] size: {size} bytes")
    print(f"\t [=] owner: {uid}, {gid}")
    print(f"\t [=] mode: {oct(mode)}")

def file_with_extensions(**kwargs):
    print_heading("Checking files with py extensions")
    
    import os
    print(kwargs)
    extensions = kwargs['extensions']
    for ext in extensions:
        print(f"files with extension: {ext}")
        for path, folder, files in os.walk("."):
            for file in files:
                if file.endswith(ext):
                    print(os.path.join(path, file))

def reading_zip_file(**kwargs):
    print_heading("Reading data from zip files")

    import zipfile
    zipfileName = kwargs['zipfileName']
    with zipfile.ZipFile(zipfileName) as file:
        for zipInfo in file.infolist():
            print(zipInfo.filename)
            #yield zipInfo.filename
            print(zipInfo.filename)

def subprocess_module(**kwargs):
    print_heading("subprocess module")

    '''
    the subprocess module enables us to invoke and communiate with python processes, send data to the input and receive the output information
    This module allows us to run and manage processes directly from Python. That involves working with stdin standard input, standard output and return codes.

    We can use the argument `stdout=subprocess.PIPE` to get the standard output on stdout when the process is finished and same can be done with `stderr=subprocess.PIPE`

    if the `check` argument is equal to 'True' and the exit code is not zero an exception of type `CalledProcessError` is thrown.
    '''

    import subprocess
    print("run the command ls -la")
    process = subprocess.run(('ls', '-la'), stdout=subprocess.PIPE)
    print(process.stdout.decode('utf-8'))

    print("Check=True argument")
    try:
        process = subprocess.run(('find', './filder', '.'), stdout=subprocess.PIPE, check=True)
        print(process.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as error:
        print("Error: ", error)

    '''
    if we run thr process using `subprocess.run()`, our parent process hangs for as long as it takes for the child process to return the response.
    Once the thread is launched, our main process blocks and only continues when the thread terminates.
    The `run()` method includes "timeout" argument to allow you to stop an external program if it takes too long to execute.
    '''

    import sys
    #result = subprocess.run([sys.executable, '-c', 'import time;time.sleep(10)'], timeout=5)

    '''
    to read input while executing another program
    '''
    #result = subprocess.run([sys.executable,'-c', 'import sys;print(sys.stdin.read())'])
    import os
    print(f"Current path: {os.getcwd()}")
    print(f"path env: {os.getenv('PATH')}")
    print("run ls -la with call method")
    subprocess.call(['ls','-la'])


def subprocess_popen(**kwargs):
    print_heading("subprocess - popen method")
    import subprocess
    import sys
    import os
    cmd = get_respective_ping_command()
    param = "-c 1"
    domain = 'www.google.com'

    p = subprocess.Popen([cmd, param, domain], shell=False,stderr=subprocess.PIPE)
    out = p.stderr.read(1)
    sys.stdout.write(str(out.decode('utf-8')))
    sys.stdout.flush()


'''
the `Popen` function has the advantages of giving more flexbility if we compare it with the `call` function,
it executes the command as a child program in a new process.
'''

def get_respective_ping_command():
    import sys
    import os
    
    print(f"OS: {sys.platform}")
    if sys.platform.startswith("linux"):
        cmd = "/bin/ping"
    elif sys.platform == "darwin":
        cmd = "/sbin/ping"
    elif os.name == "nt":
        cmd = "ping"
    return cmd

def subprocess_ping_network():
    print_heading("Subprocess Ping Network execution")

    from subprocess import Popen, PIPE
    import sys

    ping_cmd = get_respective_ping_command()

    for ip in range(159,164):
        ipAddr = f"192.168.65.{ip}"
        print(f"Scanning: {ipAddr}")
        subprocess = Popen([ping_cmd, '-c 1', ipAddr], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = subprocess.communicate(input=None)
        print(stdout)

        if b'bytes from ' in stdout:
            print(f"The Ip: {ipAddr} has responded with a ECHO_REPLY")


def run_nmap(**kwargs):
    print_heading("Nmap on localhost")
    
    ipRange = kwargs['ipRange']
    from subprocess import Popen, PIPE

    process = Popen(f'nmap -v {ipRange}'.split(" "), stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())


def program_checker():
    print_heading("Check if program exists")

    import subprocess
    program = input("enter process: ")
    process = subprocess.run(f"which {program}".split(" "), capture_output=True, text=True)
    if process.returncode == 0:
        print(f"the process {program} is installed")
        print(f"The location of the binary is: {process.stdout}")

    else:
        printf("sorry the {program} is not installed")
        print(process.stderr)

'''
The difference between using `subprocess.run()` and `subprocess.Popen()` is that the core of the subprocess module is the `subprocess.Popen()` function
The run() method was added later and is a wrapper over subprocess.
Popen was created to integrate and unify its operation. It basically allows you to run a command on a thread and wait until it finishes.

run() method blocks the main process until the command executed in the child process finishes, while the subprocess, Popen you can continue to execute parent process tasks in the parallel, calling `subprocess.communicate` to pass or receive data from the threads whenever desired
'''

def setup_venv(**kwargs):
    print_heading("Setting up python virtual env")

    import subprocess
    from pathlib import Path

    venv_name = kwargs['venv_name'] if kwargs.get('venv_name', False) else input("Virtual env name: ")
    REQUIREMENTS = 'requirements.txt'

    process = subprocess.run(['which', 'python3'], capture_output=True, text=True)
    if process.returncode != 0:
        raise OSError("Python 3 was not installed")

    python_process = process.stdout.strip()
    print(f"Python path: {python_process}")

    process = subprocess.run('echo $SHELL', shell=True, capture_output=True, text=True)
    shell_bin = process.stdout.split("/")[-1]
    create_venv = subprocess.run(f"{python_process} -m venv {venv_name}".split(" "), check=True)
    if create_venv.returncode == 0:
        print(f"venv {venv_name} has been created")
    else:
        print(f"venv {venv_name} has not been created")

    pip_process = f"{venv_name}/bin/pip3"
    if Path(REQUIREMENTS).exists():
        print(f"Requirements file found")
        print("Installing requirements")
        subprocess.run([pip_process, 'install', '-r', REQUIREMENTS])
    print("Virtual ENV creation process completed")


if __name__ == '__main__':
    (options, args) = get_function_to_execute()
    func = options.function
    print(f"[=] Executing {func} function")
    #options.args = eval(options.args)
    #print(options.args)
    #print(type(options.args))
    try:
        print("trying to execute function with passing arguments")
        globals()[func](**eval(options.args))
    except TypeError as error:
        print("executing function without passing arguments")
        globals()[func]()