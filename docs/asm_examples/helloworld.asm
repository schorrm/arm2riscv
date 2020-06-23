	.file	"helloworld.c"
        .section .tdata
REG_BANK:
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
        .dword 0
	.text
	.section	.rodata
	.align	3
.LC0:
	.string	"Hello World!"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# stp	x29, x30, [sp, -16]!
	sd	x8, -16(sp)
	sd	ra, -8(sp)
	addi	sp, sp, -16 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# bl	puts
	call	puts
	# mov	w0, 0
	li	x10, 0
	# ldp	x29, x30, [sp], 16
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 16 # writeback
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
