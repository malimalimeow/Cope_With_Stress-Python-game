# Cope with Stress
#### Video Demo: <https://youtu.be/uo7xhitIFmE>
### Description:
Stress is something everyone experiences in daily life. Some types of stress are obvious, such as problems with clear solutions. Others are less visible, like work overload, strained relationships, or emotional burdens. These invisible stresses often affect both mental and physical well-being.

The purpose of this project is to reveal a user’s stress level through a short survey and provide different ways of stress relief. Depending on the results, the program will guide the user toward writing diary, playing simple relaxing games, or listening to calming music.

---

### Project Structure
This project contains three main files: **`project.py`**, **`click.py`**, and **`snake.py`**.

#### `project.py`
This is the main entry point of the program.
1. It begins by collecting the user’s name and current mood.
2. The user is then asked four questions from the *Perceived Stress Scale (PSS-4)* (Cohen et al., 1983) to identify their stress level: **High**, **Medium**, or **Low**.
3. Based on the result, the program will call one of the following functions:
   - **`low_open_file`**: Opens a text file where the user can write freely about stress-free feelings, or make a to-do list as motivation.
   - **`mid_game_`**: Randomly selects and launches one of the two mini-games (`click.py` or `snake.py`).
   - **`high_music`**: Opens a random relaxing music video from YouTube in the browser.

#### `click.py`
This is a mini-game created with **Pygame**.
- The goal is to click as many circles as possible within 30 seconds.
- The game generates circles in random positions, sizes, and colors.
- At the end, the program displays the user’s final score before returning to the main program.

#### `snake.py`
This is another mini-game created with **Pygame**.
- The player controls a snake using the arrow keys (**up, down, left, right**).
- The snake grows longer each time it eats the target “fruit.”
- The game ends when the snake hits the screen border or collides with itself.
- There is no time limit, so users can play at their own pace as a way of relaxation.

---

### Design Choices and Trade-offs
Originally, the plan was to use the 10-question version of the Perceived Stress Scale. However, this was found to be too long and potentially boring when displayed only as terminal text. The shorter **4-question PSS-4** was chosen instead, as it still provides meaningful insight into stress levels while keeping the experience simple and user-friendly.

---

### Potential Improvements and Enhancements
There are several possible future improvements for this project:
- **Graphical User Interface (GUI):** Making the program GUI-based (instead of text-based) would make it more accessible and visually appealing.
- **Data recording:** The program could generate a CSV file to record the user’s stress levels over time and visualize trends with charts.
- **More activities:** Additional games, music playlists, or guided breathing/meditation exercises could be included to provide more variety.
- **Expanded survey:** More questions could be added to improve the accuracy and representativeness of the stress-level assessment.

---

### Conclusion
This project demonstrates how a simple Python program can combine surveys, games, and multimedia resources to help users cope with stress. While currently text-based with basic Pygame mini-games, it lays a foundation for a more interactive and supportive tool in the future.

