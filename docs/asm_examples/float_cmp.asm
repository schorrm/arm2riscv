	.file	"float_cmp.c"
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
	.align	2
	.global	random_double
	.type	random_double, %function
random_double:
	# stp	x29, x30, [sp, -16]!
	sd	x8, -16(sp)
	sd	ra, -8(sp)
	addi	sp, sp, -16 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# bl	rand
	call	rand
	# scvtf	d0, w0
	fcvt.d.w	f10, x10
	# mov	x0, 281474972516352
	li	x10, 281474972516352
	# movk	x0, 0x41df, lsl 48
	not	x27, x0 # set reg to all ones
	srli	x27, x27, 48 # this clears the upper 48 bits in the mask. We'll invert it to get the final mask
	li	x26, 16863 # load our immediate value
	slli	x26, x26, 48 # move the immediate to the parallel place
	slli	x27, x27, 48 # move the mask to the parallel place
	not	x27, x27 # flip the mask to AND against
	and	x10, x10, x27 # clear the target bits in mask
	or	x10, x10, x26 # or in the bits from the immediate to load
	# fmov	d1, x0
	fmv.d.x	f11, x10
	# fdiv	d0, d0, d1
	fdiv.d	f10, f10, f11
	# ldp	x29, x30, [sp], 16
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 16 # writeback
	# ret
	ret
	.size	random_double, .-random_double
	.section	.rodata
	.align	3
.LC0:
	.string	"%lu, %lu\t"
	.align	3
.LC1:
	.string	"<="
	.align	3
.LC2:
	.string	">="
	.align	3
.LC3:
	.string	"=="
	.align	3
.LC4:
	.string	"!="
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# stp	x29, x30, [sp, -48]!
	sd	x8, -48(sp)
	sd	ra, -40(sp)
	addi	sp, sp, -48 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# mov	w0, 123
	li	x10, 123
	# bl	srand
	call	srand
	# mov	w0, 2
	li	x10, 2
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# scvtf	d0, w0
	fcvt.d.w	f10, x10
	# str	d0, [x29, 32]
	fsd	f10, 32(x8)
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# scvtf	d0, w0
	fcvt.d.w	f10, x10
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# str	wzr, [x29, 24]
	sw	x0, 24(x8)
	# b	.L4
	j	.L4
.L15:
	# ldr	x1, [x29, 32]
	ld	x11, 32(x8)
	# ldr	x2, [x29, 40]
	ld	x12, 40(x8)
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# bl	printf
	call	printf
	# ldr	d1, [x29, 32]
	fld	f11, 32(x8)
	# ldr	d0, [x29, 40]
	fld	f10, 40(x8)
	# fcmpe	d1, d0
	flt.d	x25, f11, f10 # this is less than, RHS is bigger
	slli	x25, x25, 63 # move it to the sign bit location
	flt.d	x27, f10, f11 # if LHS is bigger
	or	x25, x25, x27 # or the results together
	# bpl	.L5
	bge	x25, x0, .L5
	# mov	w0, 60
	li	x10, 60
	# bl	putchar
	call	putchar
.L5:
	# ldr	d1, [x29, 32]
	fld	f11, 32(x8)
	# ldr	d0, [x29, 40]
	fld	f10, 40(x8)
	# fcmpe	d1, d0
	flt.d	x25, f11, f10 # this is less than, RHS is bigger
	slli	x25, x25, 63 # move it to the sign bit location
	flt.d	x27, f10, f11 # if LHS is bigger
	or	x25, x25, x27 # or the results together
	# ble	.L7
	ble	x25, x0, .L7
	# mov	w0, 62
	li	x10, 62
	# bl	putchar
	call	putchar
.L7:
	# ldr	d1, [x29, 32]
	fld	f11, 32(x8)
	# ldr	d0, [x29, 40]
	fld	f10, 40(x8)
	# fcmpe	d1, d0
	flt.d	x25, f11, f10 # this is less than, RHS is bigger
	slli	x25, x25, 63 # move it to the sign bit location
	flt.d	x27, f10, f11 # if LHS is bigger
	or	x25, x25, x27 # or the results together
	# bhi	.L9
	bgt	x25, x0, .L9
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# bl	printf
	call	printf
.L9:
	# ldr	d1, [x29, 32]
	fld	f11, 32(x8)
	# ldr	d0, [x29, 40]
	fld	f10, 40(x8)
	# fcmpe	d1, d0
	flt.d	x25, f11, f10 # this is less than, RHS is bigger
	slli	x25, x25, 63 # move it to the sign bit location
	flt.d	x27, f10, f11 # if LHS is bigger
	or	x25, x25, x27 # or the results together
	# blt	.L11
	blt	x25, x0, .L11
	# adrp	x0, .LC2
	lui	x10, %hi(.LC2)
	# add	x0, x0, :lo12:.LC2
	add	x10, x10, %lo(.LC2)
	# bl	printf
	call	printf
.L11:
	# ldr	d1, [x29, 32]
	fld	f11, 32(x8)
	# ldr	d0, [x29, 40]
	fld	f10, 40(x8)
	# fcmp	d1, d0
	flt.d	x25, f11, f10 # this is less than, RHS is bigger
	slli	x25, x25, 63 # move it to the sign bit location
	flt.d	x27, f10, f11 # if LHS is bigger
	or	x25, x25, x27 # or the results together
	# bne	.L13
	bne	x25, x0, .L13
	# adrp	x0, .LC3
	lui	x10, %hi(.LC3)
	# add	x0, x0, :lo12:.LC3
	add	x10, x10, %lo(.LC3)
	# bl	printf
	call	printf
.L13:
	# ldr	d1, [x29, 32]
	fld	f11, 32(x8)
	# ldr	d0, [x29, 40]
	fld	f10, 40(x8)
	# fcmp	d1, d0
	flt.d	x25, f11, f10 # this is less than, RHS is bigger
	slli	x25, x25, 63 # move it to the sign bit location
	flt.d	x27, f10, f11 # if LHS is bigger
	or	x25, x25, x27 # or the results together
	# beq	.L14
	beq	x25, x0, .L14
	# adrp	x0, .LC4
	lui	x10, %hi(.LC4)
	# add	x0, x0, :lo12:.LC4
	add	x10, x10, %lo(.LC4)
	# bl	printf
	call	printf
.L14:
	# mov	w0, 10
	li	x10, 10
	# bl	putchar
	call	putchar
	# bl	random_double
	call	random_double
	# str	d0, [x29, 32]
	fsd	f10, 32(x8)
	# bl	random_double
	call	random_double
	# str	d0, [x29, 40]
	fsd	f10, 40(x8)
	# ldr	w0, [x29, 24]
	lw	x10, 24(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 24]
	sw	x10, 24(x8)
.L4:
	# ldr	w0, [x29, 24]
	lw	x10, 24(x8)
	# cmp	w0, 999
	addi	x25, x10, -999
	# ble	.L15
	ble	x25, x0, .L15
	# mov	w0, 0
	li	x10, 0
	# ldp	x29, x30, [sp], 48
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 48 # writeback
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
