/*
** repeat_alpha  —  PROGRAM
** argc == 2  ->  av[1] = char *
** otherwise print '\n'
*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	int		i;
	int		j;
	int		count;
	char	c;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i])
		{
			c = argv[1][i];
			if (c >= 'a' && c <= 'z')
				count = c - 'a' + 1;
			else if (c >= 'A' && c <= 'Z')
				count = c - 'A' + 1;
			else
				count = 1;
			j = 0;
			while (j < count)
			{
				write(1, &c, 1);
				j++;
			}
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
