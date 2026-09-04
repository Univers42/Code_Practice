/*
** ft_swap  —  DRIVER
** prototype : void ft_swap(int *a, int *b);
** parse 2 args  ->  av[1], av[2] = int (atoi)
** call ft_swap(&a, &b), print "a b" + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	int	a;
	int	b;

	if (argc != 3)
		return (1);
	a = atoi(argv[1]);
	b = atoi(argv[2]);
	ft_swap(&a, &b);
	printf("%d %d\n", a, b);
	return (0);
}
