import numpy as np
import pandas as pd
import random
import math
from random import randrange
from datetime import datetime


def severity_generator(notice_pct_dist, notice_pct_loss_dist, severity_dist):
    notice_pct = np.random.choice(notice_pct_dist)
    notice_pct_loss = np.random.choice(notice_pct_loss_dist)
    low_severity_pct = np.random.choice(severity_dist)
    med_high_severity_pct_generator = np.random.random(1)[0]
    med_severity_pct = (1 - low_severity_pct) * (med_high_severity_pct_generator)
    high_severity_pct = (1 - low_severity_pct) * (1-med_high_severity_pct_generator)
    
    return notice_pct, notice_pct_loss, low_severity_pct, med_severity_pct, high_severity_pct

def DV_generator(deal_count, DV_range, sme_low_DV, sme_upper_DV, mm_low_DV, mm_upper_DV, sme_pct, mm_pct, j_pct, j_low_DV, j_upper_DV):
    DV_list = []
    sme_count = int(deal_count*sme_pct)
    mm_count = int(deal_count*mm_pct)
    j_count = int(deal_count*j_pct)
    for x in range(sme_count):
        DV_list.append(random.randrange(sme_low_DV, sme_upper_DV, DV_range)) 
    for x in range(mm_count):
        DV_list.append(random.randrange(mm_low_DV, mm_upper_DV, DV_range)) 
    for x in range(j_count):
        DV_list.append(random.randrange(j_low_DV, j_upper_DV, DV_range))  
    if (sme_count + mm_count + j_count) != deal_count:
        for i in range(deal_count - len(DV_list)):
            x = random.randrange(1, 4)
            if x == 1:
                DV_list.append(random.randrange(sme_low_DV, sme_upper_DV, DV_range)) 
            if x == 2:
                DV_list.append(random.randrange(mm_low_DV, mm_upper_DV, DV_range))
            if x == 3:
                DV_list.append(random.randrange(j_low_DV, j_upper_DV, DV_range))
    random.shuffle(DV_list)
    
    return DV_list

def structure_generator(DV_list, low_limit, upper_limit, limit_range, primary_pct, xs_pct, pri_attachment_pt_range):
    primary_xs_list = []
    for dv in DV_list:
        if dv > 750_000_000:
            x = np.random.choice([0, 1], size=1, p=[primary_pct, xs_pct])
            primary_xs_list.append(x[0])
        else:
            primary_xs_list.append(0)
            
    tower_limit_list = []
    for value in DV_list:
        tower_limit_list.append(random.randrange(value*.1, value*.2, 500_000)) 
    
    limit_list = []
    for index, tower_limit in enumerate(tower_limit_list):
        policy_limit = random.randrange(low_limit, upper_limit, limit_range)
        if policy_limit >= tower_limit_list[index]:
            policy_limit = tower_limit_list[index]
            limit_list.append(policy_limit)
        if policy_limit < tower_limit_list[index]:
            limit_list.append(policy_limit) 
        
    attachment_pt_list = []        
    for index, pri_v_xs in enumerate(primary_xs_list):
        if pri_v_xs == 0:
            y = np.random.choice(pri_attachment_pt_range, size=1)
            attachment_pt_list.append(y[0])
        if pri_v_xs == 1:
            layer_num = int(tower_limit_list[index] // limit_list[index])
            y = np.random.choice(pri_attachment_pt_range, size=1)
            z = y + ((random.randrange(1, layer_num+1)*limit_list[index])/DV_list[index])
            attachment_pt_list.append(z[0])

    return limit_list, attachment_pt_list, primary_xs_list