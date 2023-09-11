from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def waitElement(self, xpath: str) -> WebElement:
    return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def get_text_squares(self, elems) -> [[str]]:
    squares: [[str]] = []
    row: [str] = []
    cnt: int = 0
    for elem in elems:
        cnt += 1
        texts = elem.find_elements(By.TAG_NAME, "tspan")
        phrase = " ".join([text.text.replace("\n", " ") for text in texts])
        row.append(phrase)
        if cnt == self.size:
            squares.append(row)
            cnt = 0
            row = []
    return squares


def get_card_details(self, elems) -> dict:
    """
    returns a dictionary of the url of the card and a 2d array of the phrases squares of the card
    """
    return {"url": self.driver.current_url, "squares": get_text_squares(self, elems)}


def get_squares_completion(self, card: dict) -> [[bool]]:
    """
    returns the squares of the card that are checked in a 2d bool array
    adds the completion 2d matrix value to the card for it to be printed to output
    """
    squares_completion: [[bool]] = [[0 for _ in range(5)] for _ in range(5)]
    # have to search for the free space, it won't neccesarilly be in the middle
    if self.size % 2 == 0 or (not self.free_space_in_middle):
        self.input_phrases.append(self.free_space)
    else:
        # or, in if it is odd or in the middle, just check that middle
        from math import ceil

        mid = ceil(self.size / 2)
        # i forgor its indexed from 0 💀
        squares_completion[mid][mid] = 1
    for i in range(self.size):
        for j in range(self.size):
            for input_phrase in self.input_phrases:
                if input_phrase.lower() in card["squares"][i][j].lower():
                    squares_completion[i][j] = 1
                    break

    card["completion"] = squares_completion
    return squares_completion


def check_bingo_row_collumn_diagonal(size, squares) -> bool:
    """
    regular ass bingo
    """
    # check bingo for elements in row, collumn or diagonal
    for i in range(size):
        if sum(squares[i]) == size:
            return True
        if sum([row[i] for row in squares]) == size:
            return True
        if sum([squares[i][i] for i in range(size)]) == size:
            return True
        if sum([squares[i][size - 1 - i] for i in range(size)]) == size:
            return True
    return False


def check_blackout(size, squares) -> bool:
    """
    full card
    """
    # check if all squares are filled
    for i in range(size):
        if sum(squares[i]) != size:
            return False
    return True


