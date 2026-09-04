/*
** rstr_capitalizer  —  PROGRAM
** argc >= 2  ->  one line per arg
** argc == 1  ->  print '\n'
**
** Per the subject's own examples: only the LITERAL last character of a
** word gets capitalised, and only if it's a letter — e.g. "Okay," (word
** ends in ',') comes out "okay," (the 'y' stays lowercase), not "okaY,".
** If the last character isn't a letter, every letter in the word is just
** lowercased.
*/

#include <unistd.h>

static int	is_letter(char c)
{
	return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'));
}

static void	print_word(char *s, int start, int len)
{
	int		i;
	int		last;
	char	c;

	last = start + len - 1;
	i = start;
	while (i < start + len)
	{
		c = s[i];
		if (is_letter(c) && i == last)
			c = (c >= 'a' && c <= 'z') ? c - 32 : c;
		else if (is_letter(c))
			c = (c >= 'A' && c <= 'Z') ? c + 32 : c;
		write(1, &c, 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	int	a;
	int	i;
	int	start;

	if (argc == 1)
		write(1, "\n", 1);
	a = 1;
	while (a < argc)
	{
		i = 0;
		while (argv[a][i])
		{
			while (argv[a][i] == ' ' || argv[a][i] == '\t')
				write(1, &argv[a][i++], 1);
			start = i;
			while (argv[a][i] && argv[a][i] != ' ' && argv[a][i] != '\t')
				i++;
			if (i > start)
				print_word(argv[a], start, i - start);
		}
		write(1, "\n", 1);
		a++;
	}
	return (0);
}
