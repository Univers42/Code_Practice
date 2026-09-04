/*
** hidenp  —  PROGRAM
** argc == 3  ->  av[1], av[2] = char *
** otherwise print '\n'
*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;
	int	j;

	if (argc == 3)
	{
		i = 0;
		j = 0;
		while (argv[1][i] && argv[2][j])
		{
			if (argv[1][i] == argv[2][j])
				i++;
			j++;
		}
		if (argv[1][i] == '\0')
			write(1, "1\n", 2);
		else
			write(1, "0\n", 2);
		return (0);
	}
	write(1, "\n", 1);
	return (0);
}
