/*
** lcm  —  DRIVER
** prototype : unsigned int lcm(unsigned int a, unsigned int b);
** parse 2 args  ->  av[1], av[2] = unsigned int (strtoul)
** print the returned unsigned int + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	unsigned int	a;
	unsigned int	b;

	if (argc != 3)
		return (1);
	a = strtoul(argv[1], NULL, 10);
	b = strtoul(argv[2], NULL, 10);
	printf("%u\n", lcm(a, b));
	return (0);
}
