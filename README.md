# ipv4_subnet_calc
**Subnet Calculator**
##### *Type: Terminal Application*

#### Description
> Calculates subnets for a given ip and subnetmask.
> Populates each created subnets with the subnet address, broadcast address, and list all assignable IP addresses.
> All output is written and saved in a user specified destination txt file.
>
> Handles Class A, B, C networks.

### A few things to note:
- Python 3 needs to be installed and added to Path

## **Instructions:**
#### **Download**
- Using CLI, navigate to the folder you wish to download the application and run:
  ```console
  git clone https://github.com/Node0o1/ipv4_subnet_calc.git
  ```

#### **Setup**
- after downloading, use the CLI to navigate into the directory
  - No dependancies.

#### **Run**
  - From within the calc_ipv4_subnet directory using CLI:
    - python file.py param1 param2 param3 param4
    - params=(starting ip, subnetmsk, num of borrowed bits, output_file)
    - example: 
      ```py
      python ipv4_subnet_calc.py 192.168.0.0 255.255.0.0 4 ./output_file.txt
      ```

  - you may omit the parameters in CLI and be prompted for each param individually.
    - example:
      ```py
      python ipv4_subnet_calc.py
      ```

      ![PS CLI COMMAND](https://github.com/Node0o1/ipv4_subnet_calc/assets/157242958/a00ac145-1ea4-4e62-8f09-a6300a4e76e2)
      ![RESILTS WRITTEN TO A FILE](https://github.com/Node0o1/ipv4_subnet_calc/assets/157242958/4fa7a3ee-1e9e-4b69-aeaf-ab0597488fca)


