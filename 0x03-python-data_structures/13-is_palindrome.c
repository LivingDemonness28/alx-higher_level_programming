#include "lists.h"

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the linked list.
*
* Return: If the linked list is not a palindrome - 0.
* If the linked list is a palindrome - 1.
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
rev = reverse_listint(&current);
mid = rev;

current = *head;
while (rev)
{
if (current->n != rev->n)
return (0);
current = current->next;
rev = rev->next;
}
reverse_listint(&mid);

return (1);
}
