#include<stdio.h>

int main(){

int i=0,sum=0;
do{
	if(i!=(i/9)*10)
		sum+=i;
}while(++i<100);
	printf("%d\n",sum);
}
