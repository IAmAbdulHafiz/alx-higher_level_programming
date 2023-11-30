#include "lists.h"

/**
 * insert_node - Inserts a num into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @num: The num to insert.
 *
 * Return: If the function fails - NULL. Otherwise - a pointer to the 
 * current node.
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *node = *head, *current;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	current->n = num;

	if (node == NULL || node->n >= num)
	{
		current->next = node;
		*head = current;
		return (current);
	}

	while (node && node->next && node->next->n < num)
		node = node->next;

	current->next = node->next;
	node->next = current;

	return (current);
