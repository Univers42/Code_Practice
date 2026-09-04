static unsigned int	pgcd_of(unsigned int a, unsigned int b)
{
	unsigned int	tmp;

	while (b != 0)
	{
		tmp = b;
		b = a % b;
		a = tmp;
	}
	return (a);
}

unsigned int	lcm(unsigned int a, unsigned int b)
{
	unsigned int	g;

	if (a == 0 || b == 0)
		return (0);
	g = pgcd_of(a, b);
	return ((a / g) * b);
}
