#include <stdlib.h>
#include <string.h>

char	*ft_strdup(char *src)
{
	int		i;
	char	*copy;

	if (!src)
		return (NULL);
	copy = malloc(sizeof(char) * (strlen(src) + 1));
	if (!copy)
		return (NULL);
	i = 0;
	while (src[i])
	{
		copy[i] = src[i];
		i++;
	}
	copy[i] = '\0';
	return (copy);
}
