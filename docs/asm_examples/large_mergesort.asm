	.file	"large_mergesort.c"
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
	.global	merge
	.type	merge, %function
merge:
	# stp	x29, x30, [sp, -128]!
	sd	x8, -128(sp)
	sd	ra, -120(sp)
	addi	sp, sp, -128 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# str	x19, [sp, 16]
	sd	x18, 16(sp)
	# str	x0, [x29, 56]
	sd	x10, 56(x8)
	# str	w1, [x29, 52]
	sw	x11, 52(x8)
	# str	w2, [x29, 48]
	sw	x12, 48(x8)
	# str	w3, [x29, 44]
	sw	x13, 44(x8)
	# adrp	x0, :got:__stack_chk_guard
	lui	x10, %hi(__stack_chk_guard)
	# ldr	x0, [x0, #:got_lo12:__stack_chk_guard]
	add	x10, x10, %lo(__stack_chk_guard) # load from GOT -> ADD!
	# ldr	x1, [x0]
	ld	x11, 0(x10)
	# str	x1, [x29, 120]
	sd	x11, 120(x8)
	# mov	x1,0
	li	x11, 0
	# mov	x0, sp
	mv	x10, sp
	# mov	x3, x0
	mv	x13, x10
	# ldr	w1, [x29, 48]
	lw	x11, 48(x8)
	# ldr	w0, [x29, 52]
	lw	x10, 52(x8)
	# sub	w0, w1, w0
	subw	x10, x11, x10
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 80]
	sw	x10, 80(x8)
	# ldr	w1, [x29, 44]
	lw	x11, 44(x8)
	# ldr	w0, [x29, 48]
	lw	x10, 48(x8)
	# sub	w0, w1, w0
	subw	x10, x11, x10
	# str	w0, [x29, 84]
	sw	x10, 84(x8)
	# ldr	w0, [x29, 80]
	lw	x10, 80(x8)
	# sxtw	x1, w0
	sext.w	x11, x10
	# sub	x1, x1, #1
	addi	x11, x11, -1
	# str	x1, [x29, 88]
	sd	x11, 88(x8)
	# sxtw	x1, w0
	sext.w	x11, x10
	# mov	x18, x1
	ld	x22, 8(x21) # load of mmapped register
	mv	x22, x11
	sd	x22, 8(x21) # store of mmapped register
	# mov	x19, 0
	li	x18, 0
	# lsr	x1, x18, 59
	ld	x22, 8(x21) # load of mmapped register
	srli	x11, x22, 59
	# lsl	x11, x19, 5
	slli	x7, x18, 5
	# orr	x11, x1, x11
	or	x7, x11, x7
	# lsl	x10, x18, 5
	ld	x22, 8(x21) # load of mmapped register
	slli	x6, x22, 5
	# sxtw	x1, w0
	sext.w	x11, x10
	# mov	x16, x1
	mv	x27, x11
	# mov	x17, 0
	ld	x22, 0(x21) # load of mmapped register
	li	x22, 0
	sd	x22, 0(x21) # store of mmapped register
	# lsr	x1, x16, 59
	srli	x11, x27, 59
	# lsl	x9, x17, 5
	ld	x22, 0(x21) # load of mmapped register
	slli	x5, x22, 5
	# orr	x9, x1, x9
	or	x5, x11, x5
	# lsl	x8, x16, 5
	slli	x9, x27, 5
	# sxtw	x0, w0
	sext.w	x10, x10
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# add	x0, x0, 3
	addi	x10, x10, 3
	# add	x0, x0, 15
	addi	x10, x10, 15
	# lsr	x0, x0, 4
	srli	x10, x10, 4
	# lsl	x0, x0, 4
	slli	x10, x10, 4
	# sub	sp, sp, x0
	sub	sp, sp, x10
	# mov	x0, sp
	mv	x10, sp
	# add	x0, x0, 3
	addi	x10, x10, 3
	# lsr	x0, x0, 2
	srli	x10, x10, 2
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# str	x0, [x29, 96]
	sd	x10, 96(x8)
	# ldr	w0, [x29, 84]
	lw	x10, 84(x8)
	# sxtw	x1, w0
	sext.w	x11, x10
	# sub	x1, x1, #1
	addi	x11, x11, -1
	# str	x1, [x29, 104]
	sd	x11, 104(x8)
	# sxtw	x1, w0
	sext.w	x11, x10
	# mov	x14, x1
	mv	x30, x11
	# mov	x15, 0
	li	x31, 0
	# lsr	x1, x14, 59
	srli	x11, x30, 59
	# lsl	x7, x15, 5
	slli	x17, x31, 5
	# orr	x7, x1, x7
	or	x17, x11, x17
	# lsl	x6, x14, 5
	slli	x16, x30, 5
	# sxtw	x1, w0
	sext.w	x11, x10
	# mov	x12, x1
	mv	x28, x11
	# mov	x13, 0
	li	x29, 0
	# lsr	x1, x12, 59
	srli	x11, x28, 59
	# lsl	x5, x13, 5
	slli	x15, x29, 5
	# orr	x5, x1, x5
	or	x15, x11, x15
	# lsl	x4, x12, 5
	slli	x14, x28, 5
	# sxtw	x0, w0
	sext.w	x10, x10
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# add	x0, x0, 3
	addi	x10, x10, 3
	# add	x0, x0, 15
	addi	x10, x10, 15
	# lsr	x0, x0, 4
	srli	x10, x10, 4
	# lsl	x0, x0, 4
	slli	x10, x10, 4
	# sub	sp, sp, x0
	sub	sp, sp, x10
	# mov	x0, sp
	mv	x10, sp
	# add	x0, x0, 3
	addi	x10, x10, 3
	# lsr	x0, x0, 2
	srli	x10, x10, 2
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# str	x0, [x29, 112]
	sd	x10, 112(x8)
	# str	wzr, [x29, 76]
	sw	x0, 76(x8)
	# b	.L2
	j	.L2
