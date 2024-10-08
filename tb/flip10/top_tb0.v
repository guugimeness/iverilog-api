module tb_top0;
    `include "assert.v"
    reg flip;
    wire zero;
    top dut (
        .flip(flip),
        .zero(zero)
    );
    wire gzero;
    gab uut (
        .flip(flip),
        .zero(gzero)
    );
    initial begin
        flip = 1'b0; #1
        `assert(zero, gzero)
        #10 flip = 1'b1; #1
        `assert(zero, gzero)
        $display("DONE");
        $finish;
    end
endmodule