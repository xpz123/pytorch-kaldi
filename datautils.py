import os
import sys
import numpy as np
import shutil
import pdb


def set_datapath(datapath, wavpath, featpath, cmvnpath):
    def set_path(paths, rootpath, writefile):
        res = list()
        fw = open(writefile, 'w')
        for l in paths:
            utt = l.split()[0]
            filename = l.split()[1].split(r'/')[-1]
            fw.write(os.path.join(rootpath, filename) + '\n')
        fw.close()
    pdb.set_trace()
    if os.path.exists(os.path.join(datapath, 'wav.scp')):
        lines = open(os.path.join(datapath, 'wav.scp')).readlines()
        set_path(lines, wavpath, os.path.join(datapath, 'wav.scp.new'))
        os.rename(os.path.join(datapath, 'wav.scp'), os.path.join(datapath, 'wav.scp.bk'))
        os.rename(os.path.join(datapath, 'wav.scp.new'), os.path.join(datapath, 'wav.scp'))
    if os.path.exists(os.path.join(datapath, 'feat.scp')):
        orifile = os.path.join(datapath, 'feat.scp')
        lines = open(orifile).readlines()
        set_path(lines, featpath, orifile + '.new')
        os.rename(orifile, orifile + '.bk')
        os.rename(orifile + '.new', orifile)
    if os.path.exists(os.path.join(datapath, 'cmvn.scp')):
        orifile = os.path.join(datapath, 'cmvn.scp')
        lines = open(orifile).readlines()
        set_path(lines, cmvnpath, orifile + '.new')
        os.rename(orifile, orifile + '.bk')
        os.rename(orifile + '.new', orifile)
        
        

    

   


