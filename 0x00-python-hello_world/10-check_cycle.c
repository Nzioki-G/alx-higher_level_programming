#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the linked list to ckeck for cycle
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *one, *two;

	if (list == NULL)
		return (0);

	one = list->next;
	if (one == NULL)
		return (0);
	two = one->next;

	while (two != NULL)
	{
		/* if our nodes collide, we have a cycle */
		if (one == two)
			return (1);

		/* take 1 step */
		one = one->next;

		/* take 2 steps */
		two = two->next;
		if (two)
			two = two->next;
	}

	return (0);
}