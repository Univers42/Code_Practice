/*
** ft_range  —  reference implementation
** int *ft_range(int start, int end);
*/

#include <stdlib.h>

int	*ft_range(int start, int end)
{
	int	*arr;
	int	len;
	int	step;
	int	i;

	len = (end >= start) ? (end - start + 1) : (start - end + 1);
	step = (end >= start) ? 1 : -1;
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (NULL);
	i = 0;
	while (i < len)
	{
		arr[i] = start + i * step;
		i++;
	}
	return (arr);
}
