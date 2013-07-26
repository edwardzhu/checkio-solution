def checkio(data):
    counter = 0
    for s in data:
        if s == 'A' or s=='a':
            counter += 1
    return counter

if __name__=='__main__':
    assert checkio('This task is awesome!') == 2, "Test1"
    assert checkio('All tasks are awesome and interesting') == 4, "Test2"
