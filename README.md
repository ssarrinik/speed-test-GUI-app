# ⌨️ Typing Speed Test App

## Overview
This project is a desktop-based Typing Speed Test application built using Python. It uses a modern GUI library (`ttkbootstrap`), an MVC (Model-View-Controller) architecture, and a database via SQLAlchemy to manage users, track their typing speeds (Words Per Minute), and store their achievements over time.

## Features
* **User Authentication:** Secure sign-in and registration system using `bcrypt` for password hashing.
* **Typing Speed Test:** A dynamic typing test that calculates your Words Per Minute (WPM) based on accuracy and speed.
* **Customizable Lengths:** Select different word subsets to challenge yourself.
* **Progress Tracking (Achievements):** View your past typing test results and speeds in a dedicated achievements board.
* **Modern UI:** Built with `ttkbootstrap` using the "cyborg" theme for a sleek, dark-mode aesthetic with custom color constants.

## Architecture
The codebase is strictly organized following the **MVC (Model-View-Controller)** design pattern:
* **Model (`Model/services.py`, `Model/Models.py`):** Handles the database connections, user creation, password verification, and achievement logging. Reads word banks using `pandas`.
* **View (`View/SignIn.py`, `View/gameui.py`, `View/constants.py`):** Defines the graphical layout, styles, and Tkinter widgets. Fully decoupled from business logic.
* **Controller (`Core/GameController.py`, `Core/SignInController.py`, `Core/BoardController.py`):** Acts as the bridge. It binds Tkinter events (like keystrokes or button clicks) to functions that query the Model and update the View.

## Tech Stack
* **Language:** Python 3
* **GUI Framework:** `tkinter` & `ttkbootstrap`
* **Database ORM:** `SQLAlchemy`
* **Data Processing:** `pandas` (for reading `words.csv`)
* **Security:** `bcrypt` (for password hashing)

## Setup and Installation

1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install pandas sqlalchemy bcrypt ttkbootstrap