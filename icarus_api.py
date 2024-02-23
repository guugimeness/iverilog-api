import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'API online!'

@app.route('/test')
def simTest():

    nome_arq = 'design.v' # Vai ser passado pela API principal
    testbench = 'design_tb.v' # A ideia seria ter vários casos de teste
    
    # Comandos para compilação e execução do código fornecido pelo usuário
    comando_compilar = f"iverilog -o compilation.vvp {nome_arq}"
    comando_executar = "vvp compilation.vvp"
    
    # Comandos para compilação e execução do teste bench
    comando_test = f"iverilog -o test.vvp {testbench}"
    comando_executarT = "vvp test.vvp"
    
    # Compilando o código do usuário
    resposta_compilar = subprocess.run(comando_compilar, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if resposta_compilar.returncode == 0: # Caso o código compile, prosegue-se para a execução e testes
        resposta_executar = subprocess.run(comando_executar, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Compilando e executando o teste bench
        subprocess.run(comando_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        subprocess.run(comando_executarT, shell=True, text=True)
        
        if resposta_executar.returncode == 0:
            return jsonify({'status': 'OK', 'saida': resposta_executar.stdout})
    
    return jsonify({'status': 'Erro', 'saida': resposta_compilar.stderr})

app.run()