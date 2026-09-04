/*
** flood_fill  —  DRIVER
** prototype : void flood_fill(char **tab, t_point size, t_point begin);
** parse: av[1] = begin.x, av[2] = begin.y, av[3..] = grid rows
** size = { (int)strlen(av[3]), ac - 3 }; build char **tab (writable copies)
** call flood_fill, then print every row + '\n'
*/

#include "super.h"
#include "flood_fill.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

static char	**build_grid(char **argv, t_point size)
{
	char	**tab;
	int		i;

	tab = malloc(sizeof(char *) * size.y);
	i = 0;
	while (i < size.y)
	{
		tab[i] = malloc(size.x + 1);
		memcpy(tab[i], argv[3 + i], size.x + 1);
		i++;
	}
	return (tab);
}

static void	free_grid(char **tab, t_point size)
{
	int	i;

	i = 0;
	while (i < size.y)
		free(tab[i++]);
	free(tab);
}

static void	print_grid(char **tab, t_point size)
{
	int	i;

	i = 0;
	while (i < size.y)
	{
		write(1, tab[i], size.x);
		write(1, "\n", 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	t_point	size;
	t_point	begin;
	char	**tab;

	if (argc < 4)
		return (1);
	size.x = (int)strlen(argv[3]);
	size.y = argc - 3;
	begin.x = atoi(argv[1]);
	begin.y = atoi(argv[2]);
	tab = build_grid(argv, size);
	flood_fill(tab, size, begin);
	print_grid(tab, size);
	free_grid(tab, size);
	return (0);
}
