# Port scanning with sockets

def check_args_and_ask_for_input(key_to_check, input_message, kwargs):
    return kwargs[key_to_check] if kwargs.get(key_to_check, None) else input(f"{input_message}")

def port_scanning_via_sockets(**kwargs):
    heading("Port scanning v1.0 using sockets")

    '''
     sockets are the fundamental building block for network communication, and by calling the `connect_ex()` method, we can easilt test whether a particular port is opened or closed or filtered.
    '''

    import socket
    import sys
    from datetime import datetime
    import errno

    remoteServer = check_args_and_ask_for_input('remoteServer', "Enter remote host to scan: ", kwargs)
    remoteServerIp = socket.gethostbyname(remoteServer)

    startPort = check_args_and_ask_for_input('startPort', "Enter starting port: ", kwargs)
    endPort = check_args_and_ask_for_input('endPort', "Enter end port: ", kwargs)

    print(f"Scanning.... {remoteServerIp}")

    time_init = datetime.now()

    try:
        for port in range(int(startPort), int(endPort)):
            print(f"Checking port {port}...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((remoteServerIp, port))
            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")
                print(f"Reason : {errno.errorcode[result]}")
            sock.close()
    except KeyboardInterrupt:
        print("Exiting program..")
        sys.exit()
    except socket.gaierror as error:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    except socket.error:
        print("Couldn.t connect to server")
        sys.exit()

    time_finish = datetime.now()
    print(f"Port scanning completed in: {time_finish - time_init}")