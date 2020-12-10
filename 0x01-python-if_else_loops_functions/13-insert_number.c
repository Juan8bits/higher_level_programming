#include "lists.h"

/**
* insert_node - Function that inserts node in specifically position
* in a linked list.
* @head: Double pointer with address to head node.
* @number: Position to set new node.
* Return: Address to new node or Null if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *copyhead;
	listint_t *prenode;

	copyhead = *head;
	prenode = *head;
	if (!head)
		return (NULL);
/* Creation of new node */
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (copyhead == NULL || copyhead->n >= new->n)
	{
		new->next = copyhead;
		*head = new;
	}
	else
	{
/* Search position to new node */
		while (copyhead)
		{
			if (copyhead->n > new->n)
			{
				new->next = copyhead;
				prenode->next = new;
				break;
			}
			else if (copyhead->next == NULL)
			{
				copyhead->next = new;
				break;
			}
			prenode = copyhead;
			copyhead = copyhead->next;
		}
	}
	return (new);
}
