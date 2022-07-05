#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to the list under consideration
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL, *prev = NULL;
	int len = 0, i = 0;
	int *arr;

	arr = malloc(sizeof(int));
	if (!arr)
		return (0);
	if (!*head)
		return (1);

	/* reverse order in list, original order in array */
	while ((*head)->next != NULL)
	{
		arr[len] = (*head)->n;

		/* reverse list */
		temp = (*head)->next;
		(*head)->next = prev;
		prev = *head;

		/* advance to the next */
		*head = temp;
		len++;
	}
	/* take care of the last node */
	arr[len] = (*head)->n;
	(*head)->next = prev;

	/* compare original and reversed lists until halfway */
	while (i < (len + 1) / 2)
	{
		/* if head and tail aren't same, not palindrome */
		if (arr[i] != (*head)->n)
			return (0);
		/* advance to the next node */
		*head = (*head)->next;
		i++;
	}

	return (1);
}
