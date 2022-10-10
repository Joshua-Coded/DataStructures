#include <stdio.h>
#include <stdlib.h>

#define SIZE 10
int queue[SIZE];
int front = -1;
int rear = -1;
void enQueue();
void deQueue();
void display();

int main()
{
  int choice;
  while(1)
    {
      printf("THE IMPLEMENTATION OF QUEUE IN C:");
      printf("\n1.Insert data to queue: \n");
      printf("\n2. Delete data from queue\n");
      printf("\n3. Show all datas of queue\n");
      printf("\n4. End operation\n");
      scanf("%d", &choice);

      switch(choice)
	{

	case 1:
	  enQueue();
	  break;
	case 2:
	  deQueue();
	  break;
	case 3:
	  display();
	  break;
	case 4:
	  exit(1);
	default:
	  printf("\nWrong choice\n");
	}
    }

}


void enQueue()
{
  int item;
  if(rear == SIZE-1)
    printf("\nQueue is Overflow\n");
  else
    {
      if(front == -1)
	front = 0;
      printf("INsert data in queue :\n");
      scanf("%d", &item);
      rear = rear +1;
      queue[rear] = item;
    }
}

void deQueue()
{
  if(front == -1 || front > rear)
    {
      printf("Queue Underflow\n");
      return;
    }
  else {
    printf("\nData deleted from queue %d", queue[front]);
    front = front + 1;
  }
}

void display()
{
  int i;
  if(front == -1)
    printf("\nQueue is empty\n");

 else {
   printf("Queue is : \n");
   for(i = front; i <= rear; i++)
     printf("\n%d", queue[i]);
   printf("\n");
 }
}
