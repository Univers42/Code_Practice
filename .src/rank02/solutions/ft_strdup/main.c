/*
** ft_strdup  —  DRIVER
** prototype : char *ft_strdup(char *src);
** parse 1 arg  ->  av[1] = char *
** print the duplicated string, then whether the pointer is actually new
** (a cheat can `return src` untouched and the content still "looks" right)
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	char	*dup;
	int		is_new;

	if (argc != 2)
		return (1);
	dup = ft_strdup(argv[1]);
	if (!dup)
		return (1);
	is_new = (dup != argv[1]);
	printf("%s\n", dup);
	printf("%d\n", is_new);
	if (is_new)
		free(dup);
	return (0);
}
