import pyxel

from globals import GameMode
from patterns import patterns


class App:
    def __init__(self):
        self.config = {
            "title": "RhythmGame",
            "fps": 60,
            "resfile": "assets/sample.pyxres",
            "debug": False,
            "default_speed": 1.0,
        }

        pyxel.init(128, 128, fps=self.config["fps"], title=self.config["title"])
        if self.config["debug"]:
            pyxel.mouse(True)
        pyxel.load(self.config["resfile"])
        self.mode = GameMode.MENU
        self.notes = []
        self.note_count = 0
        self.note_processed = 0
        self.judge_color = 0
        self.judge_text = ""
        self.judge_time = -1
        self.score = 0
        self.combo = 0
        self.speed = self.config["default_speed"]
        self.life = self.max_life = 999
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.config["debug"]:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                print(pyxel.mouse_x, pyxel.mouse_y)

        if self.mode == GameMode.MENU:
            if pyxel.btnp(pyxel.KEY_1):
                self.life = self.max_life = 10
                self.set_mode(GameMode.EASY)
            if pyxel.btnp(pyxel.KEY_2):
                self.life = self.max_life = 10
                self.set_mode(GameMode.NORMAL)
            if pyxel.btnp(pyxel.KEY_3):
                self.life = self.max_life = 10
                self.set_mode(GameMode.HARD)

        # adjust speed
        if pyxel.btnp(pyxel.KEY_UP):
            self.speed = min(5.0, self.speed + 0.5)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.speed = max(0.5, self.speed - 0.5)

        if self.mode != GameMode.MENU:
            self.judge_notes()

    def judge_notes(self):
        judge_pos = 0
        if pyxel.btnp(pyxel.KEY_D):
            judge_pos += 1
        if pyxel.btnp(pyxel.KEY_F):
            judge_pos += 2
        if pyxel.btnp(pyxel.KEY_J):
            judge_pos += 4
        if pyxel.btnp(pyxel.KEY_K):
            judge_pos += 8

        judge_time = pyxel.frame_count - self.start_time
        for note in self.notes:
            timing = judge_time - note.time
            if timing < -9:
                break
            if note.active:
                if timing > 7:
                    # miss
                    note.active = False
                    self.life -= 1
                    # print("miss", self.life)
                    self.note_processed += 1
                    self.judge_text = "MISS"
                    self.judge_color = 8
                    self.judge_time = pyxel.frame_count
                    self.combo = 0
                elif 2**note.pos & judge_pos > 0:
                    judge_pos -= 2**note.pos
                    note.active = False
                    self.note_processed += 1
                    if -3 <= timing <= 3:
                        # perfect
                        # print("PERFECT")
                        self.score += 100
                        self.judge_text = "PERFECT"
                        self.judge_color = 11
                        self.judge_time = pyxel.frame_count
                        self.combo += 1
                    elif -5 <= timing <= 5:
                        # good
                        # print("GREAT")
                        self.score += 70
                        self.judge_text = "GREAT"
                        self.judge_color = 10
                        self.judge_time = pyxel.frame_count
                        self.combo += 1
                    elif -7 <= timing <= 7:
                        # good
                        # print("GOOD")
                        self.score += 30
                        self.judge_text = "GOOD"
                        self.judge_color = 9
                        self.judge_time = pyxel.frame_count
                        self.combo += 1
                    else:
                        # bad
                        # print("BAD")
                        self.life -= 1
                        self.judge_text = "BAD"
                        self.judge_color = 2
                        self.judge_time = pyxel.frame_count
                        self.combo = 0

    def draw(self):
        # set background
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 128, 128, 128, 0)

        # draw life
        if self.mode != GameMode.MENU:
            for i in range(self.max_life):
                healthy = self.life >= self.max_life - i
                pyxel.blt(
                    120 - i % 5 * 8,
                    i // 5 * 8,
                    0,
                    80 + (0 if healthy else 16),
                    48,
                    8,
                    8,
                    0,
                )

        if self.life > 0:
            self.do_draw()
        else:
            # display game over
            pyxel.rect(44, 58, 39, 9, 0)
            pyxel.rectb(43, 57, 41, 11, 8)
            pyxel.text(46, 60, "GAME OVER", 8)

    def do_draw(self):
        # draw menu or game ui
        if self.mode == GameMode.MENU:
            pyxel.text(
                70,
                48,
                "SELECT MODE\n\n1: EASY\n2: NORMAL\n3: HARD\n\nSPEED: "
                + str(self.speed),
                6,
            )
        else:
            self.draw_notes()
            self.draw_ui()
            # if pyxel.frame_count - self.start_time > self.length:
            if self.note_processed >= self.note_count:
                # cleared
                pyxel.rect(44, 58, 39, 9, 0)
                pyxel.rectb(43, 57, 41, 11, 11)
                pyxel.text(46, 60, "WELL DONE", 11)

        self.draw_keyeffect()
        pyxel.text(6, 117, "D   F   J   K", 7)

    def set_mode(self, mode):
        self.mode = mode
        self.start_time = pyxel.frame_count + 120
        print("starting mode", mode)
        self.notes = patterns[mode]
        self.note_count = len(self.notes)
        self.length = 960

    def draw_notes(self):
        for note in self.notes:
            if note.active:
                pyxel.blt(
                    note.pos * 16,
                    108
                    + (pyxel.frame_count - self.start_time - note.time) * self.speed,
                    0,
                    0,
                    132,
                    16,
                    4,
                    0,
                )

    def draw_ui(self):
        # difficulty and speed
        pyxel.text(67, 1, self.mode.value[:4], 6)
        pyxel.text(67, 8, "x" + str(self.speed), 6)

        # judge, combo
        judge_delay = pyxel.frame_count - self.judge_time
        if judge_delay < 45:
            pyxel.text(
                67,
                38 - (2 if judge_delay < 4 else 0),
                self.judge_text,
                self.judge_color,
            )
        pyxel.text(67, 46, str(self.combo).rjust(4) if self.combo > 0 else "", 6)

        # acc, score
        acc = 0.0
        if self.note_processed > 0:
            acc = round(self.score / self.note_processed, 2)
        pyxel.text(67, 112, "ACC   " + str(acc) + "%", 6)
        pyxel.text(67, 120, "SCORE " + str(self.score), 6)

    def draw_keyeffect(self):
        if pyxel.btn(pyxel.KEY_D):
            pyxel.blt(0, 112, 0, 16, 136, 16, 16, 0)
        else:
            pyxel.blt(0, 112, 0, 0, 136, 16, 16, 0)
        if pyxel.btn(pyxel.KEY_F):
            pyxel.blt(16, 112, 0, 16, 136, 16, 16, 0)
        else:
            pyxel.blt(16, 112, 0, 0, 136, 16, 16, 0)
        if pyxel.btn(pyxel.KEY_J):
            pyxel.blt(32, 112, 0, 16, 136, 16, 16, 0)
        else:
            pyxel.blt(32, 112, 0, 0, 136, 16, 16, 0)
        if pyxel.btn(pyxel.KEY_K):
            pyxel.blt(48, 112, 0, 16, 136, 16, 16, 0)
        else:
            pyxel.blt(48, 112, 0, 0, 136, 16, 16, 0)


App()
