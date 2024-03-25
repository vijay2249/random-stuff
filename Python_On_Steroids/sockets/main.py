from sockets import *
from optparse import OptionParser
from port_scanning import *

def get_function_to_execute():
    parser = OptionParser()
    parser.add_option("-f", dest="function", help="Function to execute")
    parser.add_option("--args", dest="args", help="Arguments needed for functions to execute", default={})
    return parser.parse_args()

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