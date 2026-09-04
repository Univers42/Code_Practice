/*
** add_prime_sum  —  PROGRAM
** argc == 2  ->  av[1] = positive int
** otherwise print 0 + '\n'
*/

#include <unistd.h>

static int	is_positive_number(char *s)
{
	int	i;

	if (!s[0])
		return (0);
	i = 0;
	while (s[i])
	{
		if (s[i] < '0' || s[i] > '9')
			return (0);
		i++;
	}
	return (s[0] != '0' || s[1] != '\0');
}

static long	to_long(char *s)
{
	long	n;
	int		i;

	n = 0;
	i = 0;
	while (s[i])
		n = n * 10 + (s[i++] - '0');
	return (n);
}

static int	is_prime(long n)
{
	long	d;

	if (n < 2)
		return (0);
	d = 2;
	while (d * d <= n)
	{
		if (n % d == 0)
			return (0);
		d++;
	}
	return (1);
}

static void	print_long(long n)
{
	char	c;

	if (n >= 10)
		print_long(n / 10);
	c = '0' + (n % 10);
	write(1, &c, 1);
}

int	main(int argc, char **argv)
{
	long	limit;
	long	sum;
	long	n;

	if (argc == 2 && is_positive_number(argv[1]))
	{
		limit = to_long(argv[1]);
		sum = 0;
		n = 2;
		while (n <= limit)
		{
			if (is_prime(n))
				sum += n;
			n++;
		}
		print_long(sum);
	}
	else
		write(1, "0", 1);
	write(1, "\n", 1);
	return (0);
}
