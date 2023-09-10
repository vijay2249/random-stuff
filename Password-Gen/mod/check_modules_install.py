# import subprocess

# def check_modules_installed(file):
#     try:
#         with open(file, 'r') as requirements:
#             required_modules = [line.strip() for line in requirements.readlines()]
#             def is_module_installed(module):
#                 try:
#                     __import__(module)
#                     return True
#                 except ModuleNotFoundError or ImportError:
#                     return False
#             not_installed_modules = [str(module) for module in required_modules if not is_module_installed(module)]
#             if not_installed_modules:
#                 print(f'[-] These modules {not_installed_modules} are being installed as per requirements')
#                 subprocess.call(["pip", "install"] + not_installed_modules)
#     except FileNotFoundError:
#         pass


from subprocess import call

def install_modules(file):
    try:
        with open(file, 'r') as requirements:
            required_modules = [line.strip() for line in requirements]
            modules = [module.split("==")[0] for module in required_modules]
            def is_module_installed(module):
                try:
                    __import__(module)
                    return True
                except ModuleNotFoundError or ImportError:
                    return False
            # for module, req_module in zip(modules, required_modules):
            not_installed_modules = [module for module in required_modules if not is_module_installed(module)]
            install = [req_module for module, req_module in zip(modules, required_modules) if not is_module_installed(module)]
            if install:
                print(f'[-] These modules {install} are being installed as per requirements')
                call(["pip", "install"] + install, shell=True)
    except FileNotFoundError:
        pass


# file reading different for different os - work on that