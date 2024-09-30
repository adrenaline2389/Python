#include <stdio.h>
#include <stdlib.h>

// 定义二叉树节点
struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

// 创建新的节点
struct TreeNode* createNode(int val) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->val = val;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// 前序遍历
void preorder(struct TreeNode* root) {
    if (root == NULL) return;
    printf("%d ", root->val);  // 访问根节点
    preorder(root->left);      // 递归遍历左子树
    preorder(root->right);     // 递归遍历右子树
}

// 中序遍历
void inorder(struct TreeNode* root) {
    if (root == NULL) return;
    inorder(root->left);       // 递归遍历左子树
    printf("%d ", root->val);  // 访问根节点
    inorder(root->right);      // 递归遍历右子树
}

// 后序遍历
void postorder(struct TreeNode* root) {
    if (root == NULL) return;
    postorder(root->left);     // 递归遍历左子树
    postorder(root->right);    // 递归遍历右子树
    printf("%d ", root->val);  // 访问根节点
}

// 队列结构和实现
#define MAX_SIZE 100

struct TreeNode* queue[MAX_SIZE];
int front = 0, rear = 0;

// 入队
void enqueue(struct TreeNode* node) {
    if (rear == MAX_SIZE) {
        printf("Queue is full!\n");
        return;
    }
    queue[rear++] = node;
}

// 出队
struct TreeNode* dequeue() {
    if (front == rear) {
        printf("Queue is empty!\n");
        return NULL;
    }
    return queue[front++];
}

// 检查队列是否为空
int isEmpty() {
    return front == rear;
}

// 层序遍历
void levelOrder(struct TreeNode* root) {
    if (root == NULL) return;

    enqueue(root);

    while (!isEmpty()) {
        struct TreeNode* current = dequeue();
        printf("%d ", current->val);  // 访问当前节点

        if (current->left != NULL) {
            enqueue(current->left);   // 把左子节点加入队列
        }
        if (current->right != NULL) {
            enqueue(current->right);  // 把右子节点加入队列
        }
    }
}

int main() {
    // 创建示例二叉树
    struct TreeNode* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    // 前序遍历
    printf("PreOrder: ");
    preorder(root);
    printf("\n");

    // 中序遍历
    printf("InOrder: ");
    inorder(root);
    printf("\n");

    // 后序遍历
    printf("PostOrder: ");
    postorder(root);
    printf("\n");

    // 层序遍历
    printf("LevelOrder: ");
    levelOrder(root);
    printf("\n");

    return 0;
}