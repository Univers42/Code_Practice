/*
** ft_strcpy  —  DRIVER
** prototype : char *ft_strcpy(char *s1, char *s2);
** parse 1 arg  ->  av[1] = char * (source)
** alloc a dst buffer SEEDED with junk (not the source!), call
** ft_strcpy(dst, av[1]), then print dst ITSELF (not the return value:
** a cheat can `return s2` untouched and still "look" right on stdout)
** and whether the return value actually is dst, as strcpy must.
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	size_t	len;
	char	*dst;
	char	*ret;

	if (argc != 2)
		return (1);
	len = strlen(argv[1]);
	dst = malloc(len + 1);
	if (!dst)
		return (1);
	memset(dst, 'X', len);
	dst[len] = '\0';
	ret = ft_strcpy(dst, argv[1]);
	printf("%s\n", dst);
	printf("%d\n", ret == dst);
	free(dst);
	return (0);
}
