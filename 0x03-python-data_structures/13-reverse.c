#include "lists.h"

/**
 * _reverse - reverse singly-linked list.
 * @head: pointer to starting node of the list to reverse.
 * Return: ptr to head of rev list
*/

listint_t *_reverse(listint_t **head)
{
listint_t *n = *head, *after, *before = NULL;

for (; n; n = after)
{
after = n->next;
n->next = before;
before = n;
}
*head = before;
return (*head);
}
