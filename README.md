# ✖️⭕ TicTacToe_AI: Reinforcement Learning for Tic-Tac-Toe

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Description

This repository hosts a machine learning project focused on developing an AI agent to master the classic game of Tic-Tac-Toe. Utilizing a reinforcement learning approach, specifically Q-learning, the AI learns optimal strategies through self-play and experience. The project provides the core game logic, an interactive training environment via Jupyter Notebook, and mechanisms to save and load the AI's learned policies (Q-tables). This allows for experimentation, analysis, and playing against a trained intelligent agent.

## Features

*   **Classic Tic-Tac-Toe Game Logic**: A robust implementation of the standard 3x3 Tic-Tac-Toe game.
*   **Reinforcement Learning AI**: An intelligent agent capable of learning optimal moves using Q-learning.
*   **Interactive Training Environment**: `model.ipynb` provides an interactive platform using Jupyter Notebook for training the AI, visualizing progress, and experimenting with different parameters.
*   **Persistent Model Storage**: Trained AI models (Q-tables) are saved as `.npy` files within the `Q_Tables/` directory, allowing for easy reloading and deployment without retraining.
*   **Modular Design**: Separation of game logic (`ttt.py`) from the training and experimentation notebook (`model.ipynb`).

## Tech Stack

*   **Python**: The primary programming language for the game logic and AI implementation.
*   **Jupyter Notebook**: Used for interactive development, training, and analysis of the AI model.
*   **NumPy**: Essential for numerical operations, especially for handling Q-tables and state representations.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
*   **pip**: Python's package installer, usually comes with Python installation.

## Installation

Follow these steps to set up the project locally:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/winth03/TicTacToe_AI.git
    cd TicTacToe_AI
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install the required dependencies**:
    ```bash
    pip install numpy jupyter
    ```

## Usage

### Training the AI

To train the Tic-Tac-Toe AI and generate new Q-tables:

1.  **Start Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
2.  **Open `model.ipynb`**: Navigate to and open the `model.ipynb` file in your browser.
3.  **Run the cells**: Execute the cells in the notebook sequentially to train the AI. You can modify training parameters within the notebook.
4.  **Save Q-table**: The notebook will typically include steps to save the trained Q-table (e.g., `q1.npy`) into the `Q_Tables/` directory.

### Playing the Game

The `ttt.py` script likely contains the core game logic and can be extended to play against a trained AI.

1.  **Run the game script** (assuming `ttt.py` has a main execution block for playing):
    ```bash
    python ttt.py
    ```
    *Note: Further instructions for playing against the AI (e.g., loading `q1.npy` into `ttt.py`) would be detailed within `model.ipynb` or comments in `ttt.py`.*

## Project Structure

```
.
├── .gitattributes         # Git attributes configuration
├── .gitignore             # Specifies intentionally untracked files to ignore
├── Q_Tables/              # Directory to store trained Q-tables
│   └── q1.npy             # Example of a saved Q-table (NumPy array)
├── README.md              # This README file
├── model.ipynb            # Jupyter Notebook for AI training, experimentation, and analysis
└── ttt.py                 # Python script containing the core Tic-Tac-Toe game logic
```

*   **`Q_Tables/`**: This directory is dedicated to storing the learned Q-tables. These `.npy` files represent the AI's "brain" and can be loaded to deploy a pre-trained agent.
*   **`model.ipynb`**: This Jupyter Notebook is the heart of the AI development. It contains the code for the Q-learning algorithm, the training loop, potentially visualization, and saving/loading of Q-tables.
*   **`ttt.py`**: This file encapsulates the fundamental rules and mechanics of the Tic-Tac-Toe game. It typically handles game states, moves, win conditions, and might include basic human-vs-human or human-vs-random-AI gameplay.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/winth03/TicTacToe_AI/blob/main/LICENSE) file for details (if applicable, or simply state "MIT License" if no explicit file exists yet).

---

_This README was generated by an AI assistant based on the provided repository information._