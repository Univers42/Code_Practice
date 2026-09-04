/*
** search_and_replace  —  PROGRAM
** argc == 4  ->  av[1] = str, av[2] = char, av[3] = char
** av[2] / av[3] must be a single letter, otherwise print '\n'
**
** the subject's own example (search_and_replace "zaz" "art" "zul" -> just
** "\n") shows av[2]/av[3] must be exactly one character long, even though
** the prose never states it explicitly.
*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		i;
	char	c;

	if (argc == 4 && argv[2][0] && !argv[2][1] && argv[3][0] && !argv[3][1])
	{
		i = 0;
		while (argv[1][i])
		{
			c = argv[1][i];
			if (c == argv[2][0])
				c = argv[3][0];
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
