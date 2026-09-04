/*
** ft_strpbrk  —  DRIVER
** prototype : char *ft_strpbrk(const char *s1, const char *s2);
** parse 2 args  ->  av[1] = s1, av[2] = s2
** print the returned substring, or "(null)", + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	char	*sub;

	if (argc != 3)
		return (1);
	sub = ft_strpbrk(argv[1], argv[2]);
	if (sub)
		printf("%s\n", sub);
	else
		printf("(null)\n");
	return (0);
}
