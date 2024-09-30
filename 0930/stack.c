#include <stdio.h>
#define MAX 5  // 栈的最大容量

// 定义栈结构
struct Stack {
    int data[MAX];  // 栈中的元素
    int top;        // 栈顶指针
};

// 初始化栈
void initStack(struct Stack* stack) {
    stack->top = -1;  // 初始化时，栈为空，top = -1
}

// 压入元素（push）
void push(struct Stack* stack, int value) {
    if (stack->top == MAX - 1) {  // 检查栈是否满了
        printf("Stack overflow!\n");
        return;
    }
    stack->data[++stack->top] = value;  // 将元素压入栈顶，并更新 top
    printf("Pushed %d to stack. Stack top is now %d\n", value, stack->top);
}

// 弹出元素（pop）
int pop(struct Stack* stack) {
    if (stack->top == -1) {  // 检查栈是否为空
        printf("Stack underflow!\n");
        return -1;
    }
    int popped_value = stack->data[stack->top--];  // 弹出栈顶元素，并更新 top
    printf("Popped %d from stack. Stack top is now %d\n", popped_value, stack->top);
    return popped_value;
}

// 打印栈的状态
void printStack(struct Stack* stack) {
    if (stack->top == -1) {
        printf("Stack is empty.\n");
        return;
    }
    printf("Current stack: ");
    for (int i = 0; i <= stack->top; i++) {
        printf("%d ", stack->data[i]);
    }
    printf("\n");
}

int main() {
    struct Stack stack;  // 创建一个栈
    initStack(&stack);   // 初始化栈

    // 压入 1, 2, 3, 4, 5
    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);
    push(&stack, 4);
    push(&stack, 5);

    // 打印当前栈
    printStack(&stack);

    // 弹出所有元素
    pop(&stack);
    pop(&stack);
    pop(&stack);
    pop(&stack);
    pop(&stack);

    // 再次打印栈
    printStack(&stack);

    return 0;
}