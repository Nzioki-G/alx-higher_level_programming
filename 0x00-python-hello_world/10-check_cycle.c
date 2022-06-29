#include "lists.h"
 
/**
 * check_cycle - checks if a list has a cycle in it
 * @list: singly linked list under consideration
 *
 * Return: 0-> no cycle, 1-> cycle 
 */
int check_cycle(listint_t *list)
{
	listint_t *each = list, *alternate = list;

	while (each->next && alternate->next->next)
	{
		/* if either ever point to the other, we have a loop */
		if (alternate->next->next == each)
		{
			return (1);
		}
		each = each->next;
		alternate = alternate->next->next;
	}
	return (0);
}
