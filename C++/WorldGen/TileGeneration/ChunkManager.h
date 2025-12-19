#pragma once
#include <unordered_map>
#include <array>
#include <cstdint>
#include <FastNoise/FastNoise.h>
#include "json.hpp"

using json = nlohmann::json;

struct Tile
{
    uint8_t tileId;
};

struct Chunk
{
    int x, y;
    Tile tiles[16][16];
};

struct ChunkCoord
{
    int x, y;
};

struct ChunkCoordHash
{
    size_t operator()(const ChunkCoord& c) const;
};

struct ChunkCoordEq
{
    bool operator()(const ChunkCoord& a, const ChunkCoord& b) const;
};

extern const std::unordered_map<std::string, std::array<float, 3>> defaultGenInfo;

// Global Functions
std::array<int, 2> RelativeToChunk(const std::array<int, 2>);
void SaveChunk(const Chunk& chunk, const json& j);
bool LoadChunk(const Chunk& chunk, const json& j);
Chunk GenerateChunk(ChunkCoord chunkCoord, FastNoise::SmartNode<FastNoise::FractalFBm>& fnNoise, int seed);
char GetTileGraphic(Chunk chunk, std::array<int, 2> tileRelativeToChunk);