/*
** union  —  PROGRAM
** argc == 3  ->  av[1], av[2] = char *
** otherwise print '\n'
*/

#include <unistd.h>

static int	already_seen(char *buf, int n, char c)
{
	int	i;

	i = 0;
	while (i < n)
	{
		if (buf[i] == c)
			return (1);
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	char	seen_chars[512];
	int		n;
	int		i;

	if (argc == 3)
	{
		n = 0;
		i = 0;
		while (argv[1][i])
		{
			if (!already_seen(seen_chars, n, argv[1][i]))
				seen_chars[n++] = argv[1][i];
			i++;
		}
		i = 0;
		while (argv[2][i])
		{
			if (!already_seen(seen_chars, n, argv[2][i]))
				seen_chars[n++] = argv[2][i];
			i++;
		}
		write(1, seen_chars, n);
	}
	write(1, "\n", 1);
	return (0);
}
