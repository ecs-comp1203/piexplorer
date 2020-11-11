#include <stdio.h>
#define NUM 1024*1024*1024
void main()
{
	int a,b,c;
	b = 0;
	for( a=0; a < NUM; a++)
	{
		b += a & 0x01;
	}
	printf("%d\n",b);
}

