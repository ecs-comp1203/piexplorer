@ comp1203 template code
@ shows how to print an integer with printf

.data
        .balign  4
	fmtstring: .asciz "%d\n"
	num: .int 0
.text
        .global main
	.extern printf

main:
push {ip, lr}			@ save link register as we will re-use it here
	@ our code here
	ldr r1, =1000000
	mov r0, #2
        mul     r0, r0, r1

	@ print the result
	mov r1, r0		
	ldr r0, =fmtstring
	bl printf

pop {ip, pc}			@ get original values for return to shell

adr_num: .word num
