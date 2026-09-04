/*
** fizzbuzz  —  PROGRAM
** no arguments, ignore argv
*/

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int	main(void)
{
	int i = 1;
	while (i <= 100)
	{
		if (i % 3 == 0)
			printf("fizz");
		if (i % 5 == 0)
			printf("buzz");
		if (i % 3 != 0 && i % 5 != 0)
			printf("%i", i);
		printf("\n");
		i++;
	}
	return (0);
}
