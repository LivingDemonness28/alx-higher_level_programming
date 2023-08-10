#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 * Return: 1 if there is a cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
listint_t *s = list, *f = list;

if (!list)
return (0);

for (; f && f->next; s = s->next, f = f->next->next)
{
if (s == f)
return (1);
}
return (0);
}
