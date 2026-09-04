#include <unistd.h>
int helper(int x);
int main(int argc, char **argv)
{
	(void)argc; (void)argv;
	if (helper(3) == 6)
		write(1, "\n", 1);
	else
		write(1, "\n", 1);
	return 0;
}
