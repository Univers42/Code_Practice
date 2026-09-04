/*
** print_bits  —  DRIVER
** prototype : void print_bits(unsigned char octet);
** parse 1 arg  ->  av[1] = 0..255 (atoi)
** call print_bits; it prints 8 chars with NO newline -> add '\n' after
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	if (argc != 2)
		return (1);
	print_bits((unsigned char)atoi(argv[1]));
	write(1, "\n", 1);
	return (0);
}
