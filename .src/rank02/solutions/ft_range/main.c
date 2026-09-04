/*
** ft_range  —  DRIVER
** prototype : int *ft_range(int start, int end);
** parse 2 args  ->  av[1] = start, av[2] = end (atoi)
** print the abs(end-start)+1 returned values, one per line
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	int	start;
	int	end;
	int	*arr;
	int	len;
	int	i;

	if (argc != 3)
		return (1);
	start = atoi(argv[1]);
	end = atoi(argv[2]);
	arr = ft_range(start, end);
	if (!arr)
		return (1);
	len = (end >= start) ? (end - start + 1) : (start - end + 1);
	i = 0;
	while (i < len)
	{
		printf("%d\n", arr[i]);
		i++;
	}
	free(arr);
	return (0);
}
