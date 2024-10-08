from flask import Flask, request, jsonify, abort
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.before_request
def validate_request():
    data = request.get_json()
    if not data:
        return jsonify({"message": 'Requisição vazia'}), 400

@app.route('/')
def home():
    return 'API online!'

@app.route('/test_verilog', methods=['POST'])
def test_verilog():
    
    data = request.get_json()
    exercise_id = data['exercise_id']
    exercise_path = os.path.join('tb', str(exercise_id))
    testbench_id = data['testbench_id']
    
    # Verifica se o exercício existe
    if not os.path.isdir(exercise_path):
        return jsonify({"message": 'Exercício não encontrado'}), 400
        
    # Caminhos: teste + gabarito
    gab = exercise_path + f'/gab.v'
    testbench = exercise_path + f'/top_tb{testbench_id}.v'
    
    # Verifica se o testbench existe
    if not os.path.isfile(testbench):
        return jsonify({"message": 'Testbench não encontrado'}), 400
    
    # Cria um diretório temporário para os arquivos da simulação
    with tempfile.TemporaryDirectory() as temp_dir:
        
        # Cria um arquivo .v temporário dentro do diretório temporário
        with tempfile.NamedTemporaryFile(dir=temp_dir, delete=False, suffix='.v', mode='w+') as code:
            code.write(data['verilog_code'])
            code_path = code.name

        simulation_out = temp_dir + 'simulation'
        
        # Compilando o testbench
        comp_test = subprocess.run(
            ['iverilog', '-I', 'tb', '-o', simulation_out, testbench, gab, code_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        if comp_test.returncode == 0:
            # Executar o testbench
            exec_test = subprocess.run(
                ['vvp', simulation_out],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            
            # Dumpfile
            try:
                with open('dump.vcd', 'r') as file:
                    dumpfile = file.read()
                os.remove('dump.vcd')
            except FileNotFoundError:
                pass
        
            if 'ASSERTION FAILED' in exec_test.stdout.strip():
                # Erro de simulação
                return jsonify({"message": f'Erro de simulação em {testbench}', 
                    "tests_passed": False, 
                    "compilation_log": exec_test.stdout.strip(), 
                    "dump": dumpfile,
                    "error": exec_test.stderr.strip(), 
                })            
        else: 
            # Erro de compilação  
            return jsonify({"message": f'Erro de compilação em {testbench}', 
                "tests_passed": False, 
                "compilation_log": comp_test.stdout.strip(), 
                "dump": '',
                "error": comp_test.stderr.strip(), 
            })
        
        # Teste passou
        return jsonify({"message": 'Teste bem-sucedido!', 
                        "tests_passed": True, 
                        "compilation_log": exec_test.stdout.strip(), 
                        "dump": dumpfile,
                        "error": exec_test.stderr.strip(),
        })
        
app.run(debug=True)