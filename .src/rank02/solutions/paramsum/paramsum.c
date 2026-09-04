/*
** paramsum  —  PROGRAM
** any number of args
** print (argc - 1) + '\n'
*/

#include <stdio.h>

int	main(int argc, char **argv)
{
	(void)argv;
	printf("%d\n", argc - 1);
	return (0);
}
