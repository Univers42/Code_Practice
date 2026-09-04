#include "flood_fill.h"

void	flood_fill(char **tab, t_point size, t_point begin)
{
	char	target;
	t_point	next;

	if (begin.x < 0 || begin.x >= size.x || begin.y < 0 || begin.y >= size.y)
		return ;
	target = tab[begin.y][begin.x];
	if (target == 'F')
		return ;
	tab[begin.y][begin.x] = 'F';
	next = begin;
	next.x = begin.x + 1;
	if (next.x < size.x && tab[next.y][next.x] == target)
		flood_fill(tab, size, next);
	next.x = begin.x - 1;
	if (next.x >= 0 && tab[next.y][next.x] == target)
		flood_fill(tab, size, next);
	next.x = begin.x;
	next.y = begin.y + 1;
	if (next.y < size.y && tab[next.y][next.x] == target)
		flood_fill(tab, size, next);
	next.y = begin.y - 1;
	if (next.y >= 0 && tab[next.y][next.x] == target)
		flood_fill(tab, size, next);
}
