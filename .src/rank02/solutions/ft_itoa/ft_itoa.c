/*
** ft_itoa  —  reference implementation
** char *ft_itoa(int nbr);
*/

#include <stdlib.h>

static int	digit_count(long n)
{
	int	count;

	count = 1;
	while (n > 9 || n < -9)
	{
		n /= 10;
		count++;
	}
	return (count);
}

char	*ft_itoa(int nbr)
{
	long	n;
	int		neg;
	int		len;
	char	*str;
	int		i;

	n = nbr;
	neg = (n < 0);
	len = digit_count(n) + neg;
	str = malloc(len + 1);
	if (!str)
		return (NULL);
	str[len] = '\0';
	i = len - 1;
	if (neg)
		n = -n;
	while (n > 9)
	{
		str[i--] = '0' + (n % 10);
		n /= 10;
	}
	str[i] = '0' + n;
	if (neg)
		str[0] = '-';
	return (str);
}
