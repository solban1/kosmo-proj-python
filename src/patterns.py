from globals import GameMode
from note import Note


def o___(time):
    return Note(time, 0)


def _o__(time):
    return Note(time, 1)


def __o_(time):
    return Note(time, 2)


def ___o(time):
    return Note(time, 3)


patterns = {
    GameMode.EASY: (
        # basic
        o___(0),
        o___(60),
        ___o(120),
        ___o(150),
        ___o(180),
        o___(240),
        _o__(270),
        __o_(300),
        ___o(330),
        o___(360),
        o___(390),
        o___(420),
        # multi
        o___(480),
        ___o(480),
        o___(540),
        ___o(540),
        _o__(600),
        __o_(600),
        _o__(630),
        __o_(630),
        _o__(660),
        __o_(660),
        # advanced
        o___(720),
        _o__(750),
        __o_(780),
        _o__(810),
        o___(840),
        ___o(840),
        _o__(870),
        __o_(885),
        _o__(900),
    ),
    GameMode.NORMAL: (
        # v1
        o___(0),
        o___(7 * 4),
        o___(7 * 6),
        o___(7 * 8),
        ___o(7 * 16),
        ___o(7 * 20),
        ___o(7 * 22),
        ___o(7 * 24),
        o___(7 * 32),
        _o__(7 * 34),
        __o_(7 * 36),
        _o__(7 * 38),
        ___o(7 * 40),
        __o_(7 * 42),
        _o__(7 * 44),
        __o_(7 * 46),
        o___(7 * 48),
        _o__(7 * 52),
        __o_(7 * 52),
        _o__(7 * 54),
        __o_(7 * 54),
        _o__(7 * 56),
        __o_(7 * 56),
        # v2
        o___(7 * 64),
        __o_(7 * 64),
        o___(7 * 66),
        __o_(7 * 66),
        o___(7 * 68),
        __o_(7 * 68),
        _o__(7 * 72),
        ___o(7 * 72),
        _o__(7 * 74),
        ___o(7 * 74),
        _o__(7 * 76),
        ___o(7 * 76),
        _o__(7 * 80),
        __o_(7 * 80),
        _o__(7 * 84),
        ___o(7 * 84),
        _o__(7 * 88),
        __o_(7 * 88),
        # v3
        o___(7 * 96),
        ___o(7 * 96),
        _o__(7 * 98),
        o___(7 * 100),
        ___o(7 * 100),
        o___(7 * 104),
        ___o(7 * 104),
        __o_(7 * 106),
        o___(7 * 108),
        ___o(7 * 108),
        _o__(7 * 112),
        __o_(7 * 112),
        o___(7 * 116),
        ___o(7 * 116),
        _o__(7 * 117),
        __o_(7 * 118),
        _o__(7 * 119),
        o___(7 * 120),
        ___o(7 * 120),
    ),
    GameMode.HARD: (
        # v1
        o___(6 * 0),
        _o__(6 * 1),
        __o_(6 * 2),
        ___o(6 * 3),
        o___(6 * 4),
        _o__(6 * 5),
        __o_(6 * 6),
        ___o(6 * 7),
        o___(6 * 8),
        o___(6 * 12),
        ___o(6 * 16),
        __o_(6 * 17),
        _o__(6 * 18),
        o___(6 * 19),
        ___o(6 * 20),
        __o_(6 * 21),
        _o__(6 * 22),
        o___(6 * 23),
        ___o(6 * 24),
        ___o(6 * 28),
        # v2
        o___(6 * 32),
        ___o(6 * 32),
        _o__(6 * 33),
        __o_(6 * 34),
        _o__(6 * 35),
        o___(6 * 36),
        ___o(6 * 36),
        __o_(6 * 37),
        _o__(6 * 38),
        __o_(6 * 39),
        o___(6 * 40),
        ___o(6 * 40),
        o___(6 * 41),
        _o__(6 * 42),
        __o_(6 * 43),
        o___(6 * 44),
        __o_(6 * 44),
        ___o(6 * 45),
        __o_(6 * 46),
        _o__(6 * 47),
        o___(6 * 48),
        __o_(6 * 48),
        ___o(6 * 48),
        _o__(6 * 50),
        o___(6 * 52),
        __o_(6 * 52),
        _o__(6 * 53),
        __o_(6 * 54),
        _o__(6 * 55),
        __o_(6 * 56),
        ___o(6 * 56),
        # v3
        o___(6 * 64),
        __o_(6 * 64),
        _o__(6 * 65),
        ___o(6 * 65),
        o___(6 * 66),
        __o_(6 * 66),
        _o__(6 * 67),
        ___o(6 * 67),
        o___(6 * 68),
        __o_(6 * 68),
        ___o(6 * 70),
        _o__(6 * 72),
        __o_(6 * 72),
        o___(6 * 73),
        ___o(6 * 73),
        _o__(6 * 74),
        __o_(6 * 74),
        o___(6 * 75),
        ___o(6 * 75),
        _o__(6 * 76),
        __o_(6 * 76),
        # final
        o___(6 * 80),
        _o__(6 * 80),
        ___o(6 * 81),
        o___(6 * 82),
        _o__(6 * 82),
        __o_(6 * 83),
        _o__(6 * 84),
        ___o(6 * 84),
        __o_(6 * 85),
        o___(6 * 86),
        ___o(6 * 86),
        o___(6 * 87),
        ___o(6 * 87),
        o___(6 * 88),
        ___o(6 * 88),
    ),
}