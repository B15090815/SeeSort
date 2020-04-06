import math
import threading
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsLineItem, QWidget

from showGround import Ui_widget
from util import Signal, shuffle


class showGroundOp(QWidget, Ui_widget):
    sort_map = {
        0: '选择排序',
        1: '插入排序',
        2: '冒泡排序',
        3: '堆排序',
        4: '归并排序',
        5: '快速排序'
    }

    def __init__(self, sort_id: int, sort_range=50, plot_speed=0.2):
        QWidget.__init__(self)
        Ui_widget.__init__(self)
        # 设置ui样式
        self.setupUi(self)
        # 创建场景
        self.scene = QGraphicsScene(self)
        # 计算场景长宽并设置
        self.w = self.show_place.width() - 30
        self.h = self.show_place.height() - 20
        self.scene.setSceneRect(0, 0, self.w, self.h)
        self.show_place.setScene(self.scene)

        # 自定义绘画信号
        self.plot_signal = Signal()
        # 定义排序信号量，控制排序过程
        self.sort_semaphore = threading.Semaphore(1)
        # 绘制速度
        self.plot_speed = plot_speed

        # 排序线程
        self.plot_thread = None

        self.stop_thread = False
        # 排序的范围
        self.sort_range = sort_range
        self.data = None
        # key[0]当前主元，key[1]保存与之比较的元素
        self.key = [-1, -1]

        self.choose_sort = sort_id
        self.sort_name.setText(self.sort_map[sort_id])

        self.start.clicked.connect(self.click_start)
        self.stop.clicked.connect(self.stop_sort)
        self.plot_signal.moved_on.connect(self.draw_thread)
        self.plot_signal.plot_last_time.connect(self.draw)

    def draw_line(self):
        line_pen = QPen(Qt.black, 2)
        item = QGraphicsLineItem(0, self.h, self.w, self.h)
        item.setPen(line_pen)
        self.scene.addItem(item)

        item = QGraphicsLineItem(self.w, 0, self.w, self.h)
        item.setPen(line_pen)
        self.scene.addItem(item)

    def draw(self):
        self.scene.clear()
        N = len(self.data)
        span = self.w // N
        width = math.floor(span * 0.8)
        margin = max(self.w - N * span - 4, 0)
        brush = [QBrush(Qt.red), QBrush(Qt.blue)]
        self.draw_line()
        for i in range(N):
            x = i * span + margin
            height = math.floor(self.data[i] / N * self.h)
            y = self.h - height
            item = QGraphicsRectItem(x, y, width, height)

            if i == self.key[0]:
                item.setBrush(brush[0])
            elif i == self.key[1]:
                item.setBrush(brush[1])
            self.scene.addItem(item)

    def click_start(self):
        if self.plot_thread is None or not self.plot_thread.is_alive():
            self.stop_thread = False
            self.data = shuffle(list(range(1, self.sort_range + 1)))
            self.plot_thread = None
            if self.choose_sort == 0:
                self.plot_thread = threading.Thread(target=self.selectSort)
            elif self.choose_sort == 1:
                self.plot_thread = threading.Thread(target=self.insertSort)
            elif self.choose_sort == 2:
                self.plot_thread = threading.Thread(target=self.bubbleSort)
            elif self.choose_sort == 3:
                self.plot_thread = threading.Thread(target=self.heapSort)
            elif self.choose_sort == 4:
                self.plot_thread = threading.Thread(target=self.mergeSort)
            elif self.choose_sort == 5:
                self.plot_thread = threading.Thread(target=self.quickSort)

            self.plot_thread.daemon = True
            self.plot_thread.start()

    def draw_thread(self):
        self.draw()
        self.sort_semaphore.release()

    def stop_sort(self):
        self.stop_thread = True

    def swap(self, i: int, j: int):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def selectSort(self):
        N = len(self.data)
        for i in range(N):
            if self.stop_thread:
                return
            k = i
            self.sort_semaphore.acquire()
            for j in range(i + 1, N):
                if self.data[k] > self.data[j]:
                    k = j

            self.key[0] = k
            self.key[1] = -1

            self.plot_signal.moved_on.emit()
            time.sleep(self.plot_speed)

            self.swap(k, i)

        self.plot_signal.plot_last_time.emit()

    def bubbleSort(self):
        N = len(self.data)
        flag = False
        for i in range(N):
            if flag:
                break
            flag = True

            for j in range(N - i - 1):
                if self.stop_thread:
                    return

                if self.data[j] > self.data[j + 1]:
                    flag = False
                    self.sort_semaphore.acquire()
                    self.key[0] = j
                    self.key[1] = j + 1
                    self.plot_signal.moved_on.emit()
                    time.sleep(self.plot_speed)

                    self.swap(j, j + 1)

        self.plot_signal.plot_last_time.emit()

    def insertSort(self):
        N = len(self.data)
        for i in range(1, N):
            for j in range(i, 0, -1):
                if self.stop_thread:
                    return

                if self.data[j] < self.data[j - 1]:
                    self.sort_semaphore.acquire()
                    self.key[0] = j
                    self.key[1] = -1
                    self.plot_signal.moved_on.emit()
                    time.sleep(self.plot_speed)

                    self.swap(j - 1, j)

        self.plot_signal.plot_last_time.emit()

    def merge(self, l1: int, r1: int, l2: int, r2: int):
        temp = []
        i = l1
        j = l2

        while i <= r1 and j <= r2:
            if self.data[i] < self.data[j]:
                temp.append(self.data[i])
                i += 1
            else:
                temp.append(self.data[j])
                j += 1

        while i <= r1:
            temp.append(self.data[i])
            i += 1

        while j <= r2:
            temp.append(self.data[j])
            j += 1

        self.sort_semaphore.acquire()
        i = l1
        j = 0
        while j < len(temp):
            self.data[i] = temp[j]
            i += 1
            j += 1

        self.key[0] = r1
        self.key[1] = r2
        self.plot_signal.moved_on.emit()
        time.sleep(self.plot_speed)

    def innerMergeSort(self, left: int, right: int):
        if left < right:
            mid = (right + left) >> 1
            self.innerMergeSort(left, mid)
            self.innerMergeSort(mid + 1, right)
            self.merge(left, mid, mid + 1, right)

    def mergeSort(self):
        self.innerMergeSort(0, len(self.data) - 1)
        self.plot_signal.plot_last_time.emit()

    def adjustHeap(self, root: int, N: int):
        k = root * 2 - 1
        while k < N:
            if k + 1 < N and self.data[k] < self.data[k + 1]:
                k += 1

            root -= 1
            if self.data[root] < self.data[k]:

                self.sort_semaphore.acquire()
                self.key[0] = root
                self.key[1] = k
                self.plot_signal.moved_on.emit()
                time.sleep(self.plot_speed)
                self.swap(root, k)
                root = k + 1
                k = root * 2 - 1
            else:
                break

    def buildHeap(self):
        N = len(self.data)
        i = N >> 1

        while i > 0:
            self.adjustHeap(i, N)
            i -= 1

    def heapSort(self):
        self.buildHeap()
        k = len(self.data) - 1
        while k > 0:
            self.swap(0, k)
            self.adjustHeap(1, k)
            k -= 1

    def partion(self, left: int, right: int):
        k = self.data[left]
        i = left + 1
        j = right

        while True:
            while self.data[i] < k and i < right:
                i += 1

            while self.data[j] > k:
                j -= 1

            if i >= j:
                break

            self.swap(i, j)

        self.sort_semaphore.acquire()
        self.key[0] = left
        self.key[1] = j
        self.plot_signal.moved_on.emit()
        time.sleep(self.plot_speed)

        self.data[left] = self.data[j]
        self.data[j] = k
        return j

    def InnerquickSort(self, p: int, r: int):
        if p < r:
            mid = self.partion(p, r)
            self.InnerquickSort(p, mid - 1)
            self.InnerquickSort(mid + 1, r)

    def quickSort(self):
        self.InnerquickSort(0, len(self.data) - 1)
