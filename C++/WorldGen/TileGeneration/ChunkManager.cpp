#include "ChunkManager.h"
#include <fstream>
#include <filesystem>
#include <array>
#include <iostream>
#include <string>
#include <FastNoise/FastNoise.h>

namespace fs = std::filesystem;

const std::unordered_map<std::string, std::array<float, 3>> info = {
    {"land", {-0.015f, 0.0f, 2.0f}}
};

size_t ChunkCoordHash::operator()(const ChunkCoord& c) const {
    return std::hash<int>()(c.x) ^ (std::hash<int>()(c.y) << 1);
}

bool ChunkCoordEq::operator()(const ChunkCoord& a, const ChunkCoord& b) const {
    return a.x == b.x && a.y == b.y;
}

//Takes in a size 2 vector, returns a size 2 vector
std::array<int,2> RelativeToChunk(const std::array<int, 2> inputCoords)
{
    std::array<int, 2> returnCoords;

    returnCoords[0] = ((inputCoords[0] % 16) + 16) % 16;
    returnCoords[1] = ((inputCoords[1] % 16) + 16) % 16;
    return returnCoords;
}

void SaveChunk(const Chunk& chunk, const json& j)
{
    std::string path = "chunk_" + std::to_string(chunk.x) + "_" + std::to_string(chunk.y) + ".json";
    std::ofstream file(path);
    if (!file.is_open()) return;
    file << j.dump(4);
}

bool LoadChunk(const Chunk& chunk, const json& j)
{
    std::string path = "chunk_" + std::to_string(chunk.x) + "_" + std::to_string(chunk.y) + ".json";
    return fs::exists(path);
}


Chunk GenerateChunk(ChunkCoord chunkCoord, FastNoise::SmartNode<FastNoise::FractalFBm>& fnNoise, int seed)
{
    Chunk chunk = {chunkCoord.x, chunkCoord.y};
    uint8_t currentTile;
    std::vector<float> landOutput(16 * 16);
    fnNoise->GenUniformGrid2D(landOutput.data(), chunk.x * 16, chunk.y * 16, 16, 16, .01f, seed);

    for (int initX = 0; initX < 16; initX++)
    {
        for (int initY = 0; initY < 16; initY++)
        {
            if (info.at("land")[0] < landOutput[(16 * initY) + initX])
            {
                currentTile = static_cast<uint8_t>(info.at("land")[2]);
            }
            else
            {
                currentTile = static_cast<uint8_t>(info.at("land")[1]);
            }

            chunk.tiles[initX][initY].tileId = currentTile;
        }
    }
    return chunk;
}

char GetTileGraphic(Chunk chunk, std::array<int, 2> tileRelativeToChunk)
{
    switch (chunk.tiles[tileRelativeToChunk[0]][tileRelativeToChunk[1]].tileId)
    {
        case 0:
            return('~');
            break;
        case 1:
            return('X');
            break;
        case 2:
            return ('"');
            break;
        default:
            return('X');
            break;
    }
}