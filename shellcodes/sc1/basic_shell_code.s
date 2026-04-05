.intel_syntax noprefix
.global _start

_start:
	xor rax, rax
	mov al, 2

	xor rsi, rsi
	push rsi

	/bin/sh/
	mov rbx, 0x68732f2f6e69622f
	push rbx
	mov rdi, wrsp


	xor rdx, rdx

	syscall
