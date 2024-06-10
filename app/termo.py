from dataclasses import dataclass
from enum import Enum, auto
from typing import Sequence, Tuple
import unicodedata


class Feedback(Enum):
    RIGHT_PLACE = auto()
    WRONG_PLACE = auto()
    WRONG = auto()


def freq(values):
    result = {}
    for it in values:
        result[it] = result.get(it, 0) + 1
    return result


@dataclass
class Result:
    win: bool
    feedback: Sequence[Tuple[str, Feedback]]


class InvalidAttempt(Exception):
    pass


@dataclass
class Termo:
    word: str
    valid_words: set
    normalized_word: str = None
    normalized_valid_words: set = None

    def __post_init__(self):
        self.normalized_word = self._remove_diacritics(self.word).lower()
        self.normalized_valid_words = set(map(
            lambda it: self._remove_diacritics(it).lower(),
            self.valid_words,
        ))

    def _remove_diacritics(self, text):
        return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))

    def _feedback(self, guess: str):
        if len(guess) != len(self.word):
            raise InvalidAttempt('Invalid attempt')
        for index, c in enumerate(guess):
            if c == self.normalized_word[index]:
                yield self.word[index], Feedback.RIGHT_PLACE
            elif c in self.normalized_word:
                yield c, Feedback.WRONG_PLACE
            else:
                yield c, Feedback.WRONG

    def feedback(self, guess: str):
        feedback = list(self._feedback(guess))

        word_freq = freq(self.word)
        feedback_freq = freq(map(
            lambda it: it[0],
            filter(lambda it: it[1] == Feedback.RIGHT_PLACE, feedback)
        ))
        for k, v in word_freq.items():
            if feedback_freq.get(k, 0) >= v:
                indexes = map(lambda it: it[0], filter(
                    lambda it: it[1][0] == k and it[1][1] == Feedback.WRONG_PLACE,
                    enumerate(feedback),
                ))
                for index in indexes:
                    feedback[index] = (feedback[index][0], Feedback.WRONG)
        return feedback

    def test(self, guess: str) -> Result:
        guess = self._remove_diacritics(guess).lower()
        if guess not in self.normalized_valid_words:
            raise InvalidAttempt()
        return Result(
            win=self.normalized_word == guess,
            feedback=self.feedback(guess),
        )
