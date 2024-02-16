#include <stdio.h>
#include <sys/time.h>

long micros()
{
	struct timeval currentTime;
	gettimeofday(&currentTime, NULL);
	return currentTime.tv_sec*1000000 + currentTime.tv_usec;
}

int main()
{
	int cnt;
	long start, end;


	start = micros();

	while(1==1) {
		cnt = cnt + 1;
		if(cnt>10000000)
			break;
	}
	end = micros();
	printf("%d\n", cnt);
	printf("%f\n", (end-start)/1000000.0);
}
