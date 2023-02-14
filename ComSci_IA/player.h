#ifndef PLAYER_H_INCLUDED
#define PLAYER_H_INCLUDED

typedef struct
{
    char name[50];
    int jerseyNum;
    char position[10];
    int serves;
    int blocks;
    int attacks;
    int serveMis;
    int passMis;
    int setMis;
    int attackMis;
    int blockMis;
    int sets;
    int passes;
} Player;

#endif
