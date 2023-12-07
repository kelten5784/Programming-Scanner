import socket


## MAIN FUNCATION
def main():
    target = input("Enter the target IP address or hostname: ")
    scan_mode = input("Enter scan mode (quick/thorough): ").lower()

    if scan_mode == 'quick':
        filter_option = input("Enter filter: (open/closed/all): ").lower()
        quick_scan(target, filter_option)

    elif scan_mode == 'thorough':
        start_port = int(input("Enter the initial port: "))
        end_port = int(input("Enter the last port: "))
        checker = True

        if start_port <= 0 or start_port > 65535:
            print("Invalid Start Port")
        elif end_port <= 0 or end_port > 65535:
            print("Invalid End Port")
        elif checker:
            print(f"Scanning ports {start_port} to {end_port} on {target}...\n")
            filter_option = input("Enter filter: (open/closed/all): ").lower()
            thorough_scan(target, start_port, end_port, filter_option)

    else:
        print("Invalid input for our scan mode option. Please enter 'quick' or 'thorough'.")

        # Use a loop to allow the user to enter a valid option
        while True:
            restart = input("Do you want to try again? (yes/no): ").lower()
            if restart == 'yes':
                main()
            elif restart == 'no':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please enter 'yes' or 'no'.")

###################################################################################################################################
##1. Port Filtering
def specific_ports(target, port, is_open):
    try:
        ##Creates a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        ##Attempt to connect to the target and port
        result = sock.connect((target, port))

        ##Runs if the socket is open(bool) | EXECPTION if connection is refused 
        if is_open:
            print(f"Port {port} is open")

    except ConnectionRefusedError:
        if not is_open:
            print(f"Port {port} is closed | Error: ConnectionRefusedError")

    except socket.timeout:
        if not is_open:
            print(f"Port {port} timed out | Error: socket.timeout")

    except Exception as e:
        print(f"An Unknown error occurred while scanning port {port}: {e}")

    finally:
        sock.close()
###################################################################################################################################
##2. Scan Modes
def quick_scan(target, filter_option):
    common_ports = [80, 443, 21, 22]

    for port in common_ports:
        if filter_option == 'open':
            specific_ports(target, port, True)
        elif filter_option == 'closed':
            specific_ports(target, port, False)
        elif filter_option == 'all':
            single_scan(target, port)
        else:
            print("Invalid filter option. Please enter 'open', 'closed', or 'all'.")

def thorough_scan(target, start_port, end_port, filter_option):
    for port in range(start_port, end_port + 1):
        if filter_option == 'open':
            specific_ports(target, port, True)
        elif filter_option == 'closed':
            specific_ports(target, port, False)
        elif filter_option == 'all':
            single_scan(target, port)
        else:
            print("Invalid filter option. Please enter 'open', 'closed', or 'all'.")

##Scans single port
def single_scan(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        # Attempt to connect to the target and port
        result = sock.connect((target, port))
        print(f"Port {port} is open")

    except ConnectionRefusedError:
        print(f"Port {port} is closed | Error: ConnectionRefusedError")

    except socket.timeout:
        print(f"Port {port} timed out | Error: socket.timeout")

    except Exception as e:
        print(f"An error occurred while scanning port {port}: {e}")

    finally:
        sock.close()


###################################################################################################################################
##3. Custom Port Lists 






###################################################################################################################################
##4. User-Friendly CLI



###################################################################################################################################
##5. Support for Scanning Multiple Targets 







###################################################################################################################################
##6. Logging and Reporting








###################################################################################################################################
##7. Output Customizaon





###################################################################################################################################
##8. Port Range Validaon





###################################################################################################################################
##9. Service Detecon




###################################################################################################################################
##10. IP Range Scanning










###################################################################################################################################
##11. Security Scanning









###################################################################################################################################
if __name__ == "__main__":
    main()
    
