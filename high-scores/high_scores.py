def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    new_scores = sorted(scores, reverse=True)
    answer = []
    try:
        answer.append(new_scores[0])
        answer.append(new_scores[1])
        answer.append(new_scores[2])
    except IndexError:
        pass
    return answer
