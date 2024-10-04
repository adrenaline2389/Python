#include <iostream>
using namespace std;

struct node
{
	int data;
	node* next;
};


node* Create()
{
	node *cur, *pre;
	node* head = NULL;
	cur = new node;
	cin>>cur->data;
	while (cur->data != 0)
	{
		if (head == NULL)
		{
			head = cur;
		}
		else 
		{
			pre->next = cur;
		}
		pre = cur;
		cur = new node;
		cin>>cur->data;
	}
	pre->next = NULL;
	delete cur;
	return head;
}

void insert(int n, int c, node *temp)
{
	// 把元素内容放进节点里面
	node *new_node = new node;
	new_node->data = c;
	// 移动temp到n处
	for (int i = 0; i < n; i++) {
		temp = temp->next;
	}
	// 插入
	new_node->next = temp->next;
	temp->next = new_node;
}

void del(int n, node *head) {
	node *p = head;
	for (int i = 0; i < n-1; i++) {
		head = head->next;
		p = p->next;
	}
	head = head->next;
	p->next = head->next;
	delete head;
}

void print(node* n)
{
	while(n)
	{
		printf("%d", n->data);
		n = n->next;
	}
}


int main()
{
	node* head;
	head = Create();
	insert(2, 4, head);
	del(4, head);
	print(head);
	return 0;
}
