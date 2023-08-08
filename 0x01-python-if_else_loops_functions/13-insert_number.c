#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the address of first node of list
 * @number: number to insert (in ascending order)
 *
 * Return: address of inserted node ot NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;

	/* empty list */
	if (!*head)
		*head = new;
	else if (current->n > number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next && current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}

	return (new);
}