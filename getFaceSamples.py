import cv2
count = 0
countno = 0

def insection_area(rect1, rect2):
    """
    :param rect1:x1, y1, width1, height1
    :param rect2:x2, y2, width2, height2
    :return:intersection_rate
    """
    rect1_points = []
    rect1_points.append([rect1[0], rect1[1]])
    rect1_points.append([rect1[0] + rect1[2] - 1, rect1[1]])
    rect1_points.append([rect1[0] + rect1[2] - 1, rect1[1] + rect1[3] - 1)
    rect1_points.append([rect1[0] + rect1[2] - 1, rect1[1] + rect1[3] - 1)

def roi_img(img, rect):
    height = img.shape[0]
    width = img.shape[1]
    cv2.imshow('img', img)

    global count, countno
    for i in range(4):
        rect[i] = int(rect[i])
    rect[2] = rect[2] + rect[0]
    rect[3] = rect[3] + rect[1]
    cv2.waitKey(10)
    # print img.shape
    x1 = max(0, int(rect[0]))
    y1 = max(0, int(rect[1]))
    x2 = min(width - 1, rect[2])
    y2 = min(height - 1, rect[3])

    img_roi = img[int(y1):int(y2), int(x1): int(x2)]
    cv2.imwrite('F:/face/20150817faceDetection/faceData/myC++TrainSample/faceSamples/'+str(count) + '.jpg', img_roi)
    count += 1
    area = (y2 - y1) * (x2 - x1)
    step = min((y2 - y1), (x2 - x1)) / 5
    x_sample = x2 - x1
    xx1 = 0
    yy1 = 0
    while x_sample < width:
        y_sample = y2 - y1
        print x_sample, width
        while y_sample < height:

            inter_height = min(y2, y_sample) - max(y1, yy1)
            inter_width = min(x2, x_sample) - max(xx1, x1)

            if max(xx1, x1) > min(x2, x_sample) or max(y1, yy1) > min(y2, y_sample):
                img_roi = img[int(yy1):int(y_sample), int(xx1):int(x_sample)]
                cv2.imshow('test', img_roi)
                cv2.waitKey(10)
                cv2.imwrite('F:/face/20150817faceDetection/faceData/myC++TrainSample/noFaceSamples/'+str(countno) + '.jpg', img_roi)
                countno += 1
                print '00'
            elif inter_height * inter_width / ((y_sample - yy1) * (x_sample - xx1) + area - inter_height * inter_width) < 0.2:
                img_roi = img[int(yy1):int(y_sample), int(xx1):int(x_sample)]
                cv2.imwrite('F:/face/20150817faceDetection/faceData/myC++TrainSample/noFaceSamples/'+str(countno) + '.jpg', img_roi)
                countno += 1
                print '0.2'
            elif inter_height * inter_width / ((y_sample - yy1) * (x_sample - xx1) + area - inter_height * inter_width) > 0.5:
                img_roi = img[int(yy1):int(y_sample), int(xx1):int(x_sample)]
                cv2.imwrite('F:/face/20150817faceDetection/faceData/myC++TrainSample/faceSamples/'+str(count) + '.jpg', img_roi)
                count += 1
                print '0.5'
            yy1 += step
            y_sample += step
        xx1 += step
        x_sample += step


def get_face_samples():
    file = open('F:/face/20150817faceDetection/faceData/myC++TrainSample/face_rect.txt', 'r')
    for img_name in file.readlines():
        img_name_line = img_name.strip()
        img_name_list = img_name_line.split('\t')
        img_name = img_name_list[1].split('/')
        # print img_name_list
        img = cv2.imread('F:/face/20150817faceDetection/faceData/ALFWi/' + img_name[1] + '/' + img_name[2])
        true_sample = img_name_list[2:]
        roi_img(img, true_sample)
        '''
        cv2.imshow('test', img)
        cv2.waitKey(10)
        '''


if __name__ == '__main__':
    get_face_samples()
