/*
** fprime  —  PROGRAM
** argc == 2  ->  av[1] = positive int
** otherwise print '\n'
*/

#include <stdio.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	long	n;
	long	d;
	int		printed;

	if (argc == 2)
	{
		n = atoi(argv[1]);
		printed = 0;
		d = 2;
		while (d * d <= n)
		{
			while (n % d == 0)
			{
				if (printed)
					printf("*");
				printf("%ld", d);
				printed = 1;
				n /= d;
			}
			d++;
		}
		if (n > 1 || !printed)
		{
			if (printed)
				printf("*");
			printf("%ld", n);
		}
	}
	printf("\n");
	return (0);
}
