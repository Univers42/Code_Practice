/*
** tab_mult  —  PROGRAM
** argc == 2  ->  av[1] = strictly positive int
** otherwise print '\n'
*/

#include <unistd.h>

static void	print_int(int n)
{
	char	c;

	if (n >= 10)
		print_int(n / 10);
	c = '0' + n % 10;
	write(1, &c, 1);
}

static int	parse_int(char *s)
{
	int	n;
	int	i;

	n = 0;
	i = 0;
	while (s[i] >= '0' && s[i] <= '9')
		n = n * 10 + (s[i++] - '0');
	return (n);
}

int	main(int argc, char **argv)
{
	int	n;
	int	i;

	if (argc == 2)
	{
		n = parse_int(argv[1]);
		i = 1;
		while (i <= 9)
		{
			print_int(i);
			write(1, " x ", 3);
			print_int(n);
			write(1, " = ", 3);
			print_int(i * n);
			write(1, "\n", 1);
			i++;
		}
	}
	else
		write(1, "\n", 1);
	return (0);
}
