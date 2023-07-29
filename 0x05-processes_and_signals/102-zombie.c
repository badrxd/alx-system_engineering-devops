#include <stdio.h>
#include <unistd.h>

/**
* infinite_while - loop
*
* Return: 0
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - display 5 of zombies process
*
* Return: 0
*/

int main(void)
{
	pid_t ch_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
	ch_pid = fork();
	if (ch_pid > 0)
	{
		printf("Zombie process created, PID: %d\n", ch_pid);
	}
	else
	{
		return (0);
	}
	}
	infinite_while();
	return (0);
}
