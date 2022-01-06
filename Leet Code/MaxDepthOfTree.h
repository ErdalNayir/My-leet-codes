#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* left;
    struct node* right;
}NODE;


NODE* newNode(int data)
{
    // Allocate memory for new node
    NODE* node = (NODE*)malloc(sizeof(NODE));

    // Assign data to this node
    node->data = data;

    // Initialize left and
    // right children as NULL
    node->left = NULL;
    node->right = NULL;
    return (node);
}

int maxDepth(NODE* root){

    if(root==NULL){
        return 0;
    }
    else{
        int leftdepth=maxDepth(root->left);
        int rightdepth=maxDepth(root->right);

        return leftdepth>rightdepth?leftdepth+1:rightdepth+1;
    }



}
