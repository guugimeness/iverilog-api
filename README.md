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
With the dependencies and compiler installed, run the code, starting the API. Using VScode, the API is opened on a localhost port. After that, it's possible to make a request to the '/test' route, passing as a parameter a json that follows the model below.
```
data = {
  "verilog_code": "Verilog code to test",
  "user_id": "user identifier",
  "exercise_id": "exercise identifier"
}

response = requests.get('http://127.0.0.1:5000/test', json=data)
```
Ps: The test bench is named by "exercise_id". For example, the exercise with id 1 will be tested by "1_tb.v"

### Response
By default, the API returns json containing the following information:
```
{
  "compilation_log": "icarus raw compilation log",
  "dump": "wave file generated on the test bench",
  "error_log": "error message, if any",
  "message": "informs whether the tests passed or not",
  "tests_passed": "true or false, whether the tests passed"
}
```