/*
** ft_split  —  reference implementation
** char **ft_split(char *str);
*/

#include <stdlib.h>

static int	is_sep(char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

static int	count_words(char *str)
{
	int	count;
	int	i;

	count = 0;
	i = 0;
	while (str[i])
	{
		while (is_sep(str[i]))
			i++;
		if (str[i])
			count++;
		while (str[i] && !is_sep(str[i]))
			i++;
	}
	return (count);
}

static char	*dup_word(char *str, int start, int len)
{
	char	*word;
	int		i;

	word = malloc(len + 1);
	if (!word)
		return (NULL);
	i = 0;
	while (i < len)
	{
		word[i] = str[start + i];
		i++;
	}
	word[len] = '\0';
	return (word);
}

char	**ft_split(char *str)
{
	char	**result;
	int		nwords;
	int		i;
	int		w;
	int		start;

	nwords = count_words(str);
	result = malloc(sizeof(char *) * (nwords + 1));
	if (!result)
		return (NULL);
	i = 0;
	w = 0;
	while (w < nwords)
	{
		while (is_sep(str[i]))
			i++;
		start = i;
		while (str[i] && !is_sep(str[i]))
			i++;
		result[w] = dup_word(str, start, i - start);
		w++;
	}
	result[nwords] = NULL;
	return (result);
}
