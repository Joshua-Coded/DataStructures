//QUEUE IMPLEMENTATION IN C
#include <stdio.h>
#define SIZE 5

void enQueue(int);
void deQueue();
void display();

int items[SIZE], front = -1, rear = -1;

int main()
{
  // deQueue is not possible on empty queue
  deQueue();

  //enQueue 5 elements
  enQueue(1);
   enQueue(2);
    enQueue(3);
     enQueue(4);
      enQueue(5);

      // check for error
      enQueue(6);

      //display the items
      display();

      // deQueue first element entered
      deQueue();

      //display items
      display();


      return 0;
}

// function for enQueue

void enQueue(int value){
  if(rear == SIZE -1)
    printf("Queue is full!!\n");
  else {
    if(front == -1)
      front = 0;
    rear++;
    items[rear] = value;
    printf("\nInserted -> %d", value);
  }

}

// function for deQueue

void deQueue(){
  if(front == -1)
    printf("Queue is empty!!\n");
  else {

    printf("\nDeleted : %d", items[front]);

    front++;
    if(front > rear)
      front = rear = -1;
  }
}

// function for printing the queues

void display(){
  if(rear == -1)
    printf("\nQueue is empty:: can't print empty queue");

  else {
    int i;
    for(i = 0; i<= rear; i++)
      printf("%d", items[i]);
  }
  printf("\n");
}
