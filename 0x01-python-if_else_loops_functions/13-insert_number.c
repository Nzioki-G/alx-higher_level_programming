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
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (NULL);
	}

	new->n = number;
	while ((*head)->next->n < number)
	{
		(*head) = (*head)->next;
	}
	new->next = (*head)->next;
	(*head)->next = new;
	return (new);
}
