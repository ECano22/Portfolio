<h1>WorldGen - Console Tile Generator</h1>

<p>This project is a C++ console application that demonstrates procedural world generation using a chunk-based system. It generates an infinite, explorable 2D terrain directly in the console window, utilizing noise algorithms to create organic terrain patterns.</p>

<h2>Skills & Concepts Demonstrated</h2>

<h3>1. Third-Party Library Integration</h3>
<ul>
    <li><strong>FastNoise:</strong> Integrated the FastNoise library to implement Simplex noise and Fractal Brownian Motion (FractalFBm) for organic terrain generation.</li>
</ul>

<h3>2. Game Development Algorithms</h3>
<ul>
    <li><strong>Procedural Generation:</strong> Implemented algorithms to generate terrain on-the-fly based on noise thresholds (e.g., determining water vs. land tiles).</li>
    <li><strong>Chunk-Based Architecture:</strong> Designed an infinite world system that divides the map into 16x16 chunks. This requires managing coordinate systems to translate global player coordinates into local chunk coordinates.</li>
    <li><strong>Spatial Hashing:</strong> Created custom hash (<code>ChunkCoordHash</code>) and equality structs to efficiently store and retrieve chunks in an <code>std::unordered_map</code> using coordinate pairs as keys.</li>
</ul>

<h3>3. Systems Programming & Optimization</h3>
<ul>
    <li><strong>Windows Console API:</strong> Directly interfaced with the Windows API (<code>&lt;windows.h&gt;</code>) to manipulate the console buffer. This includes locking the buffer size to the window and setting cursor positions for smooth rendering (avoiding the flicker associated with standard <code>system("cls")</code>).</li>
    <li><strong>Memory Management:</strong> Managed dynamic object creation for noise generators and efficient data structures for caching generated chunks.</li>
</ul>

<h3>4. C++ Proficiency</h3>
<ul>
    <li><strong>STL Containers:</strong> Extensive use of <code>std::vector</code>, <code>std::unordered_map</code>, and <code>std::array</code> for data management.</li>
</ul>

<h2>How It Works</h2>
<p>The application renders a viewport of the world based on the console window's size. As the player moves (using WASD or arrow keys), the engine calculates which chunks are visible. If a chunk exists in memory, it is rendered; if not, it is procedurally generated using FastNoise and cached.</p>
