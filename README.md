# Proxy Node Checker

This tool checks whether the specified proxy servers are operational. The check utilizes a timeout value that you specify. Operational proxies are saved in the `outputProxy.txt` file.

## Usage

1. **Setup Proxies List**  
   Add your proxy IP and port information to the `inputProxy.txt` file in the following format:

    127.0.0.1:8080
    192.168.1.1:3128


2. **Run the Script**  
Execute the script using the following command:

    python proxy_checker.py

3. **Specify Timeout**  

    0.1 _ Fast / Low Reliability
    1.0 _ Medium / Considered Reliable
    5.0 _ Slow / Highly Reliable but potentially less practical

    Enter the value between 0.1 and 5.

4. **Check the OUTPUT** 

    The script will verify the status of each proxy. Operational proxies are saved in the outputProxy.txt file.

