#include <unistd.h>

void ft_putstr(char *str);
{
    int i;
    while(str[i])
        write(1, &str[i++]);
}
