#include "stdio.h"
#include "malloc.h"
#define LEN sizeof(struct DATA)

struct DATA
{
     long num;
     struct DATA *next;
};

struct DATA *create(int n)
{
     struct DATA *head=NULL,*p1=NULL,*p2=NULL;
     int i;
     for(i=1;i<=n;i++)
     {  p1=(struct DATA *)malloc(LEN);
        scanf("%ld",&p1->num);
        p1->next=NULL;
        if(i==1) head=p1;
        else p2->next=p1;
        p2=p1;
      }
      return(head);
}

struct DATA *merge(struct DATA *head, struct DATA *head2)
{
    struct DATA *p1;
    p1=head;
    while(p1->next!=NULL)
    {
        p1=p1->next;
    }
    p1->next=head2;
    return head;
}

struct DATA *insert(struct DATA *head, struct DATA *d)
{
    struct DATA *p1,*p2,*p3;
    p1=head;
    p2=d;
    if(head==NULL)
    {
        head=p2;
        p2->next=NULL;
    }
    else
    {
        while((p1->num < p2->num) && (p1->next!=NULL))
        {
            p3=p1;
            p1=p1->next;
        }
        if(p1->num >= p2->num)
        {
            if(head==p1)
                head=p2;
            else
                p3->next=p2;
            p2->next=p1;
        }
        else
        {
            p1->next=p2;
            p2->next=NULL;
        }
    }
    return head;
}

struct DATA *sort(struct DATA *head) 
{ 
    struct DATA *p1=head,*p2=head;
    p1=p1->next;
    p2->next=NULL;
    p2=p1;
    p1=p1->next;
    p2->next=NULL;
    while(p1!=NULL)
    {
        head=insert(head,p2);
        p2=p1;
        p1=p1->next;
        p2->next=NULL;
    }
    head=insert(head,p2);
    return head;
} 

void print(struct DATA *head)
{
    struct DATA *p;
    p=head;
    while(p!=NULL)
    {
        printf("%ld",p->num);
        p=p->next;
        printf("\n");
    }
}

main()
{
    struct DATA *head, *head2;
    int n;
    long del_num;
    scanf("%d",&n);
    head=create(n);
    scanf("%d",&n);
    head2=create(n);
    head = merge(head, head2);
    head = sort(head);
    print(head);
}