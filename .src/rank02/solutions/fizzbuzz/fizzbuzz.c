/*
** fizzbuzz  —  PROGRAM
** no arguments, ignore argv
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

int	main(void)
{
	int	i;

	i = 1;
	while (i <= 100)
	{
		if (i % 3 == 0)
			write(1, "fizz", 4);
		if (i % 5 == 0)
			write(1, "buzz", 4);
		if (i % 3 != 0 && i % 5 != 0)
			print_int(i);
		write(1, "\n", 1);
		i++;
	}
	return (0);
}
