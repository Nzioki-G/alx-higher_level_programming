#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node into a sorted list
 * @head: the first node of the list
 * @number: the value of node to insert
 *
 * Return: the address of the inserted node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = (*head);

	new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (NULL);
	}

	new->n = number;
	while (current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (*head);
}
