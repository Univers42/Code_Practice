/*
** ft_atoi_base  —  reference implementation
** int ft_atoi_base(const char *str, int str_base);
*/

static int	digit_value(char c)
{
	if (c >= '0' && c <= '9')
		return (c - '0');
	if (c >= 'a' && c <= 'f')
		return (c - 'a' + 10);
	if (c >= 'A' && c <= 'F')
		return (c - 'A' + 10);
	return (-1);
}

int	ft_atoi_base(const char *str, int str_base)
{
	int	i;
	int	sign;
	int	result;
	int	digit;

	i = 0;
	sign = 1;
	if (str[0] == '-')
	{
		sign = -1;
		i++;
	}
	result = 0;
	digit = digit_value(str[i]);
	while (digit >= 0 && digit < str_base)
	{
		result = result * str_base + digit;
		i++;
		digit = digit_value(str[i]);
	}
	return (result * sign);
}
