cd test
iverilog -o tb_button_debounce.out tb_button_debounce.v
vvp tb_button_debounce.out
iverilog -o tb_ram_sp.out tb_ram_sp.v
vvp tb_ram_sp.out

cd ../script
python convert2mif.py ../test/ram_content.txt out.mif

