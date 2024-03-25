from print_data import print_heading as heading


'''
The socket module exposes all the necessary pieces to quickly write TCP and UDP clients and servers for writing low-level network applicatons.

Socket programming refers to an abstract principe by which two programs can share any data stream by using an Application Program Interface (API) for different protocols available in the internet TCP/IP stack, typically supported by all operating systems.
'''


'''
Sockets are the main components that allow us to leverage the capabilities of an operating system to interact with a network.
Sockets are point-to-point channel of communication between a client and a server.
'''

'''
Network sockets are a simple way of establiching communication between processes on the same machine or on a different ones.
The socket concept is very similar to the use of file descriptors for UNIX os

A socket address for a network consists of an IP address and port number. A socket's aim is to communicate processes over the network
'''


heading("Network sockets in python")

''' 
We can use sockets to establish a communication channel between two processes within a process or between processes on different machines. 
There are different types of sockets like TCP sockets, UDP sockets, and UNIX domain sockets
'''

def basic_socket_syntax():
    heading("Basic Sockets syntax")

    import socket
    #syntax for sockets.
    print('''
        s = socket.socket(socket_family, socket_type, protocol=0)
        ''')
    
    '''
    Based on communication type, sockets are classified as follows:
     - TCP sockets (socket.SOCK_STREAM)
     - UDP sockets (socket.SOCK_DGRAM)

   Sockets can also be categorized by family 
    - UNIX sockets (socket.AF_UNIX), which aere created before the network definition and are based on data
    - The socket.AF_INET socket for working with the IPv4 protocol
    - The socket.AT_INET6 socket for working with the IPv6 protocol

    `raw sockets`, allows us to access the communication protocols, with the possibility of using layer 3(network layer) and layer 4(transport layer) protocols, therefore giving us access to the protocols directly and the information we receive in them.
    '''

def socket_module():
    heading("Introducing socket module")

    import socket
    print(dir(socket))

    # To open a socket on a certain machine, we use the socket class constructor that accepts the family, socket type, and protocol as parameters
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #socket.accept() -> accept connections and return a value pair as (conn, address)
    #socket.bind() -> connect to the address specified as a parameter
    #socket.connect() -> connect to the address specified as a parameter
    #socket.listen() -> listen for commands on the server/client
    #socket.recv(buflen) -> receive data from the socket. The method argument indicates the max amount of data it can receive
    #socket.recvfrom(buflen) -> receive data and the senders address
    #socket.recv_into(buffer) -> receive data into a buffer
    #socket.send(bytes) -> send bytes of data to the specified target
    #socket.sendto(data, address) -> sending data to a given address
    #socket.sendall(data) -> sending all the data in the buffer to the socket
    #socket.close() -> releasing the memory and finishes the connection


def socket_connection():
    heading("client, server comm using sockets")

    '''
    in client-server architecture, there is a central server that provides services to a set of machines that connect to it. 

    The main methods that we can use from the pov of the server:
     - socket.bind(address) -> allows us to connect the address with the socket, with the requirement that the socket must be open before establishing the connection with the address
     - socket.listen(count) -> this method accepts parameter the maximum number of connections from the clients and starts the TCP listener for incoming connections
     - socket.accept() -> enables us to accept the client connections and returns a tuple with two values that represent `client_socket` and `client_address`. [ you need to call the `socket.bind()` and `socket.listen()` methods before using this method


     The main methods from pov of client:
      - socket.connect(ip_Addr) -> connects the client to the server ip address
      - socket.connect_ext(ip) -> has the same functionality as the previous method and offers the possibility of returning an error in the event of not being able to connect with the mentioned ip address
    '''

    import socket
    ip = '127.0.0.1'
    portlist = [21,22,23,80]
    for port in portlist:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        print(f"{port}: {result}")
        sock.close()


def socket_web(**kwargs):
    heading("connect to webserver port 80")

    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('ftp.debian.org', 80))
    cmd = 'GET http://ftp.debian.org/debian/README.mirrors.txt HTTP/1.0\r\n\r\n'.encode()
    sock.send(cmd)
    while True:
        data = sock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    sock.close()


