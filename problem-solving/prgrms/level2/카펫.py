def solution(brown, yellow):
    carpet = brown + yellow
    for width in range(carpet, 2, -1):
        if carpet % width == 0:
            height = carpet // width
            if yellow == (width - 2) * (height - 2):
                return [width, height]