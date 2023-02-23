import pygame
import sys
import random


class Question:
    def __init__(self, text, answer):
        """
            Initialize a Question instance.

            Args:
            - text (str): the text of the question.
            - answer (bool): the correct answer to the question (True or False).

            Attributes:
            - x (int): the x position of the question on the screen.
            - y (int): the y position of the question on the screen.
            - text (str): the text of the question.
            - splitted_text (list): a list of lines of text from the question.
            - lines_count (int): the number of lines in the question.
            - rect (pygame.Rect): the rectangle that contains the text of the question.
            - answer (bool): the correct answer to the question (True or False).
        """
        self.x = 145
        self.y = 37
        self.text = text
        self.splitted_text = str(self.text).split("\n")  # A list.
        self.lines_count = len(self.splitted_text)
        self.rect = pygame.Rect(self.x, self.y, 15 * len(self.splitted_text[0]), 40 * self.lines_count)
        self.answer = answer

    def blit_question(self, WIN):
        """
            Draw the question on the screen.

            Args:
            - WIN (pygame.Surface): the window surface to draw the question on.

            Returns:
            - None.
        """
        text_list = str(self.text).split("\n")
        self.rect = pygame.Rect(self.x, self.y, 15 * len(self.splitted_text[0]), 40 * self.lines_count)
        self.lines_count = len(text_list)
        font = pygame.font.SysFont(None, 40)
        WIN.blit(BRICKWALL_IMG, (0, 0))
        pygame.draw.rect(WIN, GREEN, true_rect)
        pygame.draw.rect(WIN, PINK, false_rect)
        WIN.blit(TRUE_IMG, (true_rect.x, true_rect.y))
        WIN.blit(FALSE_IMG, (false_rect.x, false_rect.y))
        pygame.draw.rect(WIN, WHITE, self.rect)
        for text in text_list:
            message = font.render(text, True, BLACK)
            WIN.blit(message, (self.x, self.y))
            self.y += 37

    def reset(self):
        """
            Reset the Question instance.
        """
        self.__init__(self.text, self.answer)


pygame.init()

# Images:
MENU_IMG = pygame.image.load("images/main.jpg")
ICON_IMG = pygame.image.load("images/brain.png")
PLAY_IMG = pygame.image.load("images/quiz.png")
QUIT_IMG = pygame.image.load("images/logout.png")
QUESTION_IMG = pygame.image.load("images/true-or-false.png")
GOLD_STAR_IMG = pygame.image.load("images/gold_star.png")
GRAY_STAR_IMG = pygame.image.load("images/gray_star.png")
GRAY_STAR2_IMG = pygame.image.load("images/gray_star2.png")
TOP5_IMG = pygame.image.load("images/Top_5.jpg")
TRUE_IMG = pygame.image.load("images/true.png")
FALSE_IMG = pygame.image.load("images/false.png")
BRICKWALL_IMG = pygame.image.load("images/BrickWall.jpg")
HEADER_IMG = pygame.image.load("images/header.jpg")
ABOUT_IMG = pygame.image.load("images/about.png")
BACK_IMG = pygame.image.load("images/back.png")

# Sounds:
CORRECT_SOUND = pygame.mixer.Sound("sounds/correct.wav")
INCORRECT_SOUND = pygame.mixer.Sound("sounds/incorrect.wav")
GAMEOVER_SOUND = pygame.mixer.Sound("sounds/gameover.wav")
GAMEPLAY_SOUND = pygame.mixer.Sound("sounds/jazz.wav")
GAMEPLAY_SOUND.set_volume(0.7)
# Display settings:
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia Game!")
pygame.display.set_icon(ICON_IMG)
textbox_width, textbox_height = 300, 50

# Colors:
GRAY = (100, 100, 100)
WHITE = (235, 235, 235)
BLACK = (0, 0, 0)
DEEP_BLUE = (29, 57, 101)
PINK = (209, 110, 111)
GREEN = (79, 187, 66)

STATUS = "Menu"
Got_Username = False
gameplay_sound_length = 6000
username = ""

# Rectangles:
play_rect = pygame.Rect(10, 330, 256, 256)
quit_rect = pygame.Rect(650, 450, 128, 128)
true_rect = pygame.Rect(0, 344, 256, 256)
false_rect = pygame.Rect(544, 344, 256, 256)
question_icon_rect = pygame.Rect(150, 120, 128, 128)
about_rect = pygame.Rect(10, 10, 64, 64)
back_rect = pygame.Rect(10, 10, 64, 64)

QUESTIONS = [
    Question("Abraham Lincoln was the\nfirst president of the USA.", False),
    Question("The Dead Sea is red.", False),
    Question("The Blue Whale is the  \nbiggest creature on Earth.", True),
    Question("Ice cream is made from milk.", True),
    Question("The names of the creators of\nthe game are Bar and Jonathan.", True),
    Question("World War II was ended in 1954", False),
    Question("Spiders have six legs", False),
    Question("Earth is flat.", False),
    Question("A human can survive without food for 3 months.", False),
]

