/*
** alpha_mirror  —  PROGRAM
** argc == 2  ->  av[1] = char *
** otherwise print '\n'
*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		i;
	char	c;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i])
		{
			c = argv[1][i];
			if (c >= 'a' && c <= 'z')
				c = 'a' + 'z' - c;
			else if (c >= 'A' && c <= 'Z')
				c = 'A' + 'Z' - c;
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
