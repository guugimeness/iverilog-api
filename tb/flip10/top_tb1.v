module tb_top1;
    `include "assert.v"
    reg flip;
    wire one;
    top dut (
        .flip(flip),
        .one(one)
    );
    wire gone;
    gab uut (
        .flip(flip),
        .one(gone)
    );
    initial begin
        flip = 1'b0; #1
        `assert(one, gone)
        #10 flip = 1'b1; #1
        `assert(one, gone)
        $display("DONE");
        $finish;
    end
endmodule