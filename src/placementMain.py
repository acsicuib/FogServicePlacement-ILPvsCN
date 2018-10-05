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


import random
import ILP
import experimentConfiguration
import myConfig
import myPlots
import devFailures
import CNoptimization



#****************************************************************************************************

#inizializations and set up

#****************************************************************************************************
random.seed(8)
verbose_log = False

generatePlots = True

ILPoptimization = True
CommunityOptimization = True



cnf_ = myConfig.myConfig()
ec = experimentConfiguration.experimentConfiguration(cnf_)
ec.loadConfiguration(cnf_.myConfiguration_)

ec.networkGeneration()
ec.appGeneration()
ec.userGeneration()



#########################
#    GRAPH PARTITION OPTIMIZATION
#########################

if CommunityOptimization:

    
    cno_ = CNoptimization.CNoptimization(ec,cnf_)
    service2DevicePlacementMatrix = cno_.solve()
    
#########################
#    ILP OPTIMIZATION
#########################


if ILPoptimization:
    ilp_ = ILP.ILP(ec,cnf_)
    service2DevicePlacementMatrixILP = ilp_.solve()


#########################
#    PLOTS FOR THE PAPER
#########################


if generatePlots:

    #****************************************************************************************************
    # unavailability calculation
    #****************************************************************************************************

    failures_ = devFailures.devFailures(ec,cno_, ilp_)
    failures_.createFails()    

    #****************************************************************************************************
    # creating the plots
    #****************************************************************************************************

    
    plot_ = myPlots.myPlots(cno_, ilp_, cnf_, failures_)
    plot_.plotDistanceRequest()
    plot_.plotNodeResource()
    plot_.plotFailures()
    

















    






