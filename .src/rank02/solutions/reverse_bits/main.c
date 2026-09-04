/*
** reverse_bits  —  DRIVER
** prototype : unsigned char reverse_bits(unsigned char octet);
** parse 1 arg  ->  av[1] = 0..255 (atoi)
** print the returned byte as an unsigned int + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	if (argc != 2)
		return (1);
	printf("%u\n", reverse_bits((unsigned char)atoi(argv[1])));
	return (0);
}
