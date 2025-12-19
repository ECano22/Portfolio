<h1>Data-Driven Command-Line RPG</h1>

<p>A feature-complete, text-based RPG that simulates turn-based combat. This project demonstrates the implementation of complex game mechanics, including dynamic difficulty scaling, procedural enemy generation, and a robust combat system, all within a command-line interface.</p>

<h2>Skills & Concepts Demonstrated</h2>

<h3>1. Data Structures & State Management</h3>
<ul>
    <li><strong>Parallel Collections:</strong> Managed game state using synchronized parallel lists (e.g., <code>name</code>, <code>strength</code>, <code>HP</code>) and dictionaries to track the attributes of multiple party members and enemies simultaneously.</li>
    <li><strong>Complex Dictionaries:</strong> Utilized nested dictionaries to define item attributes, spell costs, and status effect multipliers (e.g., <code>supportSpellStats</code> mapping spells to affected stats and duration).</li>
</ul>

<h3>2. Game Development Algorithms</h3>
<ul>
    <li><strong>Turn-Based Logic:</strong> Implemented a speed-based turn system where entity turn order is calculated dynamically at the start of battle by sorting participants based on their Speed stat.</li>
    <li><strong>Procedural Scaling:</strong> Designed a difficulty algorithm that scales enemy stats and levels relative to the player party's average level, ensuring balanced combat encounters throughout progression.</li>
    <li><strong>Combat Math:</strong> Engineered damage and hit-rate formulas that account for variables such as defense, evasion, elemental resistance, and active defense multipliers.</li>
</ul>

<h3>3. Data-Driven Design (File I/O)</h3>
<ul>
    <li><strong>External Configuration:</strong> Decoupled game data from logic by reading character growth rates, base stats, and enemy configurations from external <code>.txt</code> files (e.g., <code>Ally Growth Rates.txt</code>), allowing for balance adjustments without modifying the code.</li>
</ul>

<h3>4. Python Proficiency</h3>
<ul>
    <li><strong>String Manipulation & formatting:</strong> Utilized formatted strings to create a readable UI in the console, including visual health/mana bars using Unicode block characters (e.g., <code>\u2B1B</code> for full HP).</li>
</ul>

<h2>How It Works</h2>
<p>The game initializes by reading stats from external text files to populate the player's party. During combat, the engine calculates a turn order based on speed. On a player's turn, they can choose to Fight, utilize Magic (Attack or Support), Defend, or use Items. The enemy AI makes decisions based on its own health and stats, choosing effectively between attacking, healing, or fleeing.</p>
