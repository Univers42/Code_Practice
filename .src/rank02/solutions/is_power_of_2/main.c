/*
** is_power_of_2  —  DRIVER
** prototype : int is_power_of_2(unsigned int n);
** parse 1 arg  ->  av[1] = unsigned int (strtoul)
** print the returned 0 / 1 + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	unsigned int	n;

	if (argc != 2)
		return (1);
	n = strtoul(argv[1], NULL, 10);
	printf("%d\n", is_power_of_2(n));
	return (0);
}
