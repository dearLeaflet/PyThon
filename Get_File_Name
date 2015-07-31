f = open("E:/SVHN/data/mat/test_name_lable.txt", "r")
fc = open("E:/SVHN/data/mat/test_lable.txt", "w")
while True:
    line = f.readline()
    if line:
        pass    # do something here
        line = line.strip()
        p = line.rfind('/')
        filename = line[p+1:]
        print "%s" % filename
        fc.write(filename)
        fc.write('\n')
    else:
        break
f.close()
fc.close()

