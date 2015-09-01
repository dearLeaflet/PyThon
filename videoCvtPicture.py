# coding=utf-8
import cv2
import os
def read_all_files():
    """

    :rtype :遍历目录下文件
    """
    img_name_file = open('F:/face/20150817faceDetection/faceData/Single face dataset/imgName.txt', 'w')
    for rt, dirs, files in os.walk('F:/face/20150817faceDetection/faceData/Single face dataset/videoImg'):
        # print rt, dirs
        for img_name in files:
            img_name_file.write(img_name + '\n')
    img_name_file.close()


if __name__ == '__main__':
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
            for i in range((int(video_frame_rate))/2):
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
        read_all_files()
