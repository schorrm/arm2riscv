	.file	"thread_amotests.c"
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
	.global	atomic_counter
	.bss
	.align	2
	.type	atomic_counter, %object
	.size	atomic_counter, 4
atomic_counter:
	.zero	4
	.global	total_sum
	.align	2
	.type	total_sum, %object
	.size	total_sum, 4
total_sum:
	.zero	4
	.global	or_check
	.align	2
	.type	or_check, %object
	.size	or_check, 4
or_check:
	.zero	4
	.global	xor_check
	.align	2
	.type	xor_check, %object
	.size	xor_check, 4
xor_check:
	.zero	4
	.global	and_check
	.data
	.align	2
	.type	and_check, %object
	.size	and_check, 4
and_check:
	.word	1000
	.global	and_check_2
	.align	2
	.type	and_check_2, %object
	.size	and_check_2, 4
and_check_2:
	.word	1000
	.global	min_check
	.align	3
	.type	min_check, %object
	.size	min_check, 8
min_check:
	.dword	10000
	.global	unsigned_min_check
	.align	3
	.type	unsigned_min_check, %object
	.size	unsigned_min_check, 8
unsigned_min_check:
	.dword	10000
	.global	max_check
	.bss
	.align	3
	.type	max_check, %object
	.size	max_check, 8
max_check:
	.zero	8
	.global	unsigned_max_check
	.align	3
	.type	unsigned_max_check, %object
	.size	unsigned_max_check, 8
unsigned_max_check:
	.zero	8
	.global	ts
	.data
	.align	3
	.type	ts, %object
	.size	ts, 16
ts:
	.dword	0
	.dword	1000
	.text
	.align	2
	.global	mythread
	.type	mythread, %function
mythread:
	# sub	sp, sp, #32
	addi	sp, sp, -32
	# str	x0, [sp, 8]
	sd	x10, 8(sp)
	# ldr	x0, [sp, 8]
	ld	x10, 8(sp)
	# ldr	w0, [x0]
	lw	x10, 0(x10)
	# str	w0, [sp, 24]
	sw	x10, 24(sp)
	# ldr	w0, [sp, 24]
	lw	x10, 24(sp)
	# str	w0, [sp, 28]
	sw	x10, 28(sp)
	# str	wzr, [sp, 20]
	sw	x0, 20(sp)
	# b	.L2
	j	.L2
.L3:
	# adrp	x0, atomic_counter
	lui	x10, %hi(atomic_counter)
	# add	x0, x0, :lo12:atomic_counter
	add	x10, x10, %lo(atomic_counter)
	# mov	w1, 1
	li	x11, 1
	# ldaddal	w1, w1, [x0]
	amoadd.w.aqrl	x11, x11, (x10)
	# ldr	w1, [sp, 24]
	lw	x11, 24(sp)
	# adrp	x0, total_sum
	lui	x10, %hi(total_sum)
	# add	x0, x0, :lo12:total_sum
	add	x10, x10, %lo(total_sum)
	# ldaddal	w1, w2, [x0]
	amoadd.w.aqrl	x12, x11, (x10)
	# ldr	w1, [sp, 24]
	lw	x11, 24(sp)
	# adrp	x0, xor_check
	lui	x10, %hi(xor_check)
	# add	x0, x0, :lo12:xor_check
	add	x10, x10, %lo(xor_check)
	# ldeoral	w1, w2, [x0]
	amoxor.w.aqrl	x12, x11, (x10)
	# ldr	w1, [sp, 24]
	lw	x11, 24(sp)
	# adrp	x0, or_check
	lui	x10, %hi(or_check)
	# add	x0, x0, :lo12:or_check
	add	x10, x10, %lo(or_check)
	# ldsetal	w1, w2, [x0]
	amoor.w.aqrl	x12, x11, (x10)
	# mov	w1, 1000
	li	x11, 1000
	# ldr	w0, [sp, 24]
	lw	x10, 24(sp)
	# sub	w0, w1, w0
	subw	x10, x11, x10
	# mov	w1, w0
	mv	x11, x10
	# adrp	x0, and_check
	lui	x10, %hi(and_check)
	# add	x0, x0, :lo12:and_check
	add	x10, x10, %lo(and_check)
	# mov	w2, w1
	mv	x12, x11
	# mvn	w2, w2
	mv	x12, x12
	not	x12, x12
	# ldclral	w2, w2, [x0]
	not	x27, x12
	amoand.w.aqrl	x12, x27, (x10)
	# adrp	x0, and_check_2
	lui	x10, %hi(and_check_2)
	# add	x0, x0, :lo12:and_check_2
	add	x10, x10, %lo(and_check_2)
	# mov	w1, 1000
	li	x11, 1000
	# mov	w2, w1
	mv	x12, x11
	# mvn	w2, w2
	mv	x12, x12
	not	x12, x12
	# ldclral	w2, w2, [x0]
	not	x27, x12
	amoand.w.aqrl	x12, x27, (x10)
	# adrp	x0, min_check
	lui	x10, %hi(min_check)
	# add	x0, x0, :lo12:min_check
	add	x10, x10, %lo(min_check)
	# ldr	w1, [sp, 24]
	lw	x11, 24(sp)
