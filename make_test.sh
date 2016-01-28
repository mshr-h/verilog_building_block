cd test
iverilog -o tb_button_debounce.out tb_button_debounce.v
vvp tb_button_debounce.out
iverilog -o tb_ram_sp.out tb_ram_sp.v
vvp tb_ram_sp.out
iverilog -o tb_adder_tree.out tb_adder_tree.v
vvp tb_adder_tree.out
iverilog -o tb_shift_register.out tb_shift_register.v
vvp tb_shift_register.out

cd ../script
python convert2mif.py ../test/ram_content.txt out.mif