def get_info_via_socket(**kwargs):
    heading("Gathering information via sockets")

    '''
    we can convert hostname to IP address and vice versa via socket methods

     - socket.gethostbyname(hostname) -> returns a string converting a hostname to the IPv4 address format, (this is equivalent to `nslookup` command
     - socket.gethostbyname_ex(name) -> returns a tuple that contains an IP address for a specific domain name. If we see more than one IP address, this means one domain runs on multiple IP addresses
     - socket.getfqdn([domain]) -> used to find the fully qualified name of a domain
     - socket.gethostbyaddr(ip_addr) -> returns a tuple with three values (hostname, name, ip_addr_list).
     - socket.getservbyname(servicename[, protocol_name]) -> this method allows you to obtain the port number from the port name
     - socket.getservbyport(port[, protocol_name]) -> this method performs the reverse operation to the previous one, allowing you to obtain the port name from the port number
    '''

    import socket

    try:
        hostname = socket.gethostname()
        print(f"gethostname: {hostname}")

        ip_Addr = socket.gethostbyname(hostname)
        print(f"Local ip address: {ip_Addr}")
        print(f"gethostbyname - www.python.org: {socket.gethostbyname('www.python.org')}")
        print(f"github.com - gethostbyname_ex: {socket.gethostbyname_ex('github.com')}")
        print(f"gethostbyaddr - 8.8.8.8 - {socket.gethostbyaddr('8.8.8.8')}")
        print(f"getfqdn - www.google.com : {socket.getfqdn('www.google.com')}")
        print(f"getaddrinfo - www.google.com : {socket.getaddrinfo('www.google.com', None, 0, socket.SOCK_STREAM)}")
    except socket.error as error:
        print(str(error))
        print("Connection error")



def socket_service_names():
    heading("Get service name from the port number")

    import socket

    for port in [21,22,23,25,80]:
        print(f"Port :{port} => service name: {socket.getservbyport(port, 'tcp')}")

    print(f"Port: 53 => service name: {socket.getservbyport(53, 'udp')}")


def socket_exceptions():
    heading("managing socket exceptions")

    '''
       exception - socket.timeout -> catches exceptions related to the expiration of waiting times.
       exception - socket.gaierror -> catches errors during the search for information about IP addresses. (example, when we are using the `getaddrinfo()` and `getnameinfo()` method
       exception - socket.error -> catches generic input and output errors and communication. This is a generic block where you can catch any type of exception
    '''

    import socket
    host = "domain/ip_address"
    port = 80
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(sock)
        sock.settimeout(5)
    except socket.error as error:
        print(f"socket create error: {error}")

    try:
        sock.connect((host, port))
        print(sock)
    except socket.timeout as error:
        print(f"Timeout error: {error}")

    except socket.gaierror as error:
        print(f"connection error to the server: {error}")
    except socket.error as error:
        print(f"Connection error: {error}")


def basic_client_with_socket():
    heading("Basic client connection with socket module")

    '''
    We can send/receive data using the `send()` and `recv()` methods for TCP communications. For UDP communication, we could use the `sendto()` and `recvfrom()` methods instead. 
    '''

    import socket

    host = kwargs['host'] if kwargs.get('host', None) else input("Enter hostname: ")
    port = kwargs['port'] if kwargs.get('port', None) else input("Enter portnumber: ")

    '''
    create a TCP socket obj, connect the client to the remote host and send it some data. Receive some data back and print out the response
    '''
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(10)
            if sock.connect_ex((host, port)) == 0:
                print(f"Established connection to server {host}:{port}")
                request = f"GET / HTTP/1.1\r\nHost:{host}\r\n\r\n"
                sock.send(request.encode())
                data = sock.recv(4096)
                print(f"data: {repr(data)}")
                print(f"Length of data: {len(data)}")

    except socket.timeout as error:
        print(f"Timeout error: {error}")
    except socket.gaierror as error:
        print(f"Connection error to the server: {error}")
    except socket.error as error:
        print(f"Connection error: {error}")





