import random


DOORS_ENUM = range(0, 3)


def thow_the_dice() -> int:
    return random.choice(DOORS_ENUM)


def guess(answer: int, insist: bool):
    first_guess = thow_the_dice()
    if insist:
        return first_guess

    for_guess = set(DOORS_ENUM) - set([first_guess])

    if first_guess != answer:
        wrong_answer = for_guess - set([answer])
        for_guess -= set([random.choice(list(wrong_answer))])
    else:
        for_guess -= set([answer])
    return random.choice(list(for_guess))




def iters(num: int, insist: bool) -> int:
    right_answer_count = 0
    for _ in range(num):
        answer = thow_the_dice()
        guessed = guess(answer, insist)
        if answer == guessed:
            right_answer_count += 1
    return right_answer_count


if __name__ == '__main__':
    iter_num = 1000000

    print('if insist the first guess')
    right_counts = iters(iter_num, True)
    print(f'ratio: {right_counts/iter_num}\n')

    print('if not insist the first guess')
    right_counts = iters(iter_num, False)
    print(f'ratio: {right_counts/iter_num}')
