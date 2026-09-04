/*
** print_hex  —  PROGRAM
** argc == 2  ->  av[1] = positive int in base 10
** otherwise print '\n'
*/

#include <unistd.h>

static void	print_hex_rec(unsigned int n)
{
	char	*digits;

	digits = "0123456789abcdef";
	if (n >= 16)
		print_hex_rec(n / 16);
	write(1, &digits[n % 16], 1);
}

static unsigned int	parse_uint(char *s)
{
	unsigned int	n;
	int				i;

	n = 0;
	i = 0;
	while (s[i] >= '0' && s[i] <= '9')
		n = n * 10 + (s[i++] - '0');
	return (n);
}

int	main(int argc, char **argv)
{
	if (argc == 2)
		print_hex_rec(parse_uint(argv[1]));
	write(1, "\n", 1);
	return (0);
}