.L3:
	# ldr	w1, [x29, 52]
	lw	x11, 52(x8)
	# ldr	w0, [x29, 76]
	lw	x10, 76(x8)
	# add	w0, w1, w0
	addw	x10, x11, x10
	# sxtw	x0, w0
	sext.w	x10, x10
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# ldr	x1, [x29, 56]
	ld	x11, 56(x8)
	# add	x0, x1, x0
	add	x10, x11, x10
	# ldr	w2, [x0]
	lw	x12, 0(x10)
	# ldr	x0, [x29, 96]
	ld	x10, 96(x8)
	# ldrsw	x1, [x29, 76]
	lw	x11, 76(x8)
	# str	w2, [x0, x1, lsl 2]
	slli	x26, x11, 2
	add	x26, x26, x10 # converting offset register to add
	sw	x12, 0(x26)
	# ldr	w0, [x29, 76]
	lw	x10, 76(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 76]
	sw	x10, 76(x8)
.L2:
	# ldr	w1, [x29, 76]
	lw	x11, 76(x8)
	# ldr	w0, [x29, 80]
	lw	x10, 80(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# blt	.L3
	blt	x25, x0, .L3
	# str	wzr, [x29, 72]
	sw	x0, 72(x8)
	# b	.L4
	j	.L4
.L5:
	# ldr	w0, [x29, 48]
	lw	x10, 48(x8)
	# add	w1, w0, 1
	addiw	x11, x10, 1
	# ldr	w0, [x29, 72]
	lw	x10, 72(x8)
	# add	w0, w1, w0
	addw	x10, x11, x10
	# sxtw	x0, w0
	sext.w	x10, x10
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# ldr	x1, [x29, 56]
	ld	x11, 56(x8)
	# add	x0, x1, x0
	add	x10, x11, x10
	# ldr	w2, [x0]
	lw	x12, 0(x10)
	# ldr	x0, [x29, 112]
	ld	x10, 112(x8)
	# ldrsw	x1, [x29, 72]
	lw	x11, 72(x8)
	# str	w2, [x0, x1, lsl 2]
	slli	x26, x11, 2
	add	x26, x26, x10 # converting offset register to add
	sw	x12, 0(x26)
	# ldr	w0, [x29, 72]
	lw	x10, 72(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 72]
	sw	x10, 72(x8)
.L4:
	# ldr	w1, [x29, 72]
	lw	x11, 72(x8)
	# ldr	w0, [x29, 84]
	lw	x10, 84(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# blt	.L5
	blt	x25, x0, .L5
	# str	wzr, [x29, 76]
	sw	x0, 76(x8)
	# str	wzr, [x29, 72]
	sw	x0, 72(x8)
	# ldr	w0, [x29, 52]
	lw	x10, 52(x8)
	# str	w0, [x29, 68]
	sw	x10, 68(x8)
	# b	.L6
	j	.L6
.L10:
	# ldr	x0, [x29, 96]
	ld	x10, 96(x8)
	# ldrsw	x1, [x29, 76]
	lw	x11, 76(x8)
	# ldr	w1, [x0, x1, lsl 2]
	slli	x26, x11, 2
	add	x26, x26, x10 # converting offset register to add
	lw	x11, 0(x26)
	# ldr	x0, [x29, 112]
	ld	x10, 112(x8)
	# ldrsw	x2, [x29, 72]
	lw	x12, 72(x8)
	# ldr	w0, [x0, x2, lsl 2]
	slli	x26, x12, 2
	add	x26, x26, x10 # converting offset register to add
	lw	x10, 0(x26)
	# cmp	w1, w0
	sub	x25, x11, x10
	# bgt	.L7
	bgt	x25, x0, .L7
	# ldrsw	x0, [x29, 68]
	lw	x10, 68(x8)
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# ldr	x1, [x29, 56]
	ld	x11, 56(x8)
	# add	x0, x1, x0
	add	x10, x11, x10
	# ldr	x1, [x29, 96]
	ld	x11, 96(x8)
	# ldrsw	x2, [x29, 76]
	lw	x12, 76(x8)
	# ldr	w1, [x1, x2, lsl 2]
	slli	x26, x12, 2
	add	x26, x26, x11 # converting offset register to add
	lw	x11, 0(x26)
	# str	w1, [x0]
	sw	x11, 0(x10)
	# ldr	w0, [x29, 76]
	lw	x10, 76(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 76]
	sw	x10, 76(x8)
	# b	.L8
	j	.L8
.L7:
	# ldrsw	x0, [x29, 68]
	lw	x10, 68(x8)
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# ldr	x1, [x29, 56]
	ld	x11, 56(x8)
	# add	x0, x1, x0
	add	x10, x11, x10
	# ldr	x1, [x29, 112]
	ld	x11, 112(x8)
	# ldrsw	x2, [x29, 72]
	lw	x12, 72(x8)
	# ldr	w1, [x1, x2, lsl 2]
	slli	x26, x12, 2
	add	x26, x26, x11 # converting offset register to add
	lw	x11, 0(x26)
	# str	w1, [x0]
	sw	x11, 0(x10)
	# ldr	w0, [x29, 72]
	lw	x10, 72(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 72]
	sw	x10, 72(x8)
.L8:
	# ldr	w0, [x29, 68]
	lw	x10, 68(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 68]
	sw	x10, 68(x8)
.L6:
	# ldr	w1, [x29, 76]
	lw	x11, 76(x8)
	# ldr	w0, [x29, 80]
	lw	x10, 80(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# bge	.L11
	bge	x25, x0, .L11
	# ldr	w1, [x29, 72]
	lw	x11, 72(x8)
	# ldr	w0, [x29, 84]
	lw	x10, 84(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# blt	.L10
	blt	x25, x0, .L10
	# b	.L11
	j	.L11
.L12:
	# ldrsw	x0, [x29, 68]
	lw	x10, 68(x8)
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# ldr	x1, [x29, 56]
	ld	x11, 56(x8)
	# add	x0, x1, x0
	add	x10, x11, x10
	# ldr	x1, [x29, 96]
	ld	x11, 96(x8)
	# ldrsw	x2, [x29, 76]
	lw	x12, 76(x8)
	# ldr	w1, [x1, x2, lsl 2]
	slli	x26, x12, 2
	add	x26, x26, x11 # converting offset register to add
	lw	x11, 0(x26)
	# str	w1, [x0]
	sw	x11, 0(x10)
	# ldr	w0, [x29, 76]
	lw	x10, 76(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 76]
	sw	x10, 76(x8)
	# ldr	w0, [x29, 68]
	lw	x10, 68(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 68]
	sw	x10, 68(x8)
.L11:
	# ldr	w1, [x29, 76]
	lw	x11, 76(x8)
	# ldr	w0, [x29, 80]
	lw	x10, 80(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# blt	.L12
	blt	x25, x0, .L12
	# b	.L13
	j	.L13
.L14:
	# ldrsw	x0, [x29, 68]
	lw	x10, 68(x8)
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# ldr	x1, [x29, 56]
	ld	x11, 56(x8)
	# add	x0, x1, x0
	add	x10, x11, x10
	# ldr	x1, [x29, 112]
	ld	x11, 112(x8)
	# ldrsw	x2, [x29, 72]
	lw	x12, 72(x8)
	# ldr	w1, [x1, x2, lsl 2]
	slli	x26, x12, 2
	add	x26, x26, x11 # converting offset register to add
	lw	x11, 0(x26)
	# str	w1, [x0]
	sw	x11, 0(x10)
	# ldr	w0, [x29, 72]
	lw	x10, 72(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 72]
	sw	x10, 72(x8)
	# ldr	w0, [x29, 68]
	lw	x10, 68(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 68]
	sw	x10, 68(x8)
.L13:
	# ldr	w1, [x29, 72]
	lw	x11, 72(x8)
	# ldr	w0, [x29, 84]
	lw	x10, 84(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# blt	.L14
	blt	x25, x0, .L14
	# mov	sp, x3
	mv	sp, x13
	# nop
	nop
	# adrp	x0, :got:__stack_chk_guard
	lui	x10, %hi(__stack_chk_guard)
	# ldr	x0, [x0, #:got_lo12:__stack_chk_guard]
	add	x10, x10, %lo(__stack_chk_guard) # load from GOT -> ADD!
	# ldr	x1, [x29, 120]
	ld	x11, 120(x8)
	# ldr	x0, [x0]
	ld	x10, 0(x10)
	# eor	x0, x1, x0
	xor	x10, x11, x10
	# cmp	x0, 0
	addi	x25, x10, 0
	# beq	.L15
	beq	x25, x0, .L15
	# bl	__stack_chk_fail
	call	__stack_chk_fail
.L15:
	# add	sp, x29, 0
	addi	sp, x8, 0
	# ldr	x19, [sp, 16]
	ld	x18, 16(sp)
	# ldp	x29, x30, [sp], 128
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 128 # writeback
	# ret
	ret
	.size	merge, .-merge
	.align	2
	.global	mergeSort
	.type	mergeSort, %function
mergeSort:
	# stp	x29, x30, [sp, -48]!
	sd	x8, -48(sp)
	sd	ra, -40(sp)
	addi	sp, sp, -48 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# str	x0, [x29, 24]
	sd	x10, 24(x8)
	# str	w1, [x29, 20]
	sw	x11, 20(x8)
	# str	w2, [x29, 16]
	sw	x12, 16(x8)
	# ldr	w1, [x29, 20]
	lw	x11, 20(x8)
	# ldr	w0, [x29, 16]
	lw	x10, 16(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# bge	.L18
	bge	x25, x0, .L18
	# ldr	w1, [x29, 16]
	lw	x11, 16(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# sub	w0, w1, w0
	subw	x10, x11, x10
	# lsr	w1, w0, 31
	srliw	x11, x10, 31
	# add	w0, w1, w0
	addw	x10, x11, x10
	# asr	w0, w0, 1
	sraiw	x10, x10, 1
	# mov	w1, w0
	mv	x11, x10
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# add	w0, w0, w1
	addw	x10, x10, x11
	# str	w0, [x29, 44]
	sw	x10, 44(x8)
	# ldr	w2, [x29, 44]
	lw	x12, 44(x8)
	# ldr	w1, [x29, 20]
	lw	x11, 20(x8)
	# ldr	x0, [x29, 24]
	ld	x10, 24(x8)
	# bl	mergeSort
	call	mergeSort
	# ldr	w0, [x29, 44]
	lw	x10, 44(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# ldr	w2, [x29, 16]
	lw	x12, 16(x8)
	# mov	w1, w0
	mv	x11, x10
	# ldr	x0, [x29, 24]
	ld	x10, 24(x8)
	# bl	mergeSort
	call	mergeSort
	# ldr	w3, [x29, 16]
	lw	x13, 16(x8)
	# ldr	w2, [x29, 44]
	lw	x12, 44(x8)
	# ldr	w1, [x29, 20]
	lw	x11, 20(x8)
	# ldr	x0, [x29, 24]
	ld	x10, 24(x8)
	# bl	merge
	call	merge
.L18:
	# nop
	nop
	# ldp	x29, x30, [sp], 48
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 48 # writeback
	# ret
	ret
	.size	mergeSort, .-mergeSort
	.section	.rodata
	.align	3
.LC0:
	.string	"%d "
	.text
	.align	2
	.global	printArray
	.type	printArray, %function
printArray:
	# stp	x29, x30, [sp, -48]!
	sd	x8, -48(sp)
	sd	ra, -40(sp)
	addi	sp, sp, -48 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# str	x0, [x29, 24]
	sd	x10, 24(x8)
	# str	w1, [x29, 20]
	sw	x11, 20(x8)
	# str	wzr, [x29, 44]
	sw	x0, 44(x8)
	# b	.L20
	j	.L20
.L21:
	# ldrsw	x0, [x29, 44]
	lw	x10, 44(x8)
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# ldr	x1, [x29, 24]
	ld	x11, 24(x8)
	# add	x0, x1, x0
	add	x10, x11, x10
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# bl	printf
	call	printf
	# ldr	w0, [x29, 44]
	lw	x10, 44(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 44]
	sw	x10, 44(x8)
.L20:
	# ldr	w1, [x29, 44]
	lw	x11, 44(x8)
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# blt	.L21
	blt	x25, x0, .L21
	# mov	w0, 10
	li	x10, 10
	# bl	putchar
	call	putchar
	# nop
	nop
	# ldp	x29, x30, [sp], 48
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 48 # writeback
	# ret
	ret
	.size	printArray, .-printArray
	.section	.rodata
	.align	3
.LC1:
	.string	"Given array is "
	.align	3
.LC2:
	.string	"\nSorted array is "
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# mov	x16, 40032
	li	x27, 40032
	# sub	sp, sp, x16
	sub	sp, sp, x27
	# stp	x29, x30, [sp]
	sd	x8, 0(sp)
	sd	ra, 8(sp)
	# add	x29, sp, 0
	addi	x8, sp, 0
	# adrp	x0, :got:__stack_chk_guard
	lui	x10, %hi(__stack_chk_guard)
	# ldr	x0, [x0, #:got_lo12:__stack_chk_guard]
	add	x10, x10, %lo(__stack_chk_guard) # load from GOT -> ADD!
	# add	x1, x29, 32768
	li	x26, 32768 # synthesis of oversized immediate
	add	x11, x8, x26
	# ldr	x2, [x0]
	ld	x12, 0(x10)
	# str	x2, [x1, 7256]
	li	x26, 7256 # synthesis of oversized immediate
	add	x26, x26, x11 # converting offset register to add
	sd	x12, 0(x26)
	# mov	x2,0
	li	x12, 0
	# mov	w0, 1234
	li	x10, 1234
	# bl	srand
	call	srand
	# str	wzr, [x29, 16]
	sw	x0, 16(x8)
	# b	.L23
	j	.L23
.L24:
	# bl	random
	call	random
	# mov	w2, w0
	mv	x12, x10
	# ldrsw	x0, [x29, 16]
	lw	x10, 16(x8)
	# lsl	x0, x0, 2
	slli	x10, x10, 2
	# add	x1, x29, 24
	addi	x11, x8, 24
	# str	w2, [x1, x0]
	add	x26, x10, x11 # converting offset register to add
	sw	x12, 0(x26)
	# ldr	w0, [x29, 16]
	lw	x10, 16(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 16]
	sw	x10, 16(x8)
.L23:
	# ldr	w1, [x29, 16]
	lw	x11, 16(x8)
	# mov	w0, 9999
	li	x10, 9999
	# cmp	w1, w0
	sub	x25, x11, x10
	# ble	.L24
	ble	x25, x0, .L24
	# mov	w0, 10000
	li	x10, 10000
	# str	w0, [x29, 20]
	sw	x10, 20(x8)
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# bl	puts
	call	puts
	# add	x0, x29, 24
	addi	x10, x8, 24
	# ldr	w1, [x29, 20]
	lw	x11, 20(x8)
	# bl	printArray
	call	printArray
	# ldr	w0, [x29, 20]
	lw	x10, 20(x8)
	# sub	w1, w0, #1
	addiw	x11, x10, -1
	# add	x0, x29, 24
	addi	x10, x8, 24
	# mov	w2, w1
	mv	x12, x11
	# mov	w1, 0
	li	x11, 0
	# bl	mergeSort
	call	mergeSort
	# adrp	x0, .LC2
	lui	x10, %hi(.LC2)
	# add	x0, x0, :lo12:.LC2
	add	x10, x10, %lo(.LC2)
	# bl	puts
	call	puts
	# add	x0, x29, 24
	addi	x10, x8, 24
	# ldr	w1, [x29, 20]
	lw	x11, 20(x8)
	# bl	printArray
	call	printArray
	# mov	w0, 0
	li	x10, 0
	# adrp	x1, :got:__stack_chk_guard
	lui	x11, %hi(__stack_chk_guard)
	# ldr	x1, [x1, #:got_lo12:__stack_chk_guard]
	add	x11, x11, %lo(__stack_chk_guard) # load from GOT -> ADD!
	# add	x2, x29, 32768
	li	x26, 32768 # synthesis of oversized immediate
	add	x12, x8, x26
	# ldr	x3, [x2, 7256]
	li	x26, 7256 # synthesis of oversized immediate
	add	x26, x26, x12 # converting offset register to add
	ld	x13, 0(x26)
	# ldr	x1, [x1]
	ld	x11, 0(x11)
	# eor	x1, x3, x1
	xor	x11, x13, x11
	# cmp	x1, 0
	addi	x25, x11, 0
	# beq	.L26
	beq	x25, x0, .L26
	# bl	__stack_chk_fail
	call	__stack_chk_fail
.L26:
	# ldp	x29, x30, [sp]
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	# mov	x16, 40032
	li	x27, 40032
	# add	sp, sp, x16
	add	sp, sp, x27
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
