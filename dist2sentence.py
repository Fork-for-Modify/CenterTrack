#!/usr/bin/env python
# coding: utf-8
# Filepath:	 util.py

# Reference:

# Created: 	 2021-07-27_22:26:47
# Modified:	 2021-08-23_21:18:12
# Author:  	 Zhihong Zhang [https://github.com/dawnlh]
# Contact: 	 z_zhi_hong@163.com
# Copyright (c) 2021 Zhihong Zhang

import os
import json
import numpy as np
import argparse


def getObjInfoFromJson(file_path, save_path=None):
    """
    get object infomation from given file

    Parameters
    ----------
    file_path : string 
        file path
    save_path : string 
        saving path
                
    Return
    ----------
    Info : {1: {'class': int, 
                'frame_idx': N*1 int 
                'loc': N*3 float
                'dim': N*3 float
                'dep': N*1 float}
            2:,{}
            ...} 
    """

    # get tracking result json file
    with open(file_path) as f:
        f_json = json.load(f)

    # extract object information
    objInfo = dict()
    frame_num = len(f_json)
    for k in range(frame_num):
        frame_i = f_json[f'{k+1}']
        for obj_i in frame_i:
            if obj_i['tracking_id'] in list(objInfo.keys()):
                objInfo[obj_i['tracking_id']]['frame_idx'].append(k+1)
                objInfo[obj_i['tracking_id']]['loc'].append(obj_i['loc'])
                objInfo[obj_i['tracking_id']]['dim'].append(obj_i['dim'])
                objInfo[obj_i['tracking_id']]['dep'].append(obj_i['dep'][0])
            else:
                newObj = {'class': obj_i['class'],
                          'frame_idx': [k+1],
                          'loc': [obj_i['loc']],
                          'dim': [obj_i['dim']],
                          'dep': obj_i['dep']}
                objInfo[obj_i['tracking_id']] = newObj

    # save info
    if save_path:
        with open(save_path, 'w') as f:
            json.dump(objInfo, f)

    return objInfo


def filterObjInfo(objInfo):
    """
    filter out noisy object info

    Args:
        objInfo (struct): object information
    """

    # filter params
    keep_id = [2, 5]  # kept id
    keep_class = [1, 2, 3, 4, 5, 6, 7, 8]  # kept class
    min_obj_area = 400  # minimal kept object (pixel^2) #zzh
    # consecutive_visible_frame = 10
    # disappear_times = 4

    for k in list(objInfo.keys()):
        if k not in keep_id or objInfo[k]['class'] not in keep_class:
            del(objInfo[k])
    return objInfo


def genSentenceFromInfo(objInfo):
    """
    generate description sentence from input infomation

    Parameters
    ----------
    objInfo : struct list, 
            {'id': {'class':class1_string, 'dep':dep_float, 'speed',...},...} 
        information about the video tracking result
    """

    # preset info
    CATS = ['Car', 'Truck', 'Bus', 'Trailer', 'Construction vehicle',
                   'Pedestrian', 'Motorcycle', 'Bicycle',
                   'Traffic cone', 'Barrier']
    CAT_IDS = {i+1: v for i, v in enumerate(CATS)}  # category IDs
    FRAME_RATE = 25  # 25fps, 0.04s/frame

    # sentence generate
    sentence = []
    obj_ids = sorted(list(objInfo.keys()))

    ## trajectory description
    traj_description = '{CAT}{IDX} moved {DIRECTION} for {DIST:.2f} meters with an average speed of {SPEED:.2f} m/s.'
    cat_idx = dict()
    for k in obj_ids:
        cat_idx[objInfo[k]['class']] = 1 if objInfo[k]['class'] not in cat_idx \
            else cat_idx[objInfo[k]['class']] + 1

        CAT = CAT_IDS[objInfo[k]['class']]
        IDX = cat_idx[objInfo[k]['class']]  # index in a category
        loc1 = np.array(objInfo[k]['loc'][0])
        loc2 = np.array(objInfo[k]['loc'][-1])
        DIST = np.linalg.norm(loc2-loc1)
        DIRECTION = 'forward' if loc2[2]-loc1[2] > 0 else 'backward'
        frame_count = objInfo[k]['frame_idx'][-1] - objInfo[k]['frame_idx'][0]
        SPEED = DIST/(frame_count/FRAME_RATE)

        sentence.append(traj_description.format(CAT=CAT, IDX=IDX, DIRECTION=DIRECTION,
                                                LOC1=loc1, LOC2=loc2, DIST=DIST, SPEED=SPEED))

    ## final description
    description = ' '.join(sentence)

    return description
#%% main


def main(data_path, save_dir):

    # extract object information from json file
    objInfo = getObjInfoFromJson(data_path)

    # filter objInfo
    objInfo = filterObjInfo(objInfo)

    # save obj info
    data_name = data_path.split('/')[-1][0:-13]
    with open(save_dir+data_name+'_objInfo.json', 'w') as f:
        json.dump(objInfo, f)

    # print(objInfo)
    # generate description from object information
    description = genSentenceFromInfo(objInfo)

    print(description)

    with open(save_dir+data_name+'_description.json', 'w') as f:
        json.dump(description, f)


if __name__ == '__main__':
    # argparse
    parser = argparse.ArgumentParser(description='args')
    parser.add_argument('--data_path', type=str,
                        default='./results/bus/test_bus_ResData.json', help='data name')
    parser.add_argument('--save_dir', type=str,
                        default='./results/bus/', help='saving dir')
    args = parser.parse_args()
    data_path = args.data_path
    save_path = args.save_dir

    # run
    main(data_path, save_path)
