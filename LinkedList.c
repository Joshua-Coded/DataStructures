#include "LinkedList.h"

struct Node_int * create_node_int(void);
void destroy_node_int(struct Node_int *node_to_destroy);

struct Node_int * iterate(int index, struct LinkedList_int *linked_list);

void insert_node_int(int index, int data, struct LinkedList_int *linked_list);
void remove_node_int(int index, struct LinkedList_int *linked_list);

int retrieve_data_int(int index, struct LinkedList_int *linked_list);
