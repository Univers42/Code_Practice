#include <unistd.h>

void	print_bits(unsigned char octet)
{
	int	i;

	i = 7;
	while (i >= 0)
	{
		write(1, ((octet >> i) & 1) ? "1" : "0", 1);
		i--;
	}
}
