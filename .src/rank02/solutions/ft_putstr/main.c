/*
** ft_putstr  —  DRIVER
** prototype : void ft_putstr(char *str);
** parse 1 arg  ->  av[1] = char *
** call ft_putstr(av[1]); the function itself prints
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int	main(int argc, char **argv)
{
	if(argc != 2)
		return (1);
	ft_putstr(argv[1]);
	write(1, "\n", 1);
	return (0);
}
