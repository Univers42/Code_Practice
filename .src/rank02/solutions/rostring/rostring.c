/*
** rostring  —  PROGRAM
** argc >= 2  ->  av[1] = char *
** argc < 2  ->  print '\n'
*/

#include <unistd.h>

static int	skip_sep(char *s, int i)
{
	while (s[i] == ' ' || s[i] == '\t')
		i++;
	return (i);
}

static int	word_len(char *s, int i)
{
	int	len;

	len = 0;
	while (s[i + len] && s[i + len] != ' ' && s[i + len] != '\t')
		len++;
	return (len);
}

static int	print_words_single_spaced(char *s, int i)
{
	int	len;
	int	first;

	first = 1;
	i = skip_sep(s, i);
	while (s[i])
	{
		if (!first)
			write(1, " ", 1);
		first = 0;
		len = word_len(s, i);
		write(1, s + i, len);
		i = skip_sep(s, i + len);
	}
	return (!first);
}

int	main(int argc, char **argv)
{
	int	i;
	int	len;

	if (argc >= 2)
	{
		i = skip_sep(argv[1], 0);
		len = word_len(argv[1], i);
		if (len > 0)
		{
			if (print_words_single_spaced(argv[1], i + len))
				write(1, " ", 1);
			write(1, argv[1] + i, len);
		}
	}
	write(1, "\n", 1);
	return (0);
}
