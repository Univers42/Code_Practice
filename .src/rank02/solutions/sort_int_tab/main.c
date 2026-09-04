/*
** sort_int_tab  —  DRIVER
** prototype : void sort_int_tab(int *tab, unsigned int size);
** parse 1 arg  ->  av[1] = space-separated ints
** build the array, call sort_int_tab(tab, size), print the sorted ints, one per line
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

static unsigned int	count_ints(char *str)
{
	unsigned int	i;
	unsigned int	count;

	i = 0;
	count = 0;
	while (str[i])
	{
		while (str[i] == ' ')
			i++;
		if (!str[i])
			break ;
		if (str[i] == '-')
			i++;
		if (str[i] >= '0' && str[i] <= '9')
			count++;
		while (str[i] >= '0' && str[i] <= '9')
			i++;
	}
	return (count);
}

static int	*parse_ints(char *str, unsigned int *out_len)
{
	int				*tab;
	unsigned int	i;
	unsigned int	w;
	int				n;
	int				neg;

	*out_len = count_ints(str);
	tab = malloc(sizeof(int) * (*out_len == 0 ? 1 : *out_len));
	i = 0;
	w = 0;
	while (w < *out_len)
	{
		while (str[i] == ' ')
			i++;
		neg = (str[i] == '-');
		if (neg)
			i++;
		n = 0;
		while (str[i] >= '0' && str[i] <= '9')
			n = n * 10 + (str[i++] - '0');
		tab[w++] = neg ? -n : n;
	}
	return (tab);
}

int	main(int argc, char **argv)
{
	int				*tab;
	unsigned int	size;
	unsigned int	i;

	if (argc != 2)
		return (1);
	tab = parse_ints(argv[1], &size);
	sort_int_tab(tab, size);
	i = 0;
	while (i < size)
	{
		printf("%d\n", tab[i]);
		i++;
	}
	free(tab);
	return (0);
}
