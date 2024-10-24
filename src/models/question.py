#!/usr/bin/env python

from enum import Enum
import json


class ANS(Enum):
    INVALID = -1
    CORRECT = 0
    INCORRECT = 1
    OUT_OF_RANGE = 2


class Question():
    def __str__(self):
        return self.question

    def __repr__(self):
        return self.question

    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.answer = answer
        self.choices = choices

    def is_valid(self) -> bool:
        if len(self.question) == 0:
            return False
        if len(self.answer) == 0:
            return False
        if len(self.choices) != 4:
            return False
        return True

    def is_answer_valid(self, answer: int) -> ANS:
        if not self.is_valid():
            return ANS.INVALID
        if 0 < answer < len(self.answer):
            if answer == self.answer:
                return ANS.CORRECT
            else:
                return ANS.INCORRECT
        else:
            return ANS.OUT_OF_RANGE


# load the list of question from a json file
def load_question_list(file_path: str) -> list:
    question_list = list()

    with open(file_path, 'r') as file:
        data_list: list = json.load(file)
        for data in data_list:
            question = Question(
                data["question"],
                data["answer"],
                data["choices"]
            )
            if question.is_valid():
                question_list.append(question)

    return question_list
