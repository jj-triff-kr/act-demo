import sys

import pydevd_pycharm
pydevd_pycharm.settrace('host.docker.internal', port=8838, stdoutToServer=True, stderrToServer=True)

def main():
    # Default user if no argument is provided
    user = "World"
    
    # If a command line argument is provided, use it as the username
    if len(sys.argv) > 1:
        user = sys.argv[1]
    
    # Print the greeting
    print(f"Hello Dear {user}")

if __name__ == "__main__":
    main()