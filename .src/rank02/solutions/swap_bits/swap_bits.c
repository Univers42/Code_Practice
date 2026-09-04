unsigned char	swap_bits(unsigned char octet)
{
	return ((unsigned char)((octet << 4) | (octet >> 4)));
}