about_text = "Hello you all, and welcome to our Trivia Game!\n" \
             "The game was firstly developed in 13.10.2022,\n" \
             "that's when we first started working on the game.\n" \
             "By we I mean Me and Bar Levi.\n" \
             "Bar is a student who is now learning how to develop computer games.\n" \
             "He also helps other younger students with their games and I am one of them.\n" \
             "The game itself is a trivia show in which you need to place the fact into the\n" \
             "correct answer.\n" \
             "Hope you enjoy :D "


def Quit():
    """
    Quits the Pygame module and exits the program.
    """
    pygame.quit()
    sys.exit(1)


def Answer(mouse_x, mouse_y, true_rect, false_rect, real_answer):
    """
    Checks whether the answer is correct or incorrect.

    Parameters:
    mouse_x (int): The x-coordinate of the mouse pointer.
    mouse_y (int): The y-coordinate of the mouse pointer.
    true_rect (pygame.Rect): The rectangle of the "True" button.
    false_rect (pygame.Rect): The rectangle of the "False" button.
    real_answer (bool): The correct answer to the question.

    Returns:
    bool or str: Returns True if the answer is correct, False if the answer is incorrect,
    and "Not an answer." if the user did not click on either button.
    """
    if pygame.Rect(true_rect).collidepoint(mouse_x, mouse_y):
        if real_answer == True:
            CORRECT_SOUND.play()
        if real_answer == False:
            INCORRECT_SOUND.play()
        return True
    if pygame.Rect(false_rect).collidepoint(mouse_x, mouse_y):
        if real_answer == False:
            CORRECT_SOUND.play()
        if real_answer == True:
            INCORRECT_SOUND.play()
        return False
    return "Not an answer."


def HandleSound():
    """
    Plays the gameplay sound, and stops it when it reaches the end.
    """
    global gameplay_sound_length
    if gameplay_sound_length == 0:
        GAMEPLAY_SOUND.stop()
        gameplay_sound_length = 6000
    if gameplay_sound_length == 6000:
        GAMEPLAY_SOUND.play()
    gameplay_sound_length -= 1


def starblit(WIN, answers, correct_answers):
    """
        Draws a star image on the game window for each answer, with a gold star for a correct answer, and a gray star for an incorrect one.

        Parameters:
        WIN (pygame.Surface): The game window surface.
        answers (int): The number of questions answered.
        correct_answers (list): A list of question numbers with a correct answer.
        """
    for number in range(1, answers + 1):
        if number in correct_answers:
            WIN.blit(GOLD_STAR_IMG, (0, 32 * number))
        else:
            WIN.blit(GRAY_STAR_IMG, (0, 32 * number))


def DisplayGame():
    """
    Displays the game window and runs the game until all questions are answered.
    """
    global STATUS, gameplay_sound_length
    for question in QUESTIONS:
        question.reset()
    answers = 0
    correct_answers = []
    drag_question = False
    font = pygame.font.SysFont(None, 40)
    TEMP_QUESTIONS = []
    for question in QUESTIONS:
        TEMP_QUESTIONS.append(question)
    questions_num = len(TEMP_QUESTIONS)
    while answers < questions_num:  # While the player hasn't answered all the questions.
        question_answered = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()  # sys is for check and operation
        index = random.randint(0, len(TEMP_QUESTIONS) - 1)
        TEMP_QUESTIONS[index].blit_question(WIN)
        starblit(WIN, answers, correct_answers)
        while not question_answered:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if drag_question:
                        gameplay_sound_length -= 1
                        x, y = pygame.mouse.get_pos()
                        answer = Answer(x, y, true_rect, false_rect, TEMP_QUESTIONS[index].answer)
                        if answer != "Not an answer.":
                            question_answered = True
                        drag_question = False
                    elif TEMP_QUESTIONS[index].rect.collidepoint(pygame.mouse.get_pos()):
                        drag_question = True
                if event.type == pygame.QUIT:
                    Quit()
            if drag_question:
                temp_x, temp_y = pygame.mouse.get_pos()
                temp_x -= TEMP_QUESTIONS[index].rect.width / 2
                temp_y -= TEMP_QUESTIONS[index].rect.height / 2 + 20
                TEMP_QUESTIONS[index].x, TEMP_QUESTIONS[index].y = temp_x, temp_y
                TEMP_QUESTIONS[index].blit_question(WIN)
            starblit(WIN, answers, correct_answers)
            pygame.display.update()

        answers += 1
        if TEMP_QUESTIONS[index].answer == answer:
            correct_answers.append(answers)  # מכניסים את מספר השאלה לרשימת השאלות בעלות תשובה נכונה

        TEMP_QUESTIONS.remove(TEMP_QUESTIONS[index])  # מוציאים את השאלה שעבדנו איתה מרשימת השאלות
        pygame.display.update()

    font = pygame.font.SysFont(None, 80)
    pygame.draw.rect(WIN, WHITE, pygame.Rect(0, 60, 800, 200))
    message = font.render(f"Goodbye {username}!", True, BLACK)
    WIN.blit(message, (200, 100))
    message = font.render(f"your score is {len(correct_answers)}/{questions_num}", True, BLACK)
    WIN.blit(message, (200, 170))
    pygame.display.update()
    pygame.time.wait(5000)
    STATUS = "Menu"