def check_peen(size, squares) -> bool:
    """
    shape of peen:
    """
    # check middle collumn and bottom row
    for i in range(size):
        sum = 0
        if squares[i][size // 2] == 1:
            sum += 1
        if squares[size - 1][i] == 1:
            sum += 1
    if sum == 2 * size - 1:
        return True


def check_3_in_6(size, squares) -> bool:
    """
    3x3 squares insode 6x6 grid
    """
    import numpy as np

    arr = np.array(squares)
    # check for any 3x3 squares of only true
    for i in range(size - 2):
        for j in range(size - 2):
            if np.all(arr[i : i + 3, j : j + 3]):
                return True
    return False


def check_loser(size, squares) -> bool:
    """
    shape of an L on her forehead
    """
    # check first collumn and last row
    cnt: int = 0
    for i in range(size):
        if squares[i][0]:
            cnt += 1
        if squares[size - 1][i]:
            cnt += 1
    if cnt == 2 * size - 1:
        return True
    return False


def check_bingos_and_write_to_output(self) -> None:
    # this assumes the viewport is already on that specific card, so function must be used right after finding new word on current page
    from typing import Callable

    check_bingo: Callable[[any], bool]

    match self.gamemode:
        case "normal":
            check_bingo = check_bingo_row_collumn_diagonal
        case "blackout":
            check_bingo = check_blackout
        case "peen":
            check_bingo = check_peen
        case "3in6":
            check_bingo = check_3_in_6
        case "loser":
            check_bingo = check_loser

    cards: [dict] = self.cards

    winning_cards: [dict] = []

    for card in cards:
        # the following will add new attribute to card dict
        if check_bingo(self.size, get_squares_completion(self, card)):
            # for better conciseness and readability
            del card["squares"]
            winning_cards.append(card)
            print("CONGRATS YOOO YOU GOT A BINGOO, check the output file for details")
            # currently only plays sound and works for macos but imma try to change it si maybe i also contribute to playsound library on github with python 10+ support
            # playsound()

    if len(winning_cards) > 0:
        print(winning_cards)
        final_wins = winning_cards
        previous_wins = read_from_output(self)
        if len(previous_wins) > 0:
            previous_urls = [card["url"] for card in previous_wins]
            new_wins = [
                card for card in winning_cards if card["url"] not in previous_urls
            ]
            new_wins.extend(previous_wins)
            final_wins = new_wins
        write_to_output(self, final_wins)


import json


def note_card(self, card: dict) -> None:
    """
    writes the link to the cards.txt file
    """
    with open(self.cards_path, "a+") as f:
        f.write(json.dumps(card))
        f.write("\n")


def write_to_output(self, cards: [dict]) -> None:
    with open(self.output_path, "w+") as f:
        f.write(json.dumps(cards))


def update_config(options: dict):
    with open("bingoconfig.json", "w+") as f:
        f.write(json.dumps(options))


def read_cards_file(self) -> [dict]:
    with open(self.cards_path, "r") as f:
        return [json.loads(line) for line in f.readlines()]


def read_from_config() -> dict:
    with open("bingoconfig.json", "r") as f:
        return json.loads(f.read())


def update_config_one_attr(attr: str, value: any) -> None:
    options = read_from_config()
    options[attr] = value
    update_config(options)


def read_from_output(self) -> [dict]:
    try:
        with open(self.output_path, "r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return []


def update_card_size(self, elems) -> None:
    if not self.gamemode == "3in6":
        from math import sqrt

        # automatically set the size of the card
        self.size = int(sqrt(len(elems)))
        update_config_one_attr("size", self.size)


def update_if_free_space_in_middle(self, card):
    from math import ceil

    # if the first one doesn't have it in the middle, change the settings to not look for it in the middle
    mid = ceil(self.size / 2)
    if not (self.free_space.lower() in card["squares"][mid][mid].lower()):
        print("WARNING: free space not found in middle of card, updating config")
        update_config_one_attr("free_space_in_middle", 0)
    else:
        print("free space found in middle of card, updating config")
        update_config_one_attr("free_space_in_middle", 1)


def create_card_return_card_details(self) -> dict:
    # go to the website
    self.driver.get(self.url)
    # create card
    waitElement(self, "/html/body/div[1]/div/form/button").click()
    # "OK" the rules
    waitElement(self, "/html/body/div[1]/p[2]/button").click()
    # check the free space in the middle
    elems = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "bingo-card-svg g g"))
    )

    update_card_size(self, elems)

    card_details = get_card_details(self, elems)
    note_card(self, card_details)
    return card_details


def init_driver(self):
    from selenium import webdriver

    match self.driver:
        case "chrome":
            if self.headless:
                opts = webdriver.ChromeOptions()
                opts.add_argument("--headless=new")
                self.driver = webdriver.Chrome(options=opts)
            else:
                self.driver = webdriver.Chrome()
        case "edge":
            if self.headless:
                opts = webdriver.EdgeOptions()
                opts.add_argument("--headless=new")
                self.driver = webdriver.Edge(options=opts)
            else:
                self.driver = webdriver.Edge()
        case "firefox":
            if self.headless:
                opts = webdriver.FirefoxOptions()
                opts.add_argument("--headless=new")
                self.driver = webdriver.Firefox(options=opts)
            else:
                self.driver = webdriver.Firefox()
        case "safari":
            self.driver = webdriver.Safari()
        case "ie":
            self.driver = webdriver.Ie()
        case _:
            self.driver = webdriver.Chrome()


# def playsound():
#     import sounddevice
#     import soundfile

#     filename = "bruh.wav"
#     data, fs = soundfile.read(filename, dtype="float32")
#     sounddevice.play(data, fs)
#     status = sounddevice.wait()
