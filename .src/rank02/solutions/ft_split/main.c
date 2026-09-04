/*
** ft_split  —  DRIVER
** prototype : char **ft_split(char *str);
** parse 1 arg  ->  av[1] = char *
** call ft_split, print each word on its own line (NULL-terminated array)
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	char	**words;
	int		i;

	if (argc != 2)
		return (1);
	words = ft_split(argv[1]);
	if (!words)
		return (1);
	i = 0;
	while (words[i])
	{
		printf("%s\n", words[i]);
		free(words[i]);
		i++;
	}
	free(words);
	return (0);
}
