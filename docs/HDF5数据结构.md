---
title: HDF5数据结构
author: MorningTZH
uuid: 83507150-33f4-4c97-a003-976abbaef6cc
date: 2019-08-24T11:13:21+08:00
categories: 
  - 数据结构
tags: 
  - 数据结构
  - 持久化
  - HDF5
description: HDF5数据结构
---

# HDF5数据结构

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [HDF5数据结构](#hdf5数据结构)
  - [1. HDF5基础知识](#1-hdf5基础知识)
  - [2. 标的数据结构](#2-标的数据结构)

<!-- /code_chunk_output -->

## 1. HDF5基础知识

HDF5 是一种分层结构的数据库文件，其包含两种主要结构：

- HDF5 group：分组结构包含零个或多个组或数据集的实例，以及支持元数据(metadata)；
- HDF5 dataset：数据元素的多维数组，以及支持元数据；

具体可参考[HDF5简介](https://blog.csdn.net/renyhui/article/details/77735314)。

## 2. 标的数据结构

- root
  - securities
  - bars
  - finance


