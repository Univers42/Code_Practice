/*
** ft_list_remove_if  —  reference implementation
** void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)());
*/

#include "ft_list.h"
#include <stdlib.h>

void	ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)())
{
	t_list	*current;
	t_list	*prev;
	t_list	*next;

	current = *begin_list;
	prev = NULL;
	while (current)
	{
		next = current->next;
		if (cmp(current->data, data_ref) == 0)
		{
			if (prev)
				prev->next = next;
			else
				*begin_list = next;
			free(current->data);
			free(current);
		}
		else
			prev = current;
		current = next;
	}
}
