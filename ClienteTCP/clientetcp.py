import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Connection failed!!")
        print("Error: {}".format(e))
        sys.exit()
    print("Socket created!")

    TargetHost = input("Enter the host or ip address to connect to: ")
    TargetPort = input("Enter the port to connect to:")

    try:
        s.connect((TargetHost, int(TargetPort)))
        print(f"Tcp Client Connected to: {TargetHost} on port: {TargetPort}")
        s.shutdown(2)
    except socket.error as e:
        print("It wasn't possible to connect to {} on port: {}".format(TargetHost, TargetPort))
        print("Error: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()