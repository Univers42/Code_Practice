/*
** ft_atoi  —  DRIVER
** prototype : int ft_atoi(const char *str);
** parse 1 arg  ->  av[1] = char *
** print the returned int + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	if (argc != 2)
		return (1);
	printf("%i\n", ft_atoi(argv[1]));
	return (0);
}
