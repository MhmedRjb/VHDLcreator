module alu_TB();
reg a_TB,
reg B_TB,
reg C_TB,
reg D_TB,
 wire OB_TB,
 wire hgf_TB,
 wire gf_TB


//internal_signals
  reg fsdgsyu_TB;

alu alu_inst(
.a(a_TB),
.B(B_TB),
.C(C_TB),
.D(D_TB),
.OB(OB_TB),
.hgf(hgf_TB),
.gf(gf_TB)
);

endmodule
