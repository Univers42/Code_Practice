/*
** do_op  —  PROGRAM
** argc == 4  ->  av[1] = int, av[2] = op (+ - * / %), av[3] = int
** otherwise print '\n'
*/

#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	if (argc == 4)
	{
		int n1 = atoi(argv[1]);
		int n2 = atoi(argv[3]);
		if ((argv[2][0] == '/' || argv[2][0] == '%') && n2 == 0)
			return(printf("\n"));
		if (argv[2][0] == '+')
			printf("%i", n1 + n2);
		else if (argv[2][0] == '-')
			printf("%i", n1 - n2);
		else if (argv[2][0] == '*')
			printf("%i", n1 * n2);
		else if (argv[2][0] == '/')
			printf("%i", n1 / n2);
		else if (argv[2][0] == '%')
			printf("%i", n1 % n2);
	}
	printf("\n");
	return (0);
}
