#include "lists.h"

/**
* check_cycle - Functiont that checks if have a loop in a linked list
* @list: Pointer to head node linked list
* Return: 0 if there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	if (list)
	{
		while (hare->next->next)
		{
			turtle = turtle->next;
			hare = hare->next->next;
			if (hare == turtle)
				return (1);
		}
	}
	return (0);
}
