<!--
 * @Descripttion: 
 * @version: 
 * @Author: ErCHen
 * @Date: 2020-04-06 15:13:23
 * @LastEditTime: 2020-04-29 22:09:36
 -->

# SeeSort

## 介绍

一个基于PyQt5开发的排序过程可视化小程序，内置6种常见排序算法：

- 选择排序
- 插入排序
- 冒泡排序
- 堆排序
- 归并排序
- 快速排序
  
可设置排序数据规模，默认为50；每次排序随机生成序列，并根据元素值大小绘制直方图（直方图的大小根据数据规模自动调整），程序运行效果图如下：

![程序主页面](https://gitee.com/crxcoding/Image/raw/master/github/project_show/%E6%8E%92%E5%BA%8F%E8%BF%87%E7%A8%8B%E5%8F%AF%E8%A7%86%E5%8C%96.png)

![排序演示页面](https://gitee.com/crxcoding/Image/raw/master/github/project_show/%E6%8E%92%E5%BA%8F%E8%BF%87%E7%A8%8B.png)

## 实现思路

使用多线程技术，设置画图进程和排序进程，二者在信号量的控制下交替运行。排序每进行一步，便阻塞同时释放绘图信号，使得绘图进程根据当前数组的状态绘制直方图；等待绘制完毕便释放排序信号，使得排序进程得以继续。如此交替执行，直到排序完成。由于程序运行很快，所以看起来有动画的效果。
