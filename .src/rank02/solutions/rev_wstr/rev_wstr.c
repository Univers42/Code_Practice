/*
** rev_wstr  —  PROGRAM
** argc == 2  ->  av[1] = char * (words separated by single spaces)
** otherwise print '\n'
*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	int	start;
	int	end;
	int	i;

	if (argc == 2)
	{
		end = 0;
		while (argv[1][end])
			end++;
		end--;
		while (end >= 0)
		{
			start = end;
			while (start >= 0 && argv[1][start] != ' ')
				start--;
			i = start + 1;
			while (i <= end)
				write(1, &argv[1][i++], 1);
			if (start >= 0)
				write(1, " ", 1);
			end = start - 1;
		}
	}
	write(1, "\n", 1);
	return (0);
}
