simple ARM assembler examples
compile with gcc like this:

gcc -o asm1 asm.s

simplest ones do not use print but return value to shell. You can print it in the shell with 
echo $? (be aware that value has to be < 255 )
