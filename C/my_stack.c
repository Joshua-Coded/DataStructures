#include <stdio.h>
#include <stdlib.h>

void push(int item);
void display();
void peek();
void pop();

struct node {
  int data;
  struct node *link;
};

struct node *top = 0;

int main()

{
  int choice, item;

  while(1)
    {
      printf("\n1.Insert\n2. Display\n3.Delete\n4 Peek\n5.Exit\n");
      printf("Enter your choice\n");
      scanf("%d", &choice);

      switch(choice)
	{
	case 1: printf("Enter the item to be Inserted: \n");
	  scanf("%d", &item);
	  push(item);
	  break;
	case 2: display();
	  break;
	case 3: pop();
	  break;
	case 4: peek();
	  break;
	case 5: exit(0);
	  break;
	default: printf("Wrong choice\n");
	}
    }
  while(choice != 0);

}

// push function

void push(int item)
{
  struct node *ptr;
  ptr = (struct node *)malloc(sizeof(struct node));
  ptr->data = item;
  ptr->link = top;
  top = ptr;
}


// dispay function

void display()
{
  struct node *temp;
  temp = top;

  if(top == NULL)
    {
      printf("Stack is empty: \n");
    }
  else {
	printf("The items in stack are: %d", temp->data);
	temp = temp->link;
  }
}


// peek function

void peek()
{

  if(top == NULL)
    {
      printf("stack is underflow");
    }
  else {
    printf("top element is %d", top->data);
  }
}

// pop function

void pop()
{
  struct node *temp;
  temp = top;
  if(top == NULL)
    {
      printf("STACK IS UNDERFLOW\n");
    }
  else {
    printf("%d", top->data);
    top = top->link;
    free(temp);
  }
}

