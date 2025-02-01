vlib work
vlog *.*v
vsim -voptargs=+acc work.FIR_Filter_tb
do wave.do
run -all