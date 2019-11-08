for i in range(1, 11):
    with open('text{:0>2}.txt'.format(str(i)), 'w') as f:
        for s in range(10):
            f.write(str(i) + str(s) + 'test\n')
