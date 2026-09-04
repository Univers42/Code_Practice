#include <string.h>

size_t	ft_strcspn(const char *s, const char *reject)
{
	return (strcspn(s, reject));
}
