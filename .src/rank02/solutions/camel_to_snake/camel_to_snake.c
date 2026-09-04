/*
** camel_to_snake  —  PROGRAM
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
			if (c >= 'A' && c <= 'Z')
			{
				write(1, "_", 1);
				c = c + 32;
			}
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
