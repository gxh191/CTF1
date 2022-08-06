#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<ucontext.h>

void init() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

char love[8] = "loveyou";
int main()
{
    char hate[8] = "hateyou";
    char str[16];
    init();
    puts("攻略金秋雨小游戏,想办法取得女神的芳心\n金秋雨好像并不喜欢你，你想对ta说什么");
    read(0,str,32);
    if (strcmp(love,hate))
    {
        puts("金秋雨已经爱上了你");
        system("/bin/sh");
        exit(0);
    }
    puts("你没有把握机会，女神离你而去");
    return 0;
}