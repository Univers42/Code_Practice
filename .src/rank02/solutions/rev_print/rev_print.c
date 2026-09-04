/*
** rev_print  —  PROGRAM
** argc == 2  ->  av[1] = char *
** otherwise print '\n'
*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i])
			i++;
		i--;
		while (i >= 0)
			write(1, &argv[1][i--], 1);
	}
	write(1, "\n", 1);
	return (0);
}
