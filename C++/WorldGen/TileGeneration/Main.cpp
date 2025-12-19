#include <iostream>
#include <FastNoise/FastNoise.h>
#include <conio.h>
#include <vector>
#include <string>
#include "ChunkManager.h"
#include "Output.h"
#include "Input.h"

std::unordered_map<ChunkCoord, Chunk, ChunkCoordHash, ChunkCoordEq> chunkMap;

int main()
{
    LockBufferToWindow();
    ClearDisplay();
    int width = GetConsoleWidth();
    int height = GetConsoleHeight();
    //How many chunks need to be rendered to display to whole screen
    std::vector<int> rDistance = { static_cast<int>(std::ceil(width / 16.f))+ 1, static_cast<int>(std::round(height / 16.f)) + 1 };
    std::string output = "";
    std::array<int, 2> coords = { 0,0 };

    int seed = 1337;
    auto fnSimplex = FastNoise::New<FastNoise::Simplex>();
    auto fnFractal = FastNoise::New<FastNoise::FractalFBm>();
    fnFractal->SetSource(fnSimplex);
    fnFractal->SetOctaveCount(4);
    fnFractal->SetGain(1.900f);
    fnFractal->SetWeightedStrength(0.800f);
    fnFractal->SetLacunarity(0.600f);
    //std::cout << ">>>" << static_cast<uint8_t>(defaultGenInfo.at("land")[2]) << "<<<" << std::endl;

    while (true)
    {
        display(width, height, coords, chunkMap, fnFractal, seed);
        std::array<int, 2> offset = Movement();
        coords[0] -= offset[0];
        coords[1] -= offset[1];
    }
}