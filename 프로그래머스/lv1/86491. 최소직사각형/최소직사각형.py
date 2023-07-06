def solution(sizes):
    mw, mh = 0, 0
    
    for size in sizes:
        w, h = sorted(size)
        mw, mh = max(mw, w), max(mh, h)
    
    return mw * mh