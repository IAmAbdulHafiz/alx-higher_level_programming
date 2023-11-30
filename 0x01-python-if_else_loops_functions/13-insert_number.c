#include "lists.h"

/**
 * insert_node - Inserts a num into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @num: The num to insert.
 *
 * Return: If the function fails - NULL. Otherwise - a pointer to 
 * the new_value node.
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *node = *head, *new_value;

	new_value = malloc(sizeof(listint_t));
	if (new_value == NULL)
		return (NULL);
	new_value->n = num;

	if (node == NULL || node->n >= num)
	{
		new_value->next = node;
		*head = new_value;
		return (new_value);
	}

	while (node && node->next && node->next->n < num)
		node = node->next;

	new_value->next = node->next;
	node->next = new_value;

	return (new_value);
}
