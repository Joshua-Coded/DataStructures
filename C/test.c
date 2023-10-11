#include <stdio.h>
#include "DATASTRUCTURES/LinkedList.h"

int main()
{
    struct LinkedList_int list = linked_list_int_constructor();

    for (int i =0; i < 10; i++)
    {
        list_insert(1, 1, &list);
    }
    list.remove(3, &list);
    list.remove(7, &list);
    list.remove(1, 99, &list);

    for (int i = 0; i < 9; i++)
    {
        printf("%d\n", list.retrieve, &list);
    }
    list.retrieve(100, &list);
}