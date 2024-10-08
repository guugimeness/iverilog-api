`define assert(signal, value) \
        if (signal !== value) begin \
            $display("ASSERTION FAILED in %m: signal != value"); \
        end

    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0);
    end