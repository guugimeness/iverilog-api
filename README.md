# Judge-API

### Desenvolvimento
API que realiza testes e "julga" códigos Verilog.
Para tal objetivo, foi utilizado Flask e o compilador Icarus.

### Ambiente virtual
Para garantir o funcionamento da API, é importante criar um ambiente virtual dentro desse diretório. ([Tutorial de como criar e rodar um venv](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv))

Após isso, ative o ambiente e instale as dependências necessárias utilizando `pip install -r requirements.txt`.

Se alguma nova dependência for instalada, é preciso atualizar o requirements.txt com `pip freeze > requirements.txt`.

### Icarus Verilog
Para que a API funcione, é preciso ter instalado o compilador de Verilog, Icarus.
```
sudo apt-get install iverilog
```

### Como testar
Com as dependências e o compilador instalados, execute o código, iniciando a API.
Utilizando o VScode, a API é aberta em uma porta do localhost. Após isso, acesse a rota '/test' e já será possível receber uma resposta.
Ps: para testar é preciso adicionar o código Verilog e seu respectivo test bench no diretório. É importante também se atentar ao nome dos arquivos.