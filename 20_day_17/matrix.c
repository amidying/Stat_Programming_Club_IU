#include<stdio.h>
#include<stdlib.h>
#include<conio.h>


#define nL printf("\n")
int main()
{
    int arr[3][3];
    printf("enter your matrix: \n");
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            printf(" %d",arr[i][j]);
        }nL;
    }
    return 0;
}