#APP
	# ldsminal x1, x1, [x0]
	amomin.d.aqrl	x11, x11, (x10)
#NO_APP
	# adrp	x0, max_check
	lui	x10, %hi(max_check)
	# add	x0, x0, :lo12:max_check
	add	x10, x10, %lo(max_check)
	# ldr	w1, [sp, 24]
	lw	x11, 24(sp)
#APP
	# ldsmaxal x1, x1, [x0]
	amomax.d.aqrl	x11, x11, (x10)
#NO_APP
	# adrp	x0, unsigned_min_check
	lui	x10, %hi(unsigned_min_check)
	# add	x0, x0, :lo12:unsigned_min_check
	add	x10, x10, %lo(unsigned_min_check)
	# ldr	w1, [sp, 24]
	lw	x11, 24(sp)
#APP
	# lduminal x1, x1, [x0]
	amominu.d.aqrl	x11, x11, (x10)
#NO_APP
	# adrp	x0, unsigned_max_check
	lui	x10, %hi(unsigned_max_check)
	# add	x0, x0, :lo12:unsigned_max_check
	add	x10, x10, %lo(unsigned_max_check)
	# ldr	w1, [sp, 24]
	lw	x11, 24(sp)
#APP
	# ldumaxal x1, x1, [x0]
	amomaxu.d.aqrl	x11, x11, (x10)
#NO_APP
	# ldr	w0, [sp, 20]
	lw	x10, 20(sp)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [sp, 20]
	sw	x10, 20(sp)
.L2:
	# ldr	w0, [sp, 20]
	lw	x10, 20(sp)
	# cmp	w0, 9
	addi	x25, x10, -9
	# ble	.L3
	ble	x25, x0, .L3
	# mov	x0, 0
	li	x10, 0
	# add	sp, sp, 32
	addi	sp, sp, 32
	# ret
	ret
	.size	mythread, .-mythread
	.section	.rodata
	.align	3
.LC0:
	.string	"atomic add %d\n"
	.align	3
.LC1:
	.string	"atomic ad2 %d\n"
	.align	3
.LC2:
	.string	"atomic xor %d\n"
	.align	3
.LC3:
	.string	"atomic or  %d\n"
	.align	3
.LC4:
	.string	"atomic and %d\n"
	.align	3
.LC5:
	.string	"atomic an2 %d\n"
	.align	3
.LC6:
	.string	"atomic min %ld\n"
	.align	3
.LC7:
	.string	"atomic max %ld\n"
	.align	3
.LC8:
	.string	"atomic umn %ld\n"
	.align	3
.LC9:
	.string	"atomic umx %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	la	x21, REG_BANK
	# mov	x16, 8048
	li	x27, 8048
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
	# ldr	x1, [x0]
	ld	x11, 0(x10)
	# str	x1, [x29, 8040]
	li	x26, 8040 # synthesis of oversized immediate
	add	x26, x26, x8 # converting offset register to add
	sd	x11, 0(x26)
	# mov	x1,0
	li	x11, 0
	# str	wzr, [x29, 28]
	sw	x0, 28(x8)
	# b	.L6
	j	.L6
.L7:
	# mov	x0, 4
	li	x10, 4
	# bl	malloc
	call	malloc
	# str	x0, [x29, 32]
	sd	x10, 32(x8)
	# ldr	x0, [x29, 32]
	ld	x10, 32(x8)
	# ldr	w1, [x29, 28]
	lw	x11, 28(x8)
	# str	w1, [x0]
	sw	x11, 0(x10)
	# add	x1, x29, 40
	addi	x11, x8, 40
	# ldrsw	x0, [x29, 28]
	lw	x10, 28(x8)
	# lsl	x0, x0, 3
	slli	x10, x10, 3
	# add	x4, x1, x0
	add	x14, x11, x10
	# adrp	x0, mythread
	lui	x10, %hi(mythread)
	# add	x0, x0, :lo12:mythread
	add	x10, x10, %lo(mythread)
	# ldr	x3, [x29, 32]
	ld	x13, 32(x8)
	# mov	x2, x0
	mv	x12, x10
	# mov	x1, 0
	li	x11, 0
	# mov	x0, x4
	mv	x10, x14
	# bl	pthread_create
	call	pthread_create
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
.L6:
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# cmp	w0, 999
	addi	x25, x10, -999
	# ble	.L7
	ble	x25, x0, .L7
	# str	wzr, [x29, 28]
	sw	x0, 28(x8)
	# b	.L8
	j	.L8
