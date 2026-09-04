/*
** sort_list  —  DRIVER
** prototype : t_list *sort_list(t_list *lst, int (*cmp)(int, int));
** parse 1 arg  ->  av[1] = space-separated ints
** build a t_list (data = int); cmp(a, b) returns (a <= b)
** call sort_list, print the sorted ints, one per line
*/

#include "super.h"
#include "list.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

static t_list	*new_node(int value)
{
	t_list	*node;

	node = malloc(sizeof(t_list));
	node->data = value;
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
		free(lst);
		lst = next;
	}
}

static int	ascending(int a, int b)
{
	return (a <= b);
}

int	main(int argc, char **argv)
{
	t_list	*lst;
	t_list	*head;

	if (argc != 2)
		return (1);
	lst = build_list(argv[1]);
	lst = sort_list(lst, ascending);
	head = lst;
	while (lst)
	{
		printf("%d\n", lst->data);
		lst = lst->next;
	}
	free_list(head);
	return (0);
}
