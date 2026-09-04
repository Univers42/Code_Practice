/*
** pgcd  —  PROGRAM
** argc == 3  ->  av[1], av[2] = strictly positive int
** otherwise print '\n'
*/

#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	int	a;
	int	b;
	int	tmp;

	if (argc == 3)
	{
		a = atoi(argv[1]);
		b = atoi(argv[2]);
		while (b != 0)
		{
			tmp = b;
			b = a % b;
			a = tmp;
		}
		printf("%d\n", a);
	}
	else
		printf("\n");
	return (0);
}
