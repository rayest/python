# coding=utf-8


class Ranks(ranks):

    def rank(self, score):
        if 0 < score < 60:
            return "bad"
        if 60 <= score < 70:
            return "及格"
        if 70 <= score < 80:
            return "良好"
        if 80 <= score < 90:
            return "很好"
        if 90 <= score < 100:
            return "优秀"
        if score == 100:
            return "最好"
        return "加错分了"
