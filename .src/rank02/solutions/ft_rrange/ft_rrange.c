/*
** ft_rrange  —  reference implementation
** int *ft_rrange(int start, int end);
**
** ft_rrange(start, end) is ft_range(end, start): same algorithm, start and
** end swapped before running it.
*/

#include <stdlib.h>

int	*ft_rrange(int start, int end)
{
	int	*arr;
	int	len;
	int	step;
	int	i;
	int	tmp;

	tmp = start;
	start = end;
	end = tmp;
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
