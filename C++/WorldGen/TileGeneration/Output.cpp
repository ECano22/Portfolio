#define NOMINMAX
#include <windows.h>
#include <iostream>
#include <vector>
#include <array>
#include <FastNoise/FastNoise.h>
#include "ChunkManager.h"
#include "output.h"
int GetConsoleWidth()
{
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
    return csbi.srWindow.Right - csbi.srWindow.Left + 1;
}

int GetConsoleHeight()
{
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi);
    return csbi.srWindow.Bottom - csbi.srWindow.Top + 1;
}

void display(const int width, const int height, const std::array<int, 2> coords, std::unordered_map<ChunkCoord, Chunk, ChunkCoordHash, ChunkCoordEq>& chunkMap, FastNoise::SmartNode<FastNoise::FractalFBm>& fnNoise, int seed)
{
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), { 0, 0 });
    //coords-center should equal bottom left. if even number, center should be top left
    std::array<int, 2> center{ width / 2, height / 2 };
    std::array<int, 2> tileCoord{ coords[0] - center[0], coords[1] + center[1] };
    ChunkCoord chunkCoord;
    Chunk currentChunk;
    std::string output = "";
    char tileGraphic;
    //tile coords relative to parent chunk
    std::array<int, 2> tcCoord;

    //Printing out display
    for (int printy = 0; printy < height; printy++)
    {
        tileCoord[0] = coords[0] - center[0];
        
        for (int printx = 0; printx < width; printx++)
        {
            if (tileCoord == coords)
            {
                output += "@";
            }
            else
            {
                chunkCoord.x = std::floor(tileCoord[0] / 16.f);
                chunkCoord.y = std::floor(tileCoord[1] / 16.f);

                //checking unordered map rn, should look for json files later
                if (chunkMap.find(chunkCoord) == chunkMap.end())
                {
                    Chunk newChunk = GenerateChunk(chunkCoord, fnNoise, seed);
                    chunkMap[chunkCoord] = newChunk;
                }
                tcCoord = RelativeToChunk(tileCoord);
                currentChunk = chunkMap[chunkCoord];

                //std::cout << "Chunk: {" << chunkCoord.x << ", " << chunkCoord.y << "} Tile: {" << tcCoord[0] << ", " << tcCoord[1] << "}" << std::endl;

                tileGraphic = GetTileGraphic(currentChunk, tcCoord);
                output += tileGraphic;
            }
            tileCoord[0]++;
        }
        //skip this on last run
        if (printy != height-1) output += "\n";
        tileCoord[1]--;
        //std::cout << "==========\n==========\n==========" << std::endl;
    }
    std::cout << output;
    return;
}

void ClearDisplay()
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    DWORD written;
    DWORD cells;

    GetConsoleScreenBufferInfo(hConsole, &csbi);
    cells = csbi.dwSize.X * csbi.dwSize.Y;

    FillConsoleOutputCharacter(hConsole, ' ', cells, { 0, 0 }, &written);
    SetConsoleCursorPosition(hConsole, { 0, 0 });
}

void LockBufferToWindow()
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

    CONSOLE_SCREEN_BUFFER_INFO csbi;
    GetConsoleScreenBufferInfo(hConsole, &csbi);

    SMALL_RECT window = csbi.srWindow;

    COORD newSize;
    newSize.X = window.Right - window.Left + 1;
    newSize.Y = window.Bottom - window.Top + 1;

    SetConsoleScreenBufferSize(hConsole, newSize);
}
