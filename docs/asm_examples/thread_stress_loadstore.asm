	.file	"thread_stress_loadstore.c"
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
	.global	non_atomic_counter
	.align	2
	.type	non_atomic_counter, %object
	.size	non_atomic_counter, 4
non_atomic_counter:
	.zero	4
	.global	current_thread_index
	.align	2
	.type	current_thread_index, %object
	.size	current_thread_index, 4
current_thread_index:
	.zero	4
	.global	thread_reader_lock
	.align	2
	.type	thread_reader_lock, %object
	.size	thread_reader_lock, 4
thread_reader_lock:
	.zero	4
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
	.global	acquire_lock
	.type	acquire_lock, %function
acquire_lock:
	# stp	x29, x30, [sp, -48]!
	sd	x8, -48(sp)
	sd	ra, -40(sp)
	addi	sp, sp, -48 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# str	w0, [x29, 28]
	sw	x10, 28(x8)
.L4:
	# adrp	x0, current_thread_index
	lui	x10, %hi(current_thread_index)
	# add	x0, x0, :lo12:current_thread_index
	add	x10, x10, %lo(current_thread_index)
	# ldar	w0, [x0]
	lw	x10, 0(x10)
	fence	iorw,iorw # making implicit fence semantics explicit
	# str	w0, [x29, 44]
	sw	x10, 44(x8)
	# ldr	w1, [x29, 44]
	lw	x11, 44(x8)
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# cmp	w1, w0
	sub	x25, x11, x10
	# beq	.L6
	beq	x25, x0, .L6
	# adrp	x0, ts
	lui	x10, %hi(ts)
	# add	x0, x0, :lo12:ts
	add	x10, x10, %lo(ts)
	# mov	x1, 0
	li	x11, 0
	# bl	nanosleep
	call	nanosleep
	# b	.L4
	j	.L4
.L6:
	# nop
	nop
	# nop
	nop
	# ldp	x29, x30, [sp], 48
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 48 # writeback
	# ret
	ret
	.size	acquire_lock, .-acquire_lock
	.align	2
	.global	release_lock
	.type	release_lock, %function
release_lock:
	# sub	sp, sp, #16
	addi	sp, sp, -16
	# str	w0, [sp, 12]
	sw	x10, 12(sp)
	# ldr	w1, [sp, 12]
	lw	x11, 12(sp)
	# adrp	x0, current_thread_index
	lui	x10, %hi(current_thread_index)
	# add	x0, x0, :lo12:current_thread_index
	add	x10, x10, %lo(current_thread_index)
	# stlr	w1, [x0]
	fence	iorw,iorw  # making implicit fence semantics explicit
	sw	x11, 0(x10)
	# nop
	nop
	# add	sp, sp, 16
	addi	sp, sp, 16
	# ret
	ret
	.size	release_lock, .-release_lock
	.section	.rodata
	.align	3
.LC0:
	.string	"Thread %d\n"
	.text
	.align	2
	.global	mythread
	.type	mythread, %function
mythread:
	# stp	x29, x30, [sp, -48]!
	sd	x8, -48(sp)
	sd	ra, -40(sp)
	addi	sp, sp, -48 # writeback
	# add	x29, sp, 0
	addi	x8, sp, 0
	# str	x0, [x29, 24]
	sd	x10, 24(x8)
	# ldr	x0, [x29, 24]
	ld	x10, 24(x8)
	# ldr	w0, [x0]
	lw	x10, 0(x10)
	# str	w0, [x29, 40]
	sw	x10, 40(x8)
	# ldr	w0, [x29, 40]
	lw	x10, 40(x8)
	# str	w0, [x29, 44]
	sw	x10, 44(x8)
	# ldr	w0, [x29, 40]
	lw	x10, 40(x8)
	# bl	acquire_lock
	call	acquire_lock
	# adrp	x0, .LC0
	lui	x10, %hi(.LC0)
	# add	x0, x0, :lo12:.LC0
	add	x10, x10, %lo(.LC0)
	# ldr	w1, [x29, 40]
	lw	x11, 40(x8)
	# bl	printf
	call	printf
	# str	wzr, [x29, 36]
	sw	x0, 36(x8)
	# b	.L9
	j	.L9
.L10:
	# adrp	x0, non_atomic_counter
	lui	x10, %hi(non_atomic_counter)
	# add	x0, x0, :lo12:non_atomic_counter
	add	x10, x10, %lo(non_atomic_counter)
	# ldr	w0, [x0]
	lw	x10, 0(x10)
	# add	w1, w0, 1
	addiw	x11, x10, 1
	# adrp	x0, non_atomic_counter
	lui	x10, %hi(non_atomic_counter)
	# add	x0, x0, :lo12:non_atomic_counter
	add	x10, x10, %lo(non_atomic_counter)
	# str	w1, [x0]
	sw	x11, 0(x10)
	# adrp	x0, atomic_counter
	lui	x10, %hi(atomic_counter)
	# add	x0, x0, :lo12:atomic_counter
	add	x10, x10, %lo(atomic_counter)
	# mov	w1, 1
	li	x11, 1
	# ldaddal	w1, w1, [x0]
	amoadd.w.aqrl	x11, x11, (x10)
	# ldr	w0, [x29, 36]
	lw	x10, 36(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# str	w0, [x29, 36]
	sw	x10, 36(x8)
.L9:
	# ldr	w0, [x29, 36]
	lw	x10, 36(x8)
	# cmp	w0, 999
	addi	x25, x10, -999
	# ble	.L10
	ble	x25, x0, .L10
	# ldr	w0, [x29, 40]
	lw	x10, 40(x8)
	# add	w0, w0, 1
	addiw	x10, x10, 1
	# bl	release_lock
	call	release_lock
	# mov	x0, 0
	li	x10, 0
	# ldp	x29, x30, [sp], 48
	ld	x8, 0(sp)
	ld	ra, 8(sp)
	addi	sp, sp, 48 # writeback
	# ret
	ret
	.size	mythread, .-mythread
	.section	.rodata
	.align	3
.LC1:
	.string	"atomic     %d\n"
	.align	3
.LC2:
	.string	"non-atomic %d\n"
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
	# b	.L13
	j	.L13
.L14:
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
.L13:
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# cmp	w0, 999
	addi	x25, x10, -999
	# ble	.L14
	ble	x25, x0, .L14
	# str	wzr, [x29, 28]
	sw	x0, 28(x8)
	# b	.L15
	j	.L15
.L16:
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
.L15:
	# ldr	w0, [x29, 28]
	lw	x10, 28(x8)
	# cmp	w0, 999
	addi	x25, x10, -999
	# ble	.L16
	ble	x25, x0, .L16
	# adrp	x0, atomic_counter
	lui	x10, %hi(atomic_counter)
	# add	x0, x0, :lo12:atomic_counter
	add	x10, x10, %lo(atomic_counter)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC1
	lui	x10, %hi(.LC1)
	# add	x0, x0, :lo12:.LC1
	add	x10, x10, %lo(.LC1)
	# bl	printf
	call	printf
	# adrp	x0, non_atomic_counter
	lui	x10, %hi(non_atomic_counter)
	# add	x0, x0, :lo12:non_atomic_counter
	add	x10, x10, %lo(non_atomic_counter)
	# ldr	w1, [x0]
	lw	x11, 0(x10)
	# adrp	x0, .LC2
	lui	x10, %hi(.LC2)
	# add	x0, x0, :lo12:.LC2
	add	x10, x10, %lo(.LC2)
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
	# beq	.L18
	beq	x25, x0, .L18
	# bl	__stack_chk_fail
	call	__stack_chk_fail
.L18:
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
