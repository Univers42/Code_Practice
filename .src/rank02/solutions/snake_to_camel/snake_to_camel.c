/*
** snake_to_camel  —  PROGRAM
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
			if (c == '_')
			{
				i++;
				if (!argv[1][i])
					break ;
				c = argv[1][i];
				if (c >= 'a' && c <= 'z')
					c -= 32;
			}
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