.L9:
	# ldrsw	x0, [x29, 28]
	lw	x10, 28(x8)
	# lsl	x0, x0, 3
	slli	x10, x10, 3
	# add	x1, x29, 40
	addi	x11, x8, 40
	# ldr	x0, [x1, x0]
	add	x26, x10, x11 # converting offset register to add
	ld	x10, 0(x26)
	# mov	x1, 0
	li	x11, 0
	# bl	pthread_join
	call	pthread_join
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
.L8:
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# cmp	w0, 999
	addi	x25, x10, -999
	# ble	.L9
	ble	x25, x0, .L9
	# adrp	x0, atomic_counter
	lui	x10, %hi(atomic_counter)
	# add	x0, x0, :lo12:atomic_counter
	add	x10, x10, %lo(atomic_counter)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# bl	printf
	call	printf
	# adrp	x0, total_sum
	lui	x10, %hi(total_sum)
	# add	x0, x0, :lo12:total_sum
	add	x10, x10, %lo(total_sum)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# bl	printf
	call	printf
	# adrp	x0, xor_check
	lui	x10, %hi(xor_check)
	# add	x0, x0, :lo12:xor_check
	add	x10, x10, %lo(xor_check)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC2
	lui	x10, %hi(.LC2)
	# add	x0, x0, :lo12:.LC2
	add	x10, x10, %lo(.LC2)
	# bl	printf
	call	printf
	# adrp	x0, or_check
	lui	x10, %hi(or_check)
	# add	x0, x0, :lo12:or_check
	add	x10, x10, %lo(or_check)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC3
	lui	x10, %hi(.LC3)
	# add	x0, x0, :lo12:.LC3
	add	x10, x10, %lo(.LC3)
	# bl	printf
	call	printf
	# adrp	x0, and_check
	lui	x10, %hi(and_check)
	# add	x0, x0, :lo12:and_check
	add	x10, x10, %lo(and_check)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC4
	lui	x10, %hi(.LC4)
	# add	x0, x0, :lo12:.LC4
	add	x10, x10, %lo(.LC4)
	# bl	printf
	call	printf
	# adrp	x0, and_check_2
	lui	x10, %hi(and_check_2)
	# add	x0, x0, :lo12:and_check_2
	add	x10, x10, %lo(and_check_2)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC5
	lui	x10, %hi(.LC5)
	# add	x0, x0, :lo12:.LC5
	add	x10, x10, %lo(.LC5)
	# bl	printf
	call	printf
	# adrp	x0, min_check
	lui	x10, %hi(min_check)
	# add	x0, x0, :lo12:min_check
	add	x10, x10, %lo(min_check)
	# ldr	x1, [x0]
	ld	x11, 0(x10)
	# adrp	x0, .LC6
	lui	x10, %hi(.LC6)
	# add	x0, x0, :lo12:.LC6
	add	x10, x10, %lo(.LC6)
	# bl	printf
	call	printf
	# adrp	x0, max_check
	lui	x10, %hi(max_check)
	# add	x0, x0, :lo12:max_check
	add	x10, x10, %lo(max_check)
	# ldr	x1, [x0]
	ld	x11, 0(x10)
	# adrp	x0, .LC7
	lui	x10, %hi(.LC7)
	# add	x0, x0, :lo12:.LC7
	add	x10, x10, %lo(.LC7)
	# bl	printf
	call	printf
	# adrp	x0, unsigned_min_check
	lui	x10, %hi(unsigned_min_check)
	# add	x0, x0, :lo12:unsigned_min_check
	add	x10, x10, %lo(unsigned_min_check)
	# ldr	x1, [x0]
	ld	x11, 0(x10)
	# adrp	x0, .LC8
	lui	x10, %hi(.LC8)
	# add	x0, x0, :lo12:.LC8
	add	x10, x10, %lo(.LC8)
	# bl	printf
	call	printf
	# adrp	x0, unsigned_max_check
	lui	x10, %hi(unsigned_max_check)
	# add	x0, x0, :lo12:unsigned_max_check
	add	x10, x10, %lo(unsigned_max_check)
	# ldr	x1, [x0]
	ld	x11, 0(x10)
	# adrp	x0, .LC9
	lui	x10, %hi(.LC9)
	# add	x0, x0, :lo12:.LC9
	add	x10, x10, %lo(.LC9)
	# bl	printf
	call	printf
	# mov	w0, 0
	li	x10, 0
	# adrp	x1, :got:__stack_chk_guard
	lui	x11, %hi(__stack_chk_guard)
	# ldr	x1, [x1, #:got_lo12:__stack_chk_guard]
	add	x11, x11, %lo(__stack_chk_guard) # load from GOT -> ADD!
	# ldr	x2, [x29, 8040]
	li	x26, 8040 # synthesis of oversized immediate
	add	x26, x26, x8 # converting offset register to add
	ld	x12, 0(x26)
	# ldr	x1, [x1]
	ld	x11, 0(x11)
	# eor	x1, x2, x1
	xor	x11, x12, x11
	# cmp	x1, 0
	addi	x25, x11, 0
	# beq	.L11
	beq	x25, x0, .L11
	# bl	__stack_chk_fail
	call	__stack_chk_fail
.L11:
	# ldp	x29, x30, [sp]
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	# mov	x16, 8048
	li	x27, 8048
	# add	sp, sp, x16
	add	sp, sp, x27
	# ret
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
