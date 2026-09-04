/*
** ft_list_foreach  —  DRIVER
** prototype : void ft_list_foreach(t_list *begin_list, void (*f)(void *));
** parse 1 arg  ->  av[1] = space-separated ints
** build a t_list (data = int *); f prints *(int *)data + '\n'
** call ft_list_foreach(list, f)
*/

#include "super.h"
#include "ft_list.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

static t_list	*new_node(int value)
{
	t_list	*node;
	int		*data;

	node = malloc(sizeof(t_list));
	data = malloc(sizeof(int));
	*data = value;
	node->data = data;
	node->next = NULL;
	return (node);
}

static void	list_add_back(t_list **head, t_list **tail, t_list *node)
{
	if (*head == NULL)
		*head = node;
	else
		(*tail)->next = node;
	*tail = node;
}

static t_list	*build_list(char *str)
{
	t_list	*head;
	t_list	*tail;
	int		i;
	int		n;
	int		neg;

	head = NULL;
	tail = NULL;
	i = 0;
	while (str[i])
	{
		while (str[i] == ' ')
			i++;
		if (!str[i])
			break ;
		neg = (str[i] == '-');
		if (neg)
			i++;
		n = 0;
		while (str[i] >= '0' && str[i] <= '9')
			n = n * 10 + (str[i++] - '0');
		list_add_back(&head, &tail, new_node(neg ? -n : n));
	}
	return (head);
}

static void	free_list(t_list *lst)
{
	t_list	*next;

	while (lst)
	{
		next = lst->next;
		free(lst->data);
		free(lst);
		lst = next;
	}
}

static void	print_int(void *data)
{
	printf("%d\n", *(int *)data);
}

int	main(int argc, char **argv)
{
	t_list	*lst;

	if (argc != 2)
		return (1);
	lst = build_list(argv[1]);
	ft_list_foreach(lst, print_int);
	free_list(lst);
	return (0);
}
