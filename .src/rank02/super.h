#ifndef SUPER_H
# define SUPER_H

# include <stddef.h>

/*
** Shared prototypes for every rank02 FUNCTION exercise whose signature only
** uses plain C types. Each driver (solutions/<ex>/main.c) includes this file
** so it can call the exercise function; the reference implementation and the
** student's turn-in provide the definition at link time.
**
** The exercises that need a custom struct (t_list, t_point) are NOT here:
** their prototype lives in a dedicated header next to the exercise
** (solutions/<ex>/ft_list.h, list.h, flood_fill.h) because the "t_list" of
** sort_list (int data) and the "t_list" of the ft_list_* family (void *data)
** are different types with the same name.
*/

/* --- Level 1 --- */
void			ft_putstr(char *str);
char			*ft_strcpy(char *s1, char *s2);
int				ft_strlen(char *str);
void			ft_swap(int *a, int *b);

/* --- Level 2 --- */
int				ft_atoi(const char *str);
int				ft_strcmp(char *s1, char *s2);
size_t			ft_strcspn(const char *s, const char *reject);
char			*ft_strdup(char *src);
char			*ft_strpbrk(const char *s1, const char *s2);
char			*ft_strrev(char *str);
size_t			ft_strspn(const char *s, const char *accept);
int				is_power_of_2(unsigned int n);
int				max(int *tab, unsigned int len);
void			print_bits(unsigned char octet);
unsigned char	reverse_bits(unsigned char octet);
unsigned char	swap_bits(unsigned char octet);

/* --- Level 3 --- */
int				ft_atoi_base(const char *str, int str_base);
int				*ft_range(int start, int end);
int				*ft_rrange(int start, int end);
unsigned int	lcm(unsigned int a, unsigned int b);

/* --- Level 4 --- */
char			*ft_itoa(int nbr);
char			**ft_split(char *str);
void			sort_int_tab(int *tab, unsigned int size);

#endif
