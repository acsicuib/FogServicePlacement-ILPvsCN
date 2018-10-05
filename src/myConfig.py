#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Copyright 2018 Carlos Guerrero, Isaac Lera.
Created on Tue May 22 15:58:58 2018
@authors:
    Carlos Guerrero
    carlos ( dot ) guerrero  uib ( dot ) es
    Isaac Lera
    isaac ( dot ) lera  uib ( dot ) es
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.


This program has been implemented for the research presented in the
article "Availability-aware Service Placement Policy in Fog Computing 
Based on Graph Partitions" and submitted for evaluation to the "IEEE 
IoT Journal".
"""

import os


class myConfig:
    
    def __init__(self):
        
        self.graphicTerminal = True
        self.verbose_log = False
        self.myConfiguration_ = 'iotjournal'
        self.resultFolder = 'plot2'
        
        
        
        try:
            os.stat(self.resultFolder)
        except:
            os.mkdir(self.resultFolder)




