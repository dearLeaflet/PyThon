#!/usr/bin/env python
# coding=utf-8

'''
Lucas-Kanade tracker
====================

Lucas-Kanade sparse optical flow demo. Uses goodFeaturesToTrack
for track initialization and back-tracking for match verification
between frames.

Usage
-----
lk_track.py [<video_source>]


Keys
----
ESC - exit
'''

import numpy as np
import cv2
import video
from common import anorm2, draw_str
import math
from time import clock

lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict(maxCorners=500,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)


def point_product(box):
    point = []
    for i in range(int(box[0]), int(box[2]), 2):
        for j in range(int(box[1]), int(box[3]), 2):
            point.append([(i, j)])
    return point


"""
class App:
    def __init__(self, video_src):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = video.create_capture(video_src)
        self.frame_idx = 0

    def run(self):
        while True:
            ret, frame = self.cam.read()

            t = clock()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            vis = frame.copy()

            if len(self.tracks) > 0:
                img0, img1 = self.prev_gray, frame_gray
                # p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)
                p0 = np.float32(point_product(frame_gray))

                p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
                p0r, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
                for pp in p1:
                    print pp
                    cv2.circle(frame, (pp[0][0], pp[0][1]), 2, (0, 255, 0))
                cv2.imshow('tetet', frame)
                # cv2.waitKey(0)
                for p, ppp in zip(p0, p1):
                    print '222', p, ppp
                    cv2.line(frame, (int(p[0][0]), int(p[0][1])), (int(ppp[0][0]), int(ppp[0][1])), (0, 0, 255), 2)
            if self.frame_idx % self.detect_interval == 0:
                mask = np.zeros_like(frame_gray)
                mask[:] = 255
                for x, y in [np.int32(tr[-1]) for tr in self.tracks]:
                    cv2.circle(mask, (x, y), 5, 0, -1)
                p = cv2.goodFeaturesToTrack(frame_gray, mask = mask, **feature_params)

                # print 'good feature', p
                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        self.tracks.append([(x, y)])

            print clock() - t
            self.frame_idx += 1
            self.prev_gray = frame_gray
            cv2.imshow('lk_track', vis)

            ch = 0xFF & cv2.waitKey(1)
            if ch == 27:
                break


"""


def box_track(pre_box, p0, p1, p2):
    """
    :param pre_box: 跟踪窗口
    :param p0: 跟踪点
    :param p1: 跟踪到的点
    :param p2: 计算错误的反向跟踪点
    :return:跟踪到的窗口
    """
    dist = 0
    for i in p2 - p0:
        dist += math.sqrt(i[0][0] * i[0][0] + i[0][1] * i[0][1])
    dist /= 100

    count = 0
    count_sum = []
    for i, j in zip(p0, p2):
        if math.sqrt((i[0][0] - j[0][0]) * (i[0][0] - j[0][0]) + (i[0][1] - j[0][1]) * (i[0][1] - j[0][1])) < dist / 2:
            count_sum.append(count)
        count += 1
    print 'good point: ', len(count_sum)
    x = 0
    y = 0
    for i, j in zip(p1, p0):
        # print 'i[0]: ', (i[0][0] - j[0][0])
        x += (i[0][0] - j[0][0])
        y += (i[0][1] - j[0][1])
    # print 'x, y: ', x, y

    box_center_chage = [x / len(count_sum), y / len(count_sum)]
    print 'rect: ', box_center_chage
    box_center = [(pre_box[0] + pre_box[2]) / 2 + box_center_chage[0],
                   (pre_box[1] + pre_box[3]) / 2 + box_center_chage[1]]
    print box_center
    w = pre_box[2] - pre_box[0]
    h = pre_box[3] - pre_box[1]
    x = max(0, box_center[0] - w / 2)
    y = max(0, box_center[1] - h / 2)
    xx = x + w
    yy = y + h
    return [x, y, xx, yy]


class App:
    def __init__(self, video_src):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = video.create_capture(video_src)
        self.frame_idx = 0

    def run(self):
        ret, frame = self.cam.read()
        pre_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        count = 0
        box = [250, 150, 290, 190]
        while True:
            count += 1

            ret, frame = self.cam.read()
            ret, frame = self.cam.read()
            ret, frame = self.cam.read()
            t_start = clock()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            point_product_time = clock()
            p0 = np.float32(point_product(box))
            print 'point_product_time time: ', clock() - point_product_time
            img0, img1 = pre_frame_gray, frame_gray
            t_d = clock()
            p1, st, err = cv2.calcOpticalFlowPyrLK(pre_frame_gray, frame_gray, p0, None, **lk_params)
            p0r, st, err = cv2.calcOpticalFlowPyrLK(frame_gray, pre_frame_gray, p1, None, **lk_params)
            print 'calcOpticalFlowPyrLK: ', clock() - t_d
            cv2.waitKey(10)
            # print sum

            box = box_track(box, p0, p1, p0r)

            cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 2)

            #for p, ppp in zip(p0r, p0):
                # print '222', p, ppp
                #cv2.line(frame, (int(p[0][0]), int(p[0][1])), (int(ppp[0][0]), int(ppp[0][1])), (0, 255, 255), 2)
                # cv2.line(img1, (int(p[0][0]), int(p[0][1])), (int(ppp[0][0]), int(ppp[0][1])), (0, 0, 0), 2)

            cv2.imshow('tetet', frame)
            cv2.waitKey(10)
            pre_frame_gray = frame_gray
            print 'tracking time: ', clock() - t_start


def main():
    import sys

    try:
        video_src = sys.argv[1]
    except:
        video_src = 0

    print __doc__
    App(video_src).run()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
