/* A complete program for binary search and all operations*/

#include <stdio.h>
#include <conio.h>

struct node {
int data;
struct node * left;
struct node * right;
}

/* the functions prototypes */

struct node* tree;
void create_tree(struct node*);
struct node* insertElement(struct node*, int);
void preoder(struct node*);
void inorder(struct node*);
void postorder(struct node*);
struct node* deleteElement(struct node*, int);
int totalnodes(struct node*);
int height(struct node*);
struct node* deleteTree(struct node*);

void main(){
int option, val;
char ans;

struct node* ptr;
create_tree(tree);

do {
printf("\n 1. Insert");
printf("\n. 2 Preorder Traversing");
printf("\n. 3 Inorder Traversing");
printf("\n. 4 Postorder traversing");
printf("\n. 5 Delete an Element");
printf("\n. 6 Count nodes");
printf("\n. 7 Height of tree");
printf("\n. Delete tree");
printf("\n 9 Exit");
printf("\n Enter your option");
scanf("%d", &option);
switch(option)
{
case 1: printf("\n Enter the value of node");
	scanf("%d", &val);
	tree = insertElement(tree, val);
	break;
case 2: printf("Element of tree are : -");
	preorder(tree);
	break;
case 3: printf("\n Elements of tree are : -");
	inorder(tree);
	break;
case 4: printf("\n Elements of tree are  : -");
	postorder(tree);
	break;
case 5: printf("\n Enter element to delete");
	scanf("%d", &val);
	tree = deleteElement(tree, val);
	break;
case 6: printf("\n Number of nodes are %d", totalnodes(tree));
	break;
case 7: printf("\n Height of tree is %d", height(tree));
	break;
case 8: tree = deleteTree(tree);
	break;
case 9: exit(0);
}

printf("\n Do you want to continue: ");
ans=getche();
}

while (ans == 'y' || ans == 'Y');
getch();
}

void create_tree(struct node* tree)
{
tree = NULL;
}

struct node* insertElement(struct node* tree, int val){
struct node* ptr, *nodeptr, * parentptr;
ptr = (struct node*) malloc(sizeof(struct node));
ptr->data = val;
ptr->left = NULL;
ptr->right = NULL;

if (tree == NULL){
tree = ptr;
tree->left = NULL;
tree->right = NULL
} else {

parentptr = NULL;
nodeptr = tree;

while (nodeptr != NULL)
{
parentptr = nodeptr;
if(val < nodeptr->data)
nodeptr = nodeptr->left;
else
nodeptr = nodeptr->right;
}
if (val < parentptr->data)
parentptr->left = ptr;
else
parentptr->right = ptr;
}
return tree;
}

void preorder(struct node* tree)
{

if (tree != NULL)
{
printf("%d\t", tree->data);
preorder(tree->left);
preorder(tree->right);
}
}

void inorder(struct node* tree)
{
if (tree != NULL)
{
inorder(tree->left);
printf("%d\t", tree->data);
inorder(tree->right);
}
}

void postorder(struct node * tree)
{

if(tree != NULL)
{
postorder(tree->left);
postorder(tree->right);
printf("%d\t", tree->data);
}
}

struct node* deleteElement(struct node* tree, int val) {
struct node * cur, *parent, *suc, &psuc, *ptr;
if(tree->left == NULL)
{
printf("\n Tree is empty");
return (tree);
}

parent=tree;
cur = tree->left;
while (cur != NULL && val != cur->data)
{

parent = cur;
cur = (val < cur->data) ? cur->left : cur->right;
}

if (cur == NULL)
{
printf("\n Value to be deleted is not present");
return (tree);
}

if (cur->left == NULL)
ptr = cur->right;
else if (cur->right == NULL)
ptr = cur->left;
else {
psuc = cur;
cur = cur->left;
while (suc->left != NULL)
{

psuc = suc;
suc = suc->left;
}

if (cur == psuc)
{
suc->left = cur->right;
} 
else
{
suc->left = cur->left;
psuc->left = suc->right;
suc->right = cur->right;
}

ptr = suc;
}

if (parent->left == cur)
parent->left = ptr;
else
parent->right = ptr;
free(cur);
return (tree);
}

int totalnodes(struct node* tree)
{

if(tree == NULL)
return 0;
else
return (totalnodes(tree->left) + totalnodes(tree->right) + 1);
}

int height(struct node * tree)
{
int lh, rh;

if (tree == NULL)
return 0;
else {
lh = height(tree->left);
rh = height(tree->rigt);

if(lh>rh)
return (lh + 1);
else
return (rh + 1);
}
}

struct node* deleteTree(struct node* tree)
{
if (tree != NULL)
{

deleteTree(tree->left);
deleteTree(tree->right);
free(tree);
return 0;
}
}

