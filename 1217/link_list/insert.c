#include "stdio.h"
#include "malloc.h"
#define LEN sizeof(struct student)

struct student
{
     long num;
     int score;
     struct student *next;
};

struct student *create(int n)
{ 
     struct student *head=NULL,*p1=NULL,*p2=NULL;
     int i;
     for(i=1;i<=n;i++)
     {  p1=(struct student *)malloc(LEN);
        scanf("%ld",&p1->num);    
        scanf("%d",&p1->score);    
        p1->next=NULL;
        if(i==1) head=p1;
        else p2->next=p1;
        p2=p1;
      }
      return(head);
}

void print(struct student *head)
{
    struct student *p;
    p=head;
    while(p!=NULL)
    {
        printf("%ld\t%d",p->num,p->score);
        p=p->next;
        printf("\n");
    }
}

struct student *insert(struct student *head, struct student *stud)
{  
    struct student *p0,*p1,*p2;
    p1=head;
    p0=stud;
    if(head==NULL)//如果head是空表 则令head指向p0 ，p0的next指向null
    {
        head=p0;
        p0->next=NULL;
    }
    else     //否则当需要插入的号码大于原有表中的号码且原有表p1的next不为空时，让p2指向p1，p1指向下一个
    {
        while((p0->num>p1->num)&&(p1->next!=NULL))
        {
            p2=p1;
            p1=p1->next;
        }
        if(p0->num<=p1->num)//说明p0在p1前面，如果前面没有其他元素了，head->p0->p1;如果前面还有其他元素head->...->p2->p0->p1
        {
            if(head==p1)head=p0;
            else p2->next=p0;
            p0->next=p1;
        }
        else//如果p0在p1后面 p1->p0->null
        {
            p1->next=p0;
            p0->next=NULL;
        }
    }
    return(head);
}

main()
{
    struct student *head,*stu;
    int n;
    scanf("%d",&n);   
    head=create(n);
    print(head);
    stu=(struct student *)malloc(LEN);
    scanf("%ld",&stu->num);        
    scanf("%d",&stu->score);    
    stu->next = NULL;
    head=insert(head,stu);
    print(head);
}