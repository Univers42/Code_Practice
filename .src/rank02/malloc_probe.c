/*
** LD_PRELOAD shim: logs every malloc() size request to the file named by
** MALLOC_PROBE_LOG, one size per line, then forwards to the real malloc.
** Used only to check for disproportionate allocations (e.g. malloc(1000000)
** for a 3-byte word) — never linked into the binary that actually runs
** the graded comparison, and never combined with -fsanitize=address (ASan
** installs its own allocator and conflicts with LD_PRELOAD malloc hooks).
**
** Uses raw open()/write()/close() rather than fopen()/fprintf(): stdio
** allocates its own buffer via malloc() on first use, which would recurse
** straight back into this hook and blow the stack.
*/
#define _GNU_SOURCE
#include <dlfcn.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

static void	*(*real_malloc)(size_t);
static int	in_hook;

static void	log_size(size_t size)
{
	char			*path;
	int				fd;
	char			buf[32];
	int				len;
	int				t;
	char			digits[32];
	unsigned long	n;

	path = getenv("MALLOC_PROBE_LOG");
	if (!path)
		return ;
	fd = open(path, O_WRONLY | O_CREAT | O_APPEND, 0644);
	if (fd < 0)
		return ;
	n = (unsigned long)size;
	t = 0;
	if (n == 0)
		digits[t++] = '0';
	while (n > 0)
	{
		digits[t++] = '0' + n % 10;
		n /= 10;
	}
	len = 0;
	while (t > 0)
		buf[len++] = digits[--t];
	buf[len++] = '\n';
	write(fd, buf, len);
	close(fd);
}

void	*malloc(size_t size)
{
	void	*ptr;

	if (!real_malloc)
		real_malloc = dlsym(RTLD_NEXT, "malloc");
	ptr = real_malloc(size);
	if (!in_hook)
	{
		in_hook = 1;
		log_size(size);
		in_hook = 0;
	}
	return (ptr);
}
