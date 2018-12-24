def get_even_list(l):
    even_list = []
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
    return even_list