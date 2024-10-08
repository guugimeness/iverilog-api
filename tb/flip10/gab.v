module gab (
    input flip,
    output zero, one
);
    // Pro mode stuff
    assign zero = flip;
    assign one = ~flip;
endmodule 