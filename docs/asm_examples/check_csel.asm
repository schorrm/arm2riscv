	.file	"check_csel.c"
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
	.string	"The smaller number is: %d\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# stp	x29, x30, [sp, -32]!
	sd	x8, -32(sp)
	sd	ra, -24(sp)
	addi	sp, sp, -32 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# mov	w0, 32
	li	x10, 32
	# str	w0, [x29, 20]
	sw	x10, 20(x8)
	# mov	w0, 35
	li	x10, 35
	# str	w0, [x29, 24]
	sw	x10, 24(x8)
	# str	wzr, [x29, 28]
	sw	x0, 28(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# ldr	w1, [x29, 24]
	lw	x11, 24(x8)
#APP
	# mov x10, x0
	mv	x6, x10
	# mov x11, x1
	mv	x7, x11
	# cmp x10, x11
	sub	x25, x6, x7
	# csel x0, x10, x11, LE
	add	x27, x6, x0 # move option s1 to temp
	ble	x25, x0, 999999f # conditionally branch past moving option s2 to temp 
	add	x27, x7, x0 # move s2 to temp
	999999:
	add	x10, x0, x27 # move temp to dest
#NO_APP
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# ldr	w1, [x29, 28]
	lw	x11, 28(x8)
	# bl	printf
	call	printf
	# mov	w0, 0
	li	x10, 0
	# ldp	x29, x30, [sp], 32
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 32 # writeback
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
