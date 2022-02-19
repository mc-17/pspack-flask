// BSD syscalls
const SYSCALL_CLOSE 		= 6;
const SYSCALL_GETPID 		= 20;
const SYSCALL_SETUID 		= 23;
const SYSCALL_MUNMAP 		= 73;
const SYSCALL_MPROTECT 		= 74;
const SYSCALL_SOCKET 		= 97;
const SYSCALL_MLOCK 		= 203;
const SYSCALL_MUNLOCKALL 	= 325;
const SYSCALL_KQUEUE 		= 362;
const SYSCALL_KEVENT 		= 363;
const SYSCALL_MMAP 			= 477;

// PS4 syscalls
const SYSCALL_sys_dynlib_load_prx 		= 594;
const SYSCALL_sys_randomized_path 		= 602;
const SYSCALL_sys_dynlib_get_info_ex 	= 608;