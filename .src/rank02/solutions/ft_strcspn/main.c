/*
** ft_strcspn  —  DRIVER
** prototype : size_t ft_strcspn(const char *s, const char *reject);
** parse 2 args  ->  av[1] = s, av[2] = reject
** print the returned size_t + '\n'
*/

#include "super.h"
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int	main(int argc, char **argv)
{
	if (argc != 3)
		return (1);
	printf("%zu\n", ft_strcspn(argv[1], argv[2]));
	return (0);
}
