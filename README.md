# Iverilog-API

### Development
API that performs tests and "judges" Verilog codes. 
For this purpose, Flask and the Icarus compiler were used.

### Virtual environment
To ensure the API works, it's important to create a virtual environment within this directory. ([How to create and run a venv](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv))

After that, activate the environment and install the necessary dependencies using `pip install -r requirements.txt`.

### Icarus Verilog
For the API to work, you must have the Verilog compiler, Icarus, installed.
```
sudo apt-get install iverilog
```

### How to test
With the dependencies and compiler installed, run the code, starting the API. Using VScode, the API is opened on a localhost port. After that, access the '/test' route and you will be able to receive a response. 
Ps: to test you need to add the Verilog code and its respective test bench to the directory. It is also important to pay attention to the name of the files.