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
## **Images**
<p>With parameters:</p>
<p align="center">
  <img width="755" alt="Screenshot 2024-03-08 141938" src="https://github.com/Node0o1/ipv4_subnet_calc/assets/157242958/206cee88-0c63-4ef3-b915-17831997da90">
</p>
<br/>
<p>Or without parameters:</p>
<p align="center">
  <img width="782" alt="Screenshot 2024-03-08 141519" src="https://github.com/Node0o1/ipv4_subnet_calc/assets/157242958/267694fc-77d2-4a25-a675-d1143337d765">
</p>
<br/>
<p>File contents:</p>
<p align="center">
  <img alt="output file contents" src="https://github.com/Node0o1/ipv4_subnet_calc/assets/157242958/0fe9acd7-521c-4bd6-8c9e-545de82c42ee">
</p>

