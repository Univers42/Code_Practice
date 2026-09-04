/*
** ft_itoa  —  DRIVER
** prototype : char *ft_itoa(int nbr);
** parse 1 arg  ->  av[1] = int (atoi)
** print the returned string + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	char	*s;

	if (argc != 2)
		return (1);
	s = ft_itoa(atoi(argv[1]));
	if (!s)
		return (1);
	printf("%s\n", s);
	free(s);
	return (0);
}
