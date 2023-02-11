def binary_truth_table(a, b, c, d):
    temp = 1
    print("A\tB\tC\tD\tA*B\tC*D\tA*B+C*D")
    for i in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:
                for l in [0, 1]:
                    x = (i and j)+(k and l)
                    if x >1:
                        x = temp
                    print("%d\t%d\t%d\t%d\t%d\t%d\t%d" % (i, j, k, l, i and j, k and l,x))
binary_truth_table(True, True, True, True)