def GetDetails():
    """
    This function creates a window for the user to input their username. It listens for keyboard events and updates the window accordingly.
    It sets the global variables Got_Username and username. The function exits when the user submits their username
    by pressing the Enter key or closes the window.
    """
    global Got_Username, username
    # Setting a textbox for player's username input.
    textbox = pygame.Rect(WIDTH / 2 - textbox_width / 2, HEIGHT / 2 - textbox_height / 2, textbox_width, textbox_height)
    user_window = pygame.display.set_mode((WIDTH, HEIGHT))  # Creating a new window.
    while not Got_Username:
        user_window.fill(BLACK)  # Filling the window with a black color, for getting a black background.
        pygame.draw.rect(user_window, WHITE, textbox)  # Drawing the input textbox on the window.
        font = pygame.font.SysFont(None, 48)  # Changing writing font.
        text = font.render(username, True, BLACK)  # Saving the written username as "text" variable.
        #  Asking the player to type in his username:
        message = font.render("Please enter your name:", True, WHITE)
        user_window.blit(message, (textbox.x - 42, textbox.y - 60))
        user_window.blit(text, (textbox.x + 5, textbox.y + 10))  # Showing the written username on the window.
        font = pygame.font.SysFont(None, 24)
        message = font.render("(Press 'Enter' to submit)", True, WHITE)
        user_window.blit(message,
                         (textbox.x + 55, textbox.y + 70))  # Writing "Press 'Enter' to submit" under the textbox.
        pygame.display.update()
        for event in pygame.event.get():  # Getting the events which happen on the window while typing the username.
            if event.type == pygame.KEYDOWN:  # If there is a button pressing.
                if event.key == pygame.K_BACKSPACE:  # If the player is pressing the "Backspace" button.
                    username = username[0:-1]  # Removing the username's last character.
                elif event.key == pygame.K_RETURN:  # If the player is pressing the "Enter/Return" button.
                    if username != "" and username != "\t" and username != " ":  # If username isn't empty/"Space"/"Tab".
                        Got_Username = True
                else:
                    username += event.unicode  # Adding the typed characters to the "username" variable.
            if event.type == pygame.QUIT:  # If the player is pressing the "X" button on the window's top right corner.
                pygame.quit()  # Closing the window.
                exit(1)  # Closing the program.


def DisplayAbout():
    """
    This function displays the About screen. It sets the global variable STATUS to "Menu" if the user clicks the Back
    button or closes the window. It blits the background image, title, and text to the window. The function exits when
    the user clicks the Back button or closes the window.
    """
    global STATUS
    WIN.fill(BLACK)
    WIN.blit(BACK_IMG, (back_rect.x, back_rect.y))
    font = pygame.font.Font(None, 80)
    message = font.render("ABOUT", True, WHITE)  # WHY? - WE WANT TO SET THE TITLE TO WHITE COLOR
    WIN.blit(message, (300, 10))
    font = pygame.font.SysFont(None, 30)
    temp_y = 100
    for line in about_text.split("\n"):
        message = font.render(line, True, WHITE)  # WHY? - WE WANT TO SET THE TITLE TO WHITE COLOR
        WIN.blit(message, (0, temp_y))
        temp_y += 40
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_rect.collidepoint(pygame.mouse.get_pos()):
                STATUS = "Menu"
                MainMenu()


def DisplayMenu():
    """
    This function displays the Main Menu screen. It blits the background image, title, play button, quit button, and
    about button to the window. The function does not exit until the program is closed.
    """
    WIN.blit(HEADER_IMG, (0, 0))
    WIN.blit(PLAY_IMG, (play_rect.x, play_rect.y))
    WIN.blit(QUIT_IMG, (quit_rect.x, quit_rect.y))
    WIN.blit(ABOUT_IMG, (about_rect.x, about_rect.y))


def MainMenu():
    """
    This function handles the main game loop. It listens for events and updates the window accordingly. It sets the
    global variable STATUS based on the user's current screen. The function does not exit until the program is closed.
    """
    global STATUS
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(pygame.mouse.get_pos()):
                    STATUS = "Playing"
                if quit_rect.collidepoint(pygame.mouse.get_pos()):
                    Quit()
                if about_rect.collidepoint(pygame.mouse.get_pos()):
                    STATUS = "About"

        if STATUS == "Menu":
            HandleSound()
            DisplayMenu()

        if STATUS == "Playing":
            GAMEPLAY_SOUND.stop()
            GetDetails()
            DisplayGame()

        if STATUS == "About":
            HandleSound()
            DisplayAbout()

        pygame.display.update()


MainMenu()
