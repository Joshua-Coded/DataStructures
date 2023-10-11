#include <stdio.h>
#include <stdlib.h>

#define SIZE 10
int Top = -1, stack[SIZE];

void push();
void pop();
void display();

int main()
{
  int choice;
  while(1)
    {
      printf("\nOperations performed in stack");
      printf("\n1. Push the element\n2.Pop the element\n3.Display the element\n4. End");
      printf("\n\Enter the choice:");
      scanf("%d", &choice);


      switch(choice)
	{
	case 1: push();
	  break;
	case 2: pop();
	  break;
	case 3: display();
	  break;
	case 4: exit(0);
	default: printf("\nInvalid choice!!");
	}
    }
  
}


void push()
{

  int x;
  if(Top == SIZE-1)
    {
      printf("\nOverflow!!");
    }
  else {
    printf("Enter your data to be inserted to the stack: \n");
    scanf("%d", &x);
    Top=Top+1;
    stack[Top] = x;
    
  }
}

void pop()
{
  if(Top == -1)
    {
      printf("\nUndeflow!!");
    }
  else {
    printf("\nPopped data: %d", stack[Top]);
    Top=Top-1;
  }
}

void display()
{
  if(Top == -1)
    {
      printf("\nUnderflow!!");
    }
  else {
    printf("\nElement present in the stack: \n");
    for(int i=Top;i>=0;i--)
      printf("%d\n", stack[i]);
  }
}
