/*
** ft_strcmp  —  DRIVER
** prototype : int ft_strcmp(char *s1, char *s2);
** parse 2 args  ->  av[1], av[2] = char *
** print the SIGN of the return (-1 / 0 / 1) + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	if (argc != 3)
		return 1;
	printf("%i\n", ft_strcmp(argv[1], argv[2]));
	return (0);
}
