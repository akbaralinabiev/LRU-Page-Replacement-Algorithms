def lru_algorithm(pages, frame_size):
    frame = []
    page_faults = 0
    for page in pages:
        if page not in frame:
            page_faults += 1
            if len(frame) == frame_size:
                frame.pop(0)
            frame.append(page)
        else:
            frame.remove(page)
            frame.append(page)
    return page_faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frame_size = 3

print("Number of page faults:", lru_algorithm(pages, frame_size))
