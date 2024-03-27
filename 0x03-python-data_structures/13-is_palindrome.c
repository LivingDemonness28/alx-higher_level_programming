#include "lists.h"
#include "13-reverse"

/**
* is_palindrome - Checks if list is palindrome.
* @head: ptr to head of the linked list.
* Return: 1 (Success), 0 (Otherwise).
*/
int is_palindrome(listint_t **head)
{
listint_t *current, *rev, *mid;
size_t size = 0, i;

if (*head == NULL || (*head)->next == NULL)
return (1);

current = *head;
for (; current != NULL; current = current->next)
{
size++;
}

current = *head;
for (i = 0; i < (size / 2) - 1; i++)
{
current = current->next;
}

if ((size % 2) == 0 && current->n != current->next->n)
return (0);

current = current->next->next;
rev = _reverse(&current);
mid = rev;

current = *head;
while (rev)
{
if (current->n != rev->n)
return (0);
current = current->next;
rev = rev->next;
}
_reverse(&mid);

return (1);
}
