#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return:  0 when no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ave, *don;

	if (list == NULL || list->next == NULL)
	return (0);

	ave = list->next;
	don = list->next->next;

	while (ave && don && don->next)
	{
		if (ave == don)
			return (1);
		ave = ave->next;
		don = don->next->next;
	}

	return (0);
}
