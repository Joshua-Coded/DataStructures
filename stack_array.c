#include <stdio.h>
#include <stdlib.h>

#define N 5
int stack[N];
int top = -1;

void push()
{
  int x;
  printf("Enter data: \n");
  scanf("%d", &x);

  if(top == N-1)
    {
      printf("Overflow condition, you cannot insert: \n");
    }
  else {
    top++;
    stack[top] = x;
  }

}

void pop()
{
  int item;

  if(top == -1)
    {
      printf("underflow, nothing to remove: \n");
    }
  else {
    item = stack[top];
    top--;
    printf("%d", item);
  }
}

void peek()
{
  if(top == -1)
    {
      printf("stack is empty:\n");
    }
  else {
    printf("the top most element is %d", stack[top]);
      }
}

void display()
{
  int i;
  for(i = top; i >= 0; i--)
    {
      printf("%d", stack[i]);
    }
}


int main()
{
  int ch;
  printf("stack operation with choices \n 1 for push \n 2 for pop\n 3 for peek\n 4 for display:\n 0 for exit\n");

    printf("Enter your choice:");
    scanf("%d", &ch);
    switch(ch)
      {
      case1:
	push();
	break;
      case2:
	pop();
	break;
      case3:
	peek();
	break;
      case4:
	display();
	break;
      case0:
	exit(0);

      default:
	printf("invalid choice:");
      }

  while (ch!=0);
  return 0;
    }
