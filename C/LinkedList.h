#ifndef LinkedList_h
#define LinkedList_h

#include <stdio.h>
#include <stdlib.h>
#include "Node.h"


struct LinkedList_int
{
   struct Node_int *head;
   int length;

   void(*insert)(int index, struct LinkedList_int *linked_list);
   void (*remove)(int index, struct LinkedList_int *linked_list);
   int (*retrieve)(int index, struct LinkedList_int *linked_list);

};

struct LinkedList_int linked_list_constructor();

#endif