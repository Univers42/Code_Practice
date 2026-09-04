/*
** first_word  —  PROGRAM
** argc == 2  ->  av[1] = char * (the string)
** otherwise print just '\n'
*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	int	i;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i] == ' ' || argv[1][i] == '\t')
			i++;
		while (argv[1][i] && argv[1][i] != ' ' && argv[1][i] != '\t')
			write(1, &argv[1][i++], 1);
	}
	write(1, "\n", 1);
	return (0);
}
