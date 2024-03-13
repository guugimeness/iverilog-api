import subprocess
import os
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/')
def home():
    return 'API online!'

@app.before_request
def validate_request():
    data = request.get_json()
    if not data:
        abort(400)

@app.route('/test')
def simTest():
    
    log, dumpfile = '', ''
    tests_passed = False
    response = 'Algum teste falhou!'
    
    data = request.get_json()
    
    # Criando o arquivo .v
    with open('code.v', 'w') as arquivo:
        arquivo.write(data['verilog_code'])
    
    id_exer = data['exercise_id']
    testbench = f'{id_exer}_tb.v' # A ideia seria ter vários casos de teste
    
    # Comandos para compilação e execução do código fornecido pelo usuário
    command_comp = f"iverilog -o compilation.vvp code.v"
    command_exec = "vvp compilation.vvp"
    
    # Comandos para compilação e execução do teste bench
    command_test = f"iverilog -o test.vvp {testbench}"
    command_exec_tb = "vvp -l test.out test.vvp"
    
    # Compilando o código do usuário
    code_comp = subprocess.run(command_comp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    code_exec = subprocess.run(command_exec, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
    # Compilando e executando o teste bench
    test_comp = subprocess.run(command_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    test_exec = subprocess.run(command_exec_tb, shell=True, text=True)
    err = test_comp.stderr

    if test_comp.returncode == 0:
        tests_passed = True
        response = 'Todos os testes passaram!'
        with open('test.out', 'r') as arquivo:
            log = arquivo.read()
        with open('dump.vcd', 'r') as arquivo:
            dumpfile = arquivo.read()
    
    # Excluindo os arquivos de teste
    try:
        os.remove('code.v')
        os.remove('compilation.vvp')
        os.remove('test.vvp')
        os.remove('test.out')
        os.remove('dump.vcd')
    except FileNotFoundError:
        pass
        
    return jsonify({"message": response, 
                    "tests_passed": tests_passed, 
                    "compilation_log": log, 
                    "dump": dumpfile,
                    "error": err, })

app.run()