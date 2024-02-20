# calc_ipv4_subnet
**Subnet Calculator**
##### *Type: Terminal Application*

#### Description
> Calculates subnets for a given ip and subnetmask.
> Populates each created subnets with the subnet address, broadcast address, and list all assignable IP addresses.
> All output is written and saved in a user specified destination txt file.

### A few things to note:
- Python 3 needs to be installed and added to Path

## **Instructions:**
#### **Download**
- Using CLI, navigate to the folder you wish to download the application and run:
  ```console
  git clone https://github.com/Node0o1/calc_ipv4_subnet.git
  ```

#### **Setup**
- after downloading, use the CLI to navigate into the directory
  > No dependancies.

#### **Run**
  - From within the calc_ipv4_subnet directory using CLI:
    - python file.py param1 param2 param3
    - params=(starting ip, subnetmsk, num of borrowed bits)
    - example: 
      ```py
      python calc_ipv4_subnet.py 192.168.0.0 255.255.0.0 4
      ```

  - you may omit the parameters in CLI and be prompted for each param individually.
    > example:
      ```py
      python calc_ipv4_subnet.py
      ```
