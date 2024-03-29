#include <stdio.h>
#include <stdlib.h>

//Author: Joshua Alana
// Date: 29/03/23
//location: African Leadership University


void push();
void pop();
void display();


int main()
{
  int choice;
  while(1)
    {
      printf("\nOperations performed in linked_list stack");
      printf("\n1. Push a data into a stack\n2. Pop a data from a stack\n3. Display the datas in the stack\n4. End operation");
      printf("\nEnter your choice of operation: ");
      scanf("%d", &choice);


      switch(choice)
	{
	case1: push();
	  break;
	case2: pop();
	  break;
	case3: display();
	  break;
	case4: exit(0);
	default: printf("\n Invalid choice!!");
	  
	}
    }
}




struct node
  {
    int data;
    struct node * link;
};
  struct node *top = 0;

// push function for adding data linked_list

void push(int x)
{
  struct node *newnode;

  newnode = (struct node *)malloc(sizeof(struct node));

  newnode->data = x;

  newnode->link = top;
  top = newnode;

}

//pop function for removing data in link_list






// display function for displaying our datas

void display()
{
  struct node *temp;
  temp = top;

  if(top == 0)
    {
      printf("Stack is empty: \n");
    }
  else {

    while (temp != 0)
      {
	printf("%d", temp->data);
	temp = temp->link;
      }
  }
}


// peek function for displaying the top most data


void peek()
{
  if (top == 0)
    {
      printf("Stack is empty");
    }
    

 else {
       printf("Top element is: %d", top->data);

      }
}

// pop function for deleting data from stack

void pop()
{
  struct node *temp;
  temp = top;

  if(top == 0)
    {
      printf("Underflow condition: No data in stack:\n");
    }
  else {
    printf("%d", top->data);
    top = top->link;
    free(temp);
    
  }

}
