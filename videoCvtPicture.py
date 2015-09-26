# coding=utf-8
import cv2
import os


def read_txt_file_test(file_path):
    file_read = open(file_path, 'r')
    for img_name in file_read.readlines():
        print img_name, len(img_name)


def get_video_img(root_path, child_file, file_name):
    """
    :param root_path: 根目录
    :param childfile: 创建的子目录
    :param file_name: 信息写入文件
    :return: void
    """
    make_file_name = root_path + '/' + child_file
    if os.path.exists(make_file_name):
        # isfile
        pass
    else:
        os.mkdir(make_file_name)
    # file_write = open(make_file_name + '/' + file_name, 'w')
    file_write = open(make_file_name + '/' + file_name, 'w')
    count = 0
    cap = cv2.VideoCapture(0)
    frame_rate = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    while True:
        for i in range(int(frame_rate / 5)):
            cap.read()
        re, img = cap.read()
        cv2.imshow('img', img)
        cv2.waitKey(10)
        if re:
            img_name = child_file + '_' + str(count) + '.jpg'
            cv2.imwrite(make_file_name + '/' + img_name, img)
            file_write.writelines(img_name + '\n')
            count += 1
            '''
            if count == 100:
                break
                '''
        else:
            print 'stop'
            break
    file_write.close()


def read_all_files(img_path, file_name):
    """
    :param img_path: 图片所在目录
    :param file_name: 信息写入文件
    :return: void
    """
    # img_name_file = open('F:/face/20150817faceDetection/faceData/Single face dataset/imgName.txt', 'w')
    img_name_file = open(file_name, 'w')
    for rt, dirs, files in os.walk(img_path):
        # print rt, dirs
        for img_name in files:
            img_name_file.writelines(img_name + '\n')
    img_name_file.close()


def videe_cvt_img():
    """"
    :return: void
    """
    video_path = \
        ['F:/face/20150817faceDetection/faceData/Single face dataset/motinas_emilio_webcam/motinas_emilio_webcam.avi',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_emilio_webcam_turning/motinas_emilio_webcam_turning.avi',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_multi_face_fast/motinas_multi_face_fast.avi',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_multi_face_frontal/motinas_multi_face_frontal.avi',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_multi_face_turning/motinas_multi_face_turning.avi',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_nikola_dark/motinas_nikola_dark.avi',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_toni/motinas_toni.avi',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_toni_change_ill/motinas_toni_change_ill.avi']

    img_path = \
        ['F:/face/20150817faceDetection/faceData/Single face dataset/motinas_emilio_webcam/',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_emilio_webcam_turning/',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_multi_face_fast/',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_multi_face_frontal/',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_multi_face_turning/',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_nikola_dark/',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_toni/',
         'F:/face/20150817faceDetection/faceData/Single face dataset/motinas_toni_change_ill/']
    for path, img_file_path in zip(video_path, img_path):
        file_name = path.split('/')
        img_file_name = file_name[len(file_name) - 2]
        cap = cv2.VideoCapture(path)
        video_frame_rate = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        count = 0
        while True:
            for i in range((int(video_frame_rate)) / 2):
                re, img = cap.read()
            if re:
                cv2.imwrite('F:/face/20150817faceDetection/faceData/Single face dataset/videoImg/'
                            + img_file_name + str(count) + '.jpg', img)
                count += 1
                cv2.imshow('test', img)
                cv2.waitKey(10)
            else:
                print path + 'video is ok!'
                break
                # read_all_files()


def file_iterator(root, file2save):
    """

    :root:根目录
    :file2save:读取的文件保存在哪里

    """
    img_count = 0
    file_wtire = open(file2save, "w")
    for root_path, chile_file, img1 in os.walk(root):
        '''
        file_lists = str(img).split('.')
        if file_lists[-1] == ['jpg']:
            str(img).strip('\t' or '\n')
        '''
        for imgpath in img1:
            implement_path = str(root) + '/' + str(imgpath)
            file_wtire.writelines(str(imgpath) + '\n')

            img = cv2.imread(implement_path)

            size = (int(img.shape[1] * 0.444), int(img.shape[0] * 0.444))
            img_resize = cv2.resize(img, size)
            resize_img_path = 'E:/face/train/1_1_04_0/prob/side_face_resized/' + str(imgpath).strip()
            print resize_img_path
            cv2.imwrite(resize_img_path, img_resize)
            print resize_img_path
            # cv2.imwrite(resize_img_path, img_resize)
            cv2.imshow('just_show', img_resize)
            cv2.waitKey(10)
            # cv2.imwrite(file2save + '/' + str(img), img)
    file_wtire.close()
    file_write1 = open(file2save, "r")
    for i in file_write1.readlines():
        img_count += 1
        print i, img_count


if __name__ == '__main__':
    '''
    path = []
    txt_file = []
    path.append('F:/face/20150817faceDetection/faceData/myCapture')
    txt_file.append('F:/face/20150817faceDetection/faceData/myCapture/file_name_lists.txt')
    read_all_files(path[0], txt_file[0])
    '''

    # get_video_img('F:/face/20150817faceDetection/faceData', 'distance_set1', 'distance_set_img_name1.txt')
    # read_txt_file_test('F:/face/20150817faceDetection/faceData/just_test1/test.txt')

    # file_iterator('F:/face/20150817faceDetection/faceData/AFW/testimages', 'F:/face/20150817faceDetection/faceData/AFW/AFW.txt')

    # read_all_files('/media/wjy/Document/face/20150817faceDetection/faceData/Single face dataset/videoImg', '/media/wjy/Document/face/20150817faceDetection/faceData/Single face dataset/imgName.txt')
    file_iterator('E:/face/train/1_1_04_0/prob/dongnanmeneast_15_1920x1080_30',
                  'E:/face/train/1_1_04_0/prob/dongnanmeneast_15_1920x1080_30/side_face.txt')
