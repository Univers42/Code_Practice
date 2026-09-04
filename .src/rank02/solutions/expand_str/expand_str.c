/*
** expand_str  —  PROGRAM
** argc == 2  ->  av[1] = char *
** otherwise print '\n'
*/

#include <unistd.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	int	i;
	int	first;

	if (argc == 2)
	{
		i = 0;
		first = 1;
		while (argv[1][i])
		{
			while (argv[1][i] == ' ' || argv[1][i] == '\t')
				i++;
			if (argv[1][i])
			{
				if (!first)
					write(1, "   ", 3);
				first = 0;
				while (argv[1][i] && argv[1][i] != ' ' && argv[1][i] != '\t')
				{
					write(1, &argv[1][i], 1);
					i++;
				}
			}
		}
	}
	write(1, "\n", 1);
	return (0);
}
