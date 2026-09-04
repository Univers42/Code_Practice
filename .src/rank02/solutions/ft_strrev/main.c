/*
** ft_strrev  —  DRIVER
** prototype : char *ft_strrev(char *str);
** parse 1 arg  ->  av[1] = char * (copy it, it is modified in place)
** print the reversed string, then whether the return value is the
** same buffer we passed in (the subject requires "must return its
** parameter" — a cheat could return a new, correctly-reversed copy
** instead of mutating in place, and the content alone wouldn't show it)
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	char	*copy;
	char	*ret;
	size_t	i;

	if (argc != 2)
		return (1);
	copy = malloc(strlen(argv[1]) + 1);
	if (!copy)
		return (1);
	i = 0;
	while (argv[1][i])
	{
		copy[i] = argv[1][i];
		i++;
	}
	copy[i] = '\0';
	ret = ft_strrev(copy);
	printf("%s\n", copy);
	printf("%d\n", ret == copy);
	free(copy);
	return (0);
}
