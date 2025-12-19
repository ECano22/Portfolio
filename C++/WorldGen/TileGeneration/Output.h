#pragma once
#include <vector>
#include <FastNoise/FastNoise.h>
#include "ChunkManager.h"

//Global Functions
int GetConsoleWidth();
int GetConsoleHeight();
void display(const int width, const int height, const std::array<int, 2> coords, std::unordered_map<ChunkCoord, Chunk, ChunkCoordHash, ChunkCoordEq>& chunkMap, FastNoise::SmartNode<FastNoise::FractalFBm>& fnNoise, int seed);
void ClearDisplay();
void LockBufferToWindow();