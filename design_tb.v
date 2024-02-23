`timescale 1ns/1ns  // Define a escala de tempo para a simulação
`include "design.v"

module and_gate_tb;

    // Parâmetros de entrada para o testbench
    reg a;
    reg b;

    // Saída do módulo
    wire c;

    // Instanciar o módulo que está sendo testado
    and_gate dut (
        .a(a),
        .b(b),
        .c(c)
    );

    // Declaração do dumpfile
    initial begin
        $dumpfile("dump.vcd"); // Nome do arquivo de despejo (pode ser qualquer nome)
        $dumpvars(0, and_gate_tb); // Inclui todas as variáveis do testbench no despejo
    end

    // Estímulos de entrada
    initial begin
        $monitor("Time=%0t a=%b b=%b c=%b", $time, a, b, c);
        
        // Teste 1: a = 0, b = 0
        #10 a = 0; b = 0;
        
        // Teste 2: a = 1, b = 0
        #10 a = 1; b = 0;
        
        // Teste 3: a = 0, b = 1
        #10 a = 0; b = 1;
        
        // Teste 4: a = 1, b = 1
        #10 a = 1; b = 1;
        
        // Finalizar a simulação
        #10 $finish;
    end

endmodule
