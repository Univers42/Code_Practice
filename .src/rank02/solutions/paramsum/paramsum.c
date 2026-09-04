/*
** paramsum  —  PROGRAM
** any number of args
** print (argc - 1) + '\n'
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

int	main(int argc, char **argv)
{
	(void)argv;
	print_int(argc - 1);
	write(1, "\n", 1);
	return (0);
}
