/*
** ft_atoi_base  —  DRIVER
** prototype : int ft_atoi_base(const char *str, int str_base);
** parse 2 args  ->  av[1] = str, av[2] = base (atoi)
** print the returned int + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	if (argc != 3)
		return (1);
	printf("%d\n", ft_atoi_base(argv[1], atoi(argv[2])));
	return (0);
}
