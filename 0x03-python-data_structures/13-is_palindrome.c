#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of list
 *
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int len = 0, *array, idx;

	/* empty list is palindrome */
	if (!*head)
		return (1);

	current = *head;
	while (current)
	{
		len++;
		current = current->next;
	}

	current = *head;
	array = malloc(sizeof(int) * len / 2 + 1);
	for (idx = 0; idx < len / 2; idx++)
	{
		array[idx] = current->n;
		current = current->next;
	}

	if (len % 2 == 1)
		current = current->next;
	idx = len / 2 - 1;
	while (idx >= 0)
	{
		if (array[idx] != current->n)
			return (0);
		idx--;
		current = current->next;
	}
	return (1);
}