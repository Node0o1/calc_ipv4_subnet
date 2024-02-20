# calc_ipv4_subnet
*** subnet calculator ***
##### *Type: Terminal Application*

#### Description
> Calculates subnets for a given ip and subnetmask and write the output to a destination txt file.

### A few things to note:
- Python 3 needs to be installed and added to Path

## **Instructions:**
#### **Download**
- Using CLI, navigate to the folder you wish to download the application and run:
  ```console
  git clone https://github.com/Node0o1/calc_ipv4_subnet.git
  ```

#### **setup**
- after downloading, use the CLI to navigate into the directory
  No dependancies.

#### **Run**
  - From within the calc_ipv4_subnet directory using CLI:
    python file.py param1 param2 param3
    params=(starting ip, subnetmsk, num of borrowed bits)
    example: 
      ``` python calc_ipv4_subnet.py 192.168.0.0 255.255.0.0 4 ```

  - YOU MAY OMIT THE PARAMETERS VIA CMD AND WILL BE PROMTED FOR EACH
    example:
      ``` python calc_ipv4_subnet.py ```
