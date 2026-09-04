#ifndef LIST_H
# define LIST_H

/*
** sort_list works on integer data (cmp is int (*)(int, int)), so this t_list
** carries an int, unlike the ft_list_* family whose data is a void *.
*/
typedef struct s_list
{
	struct s_list	*next;
	int				data;
}	t_list;

t_list	*sort_list(t_list *lst, int (*cmp)(int, int));

#endif
