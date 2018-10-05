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

import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


class myPlots:
    
    def __init__(self, cn, ilp, cnf, failures):

        self.colorGtws = '#756bb1'
        self.colorPartition =  '#a6bddb'
        self.colorILP = '#e34a33'
        
        self.labelPartition = 'Partition'
        self.labelILP = 'ILP'
        self.labelGtws = 'Gtws'
        
        self.cn = cn
        self.ilp = ilp
        self.cnf = cnf
        self.failures = failures


    def plotNodeResource(self):
        ####Plot for node ordered vs service resources
        #nodeid:request
        #statisticsNodesRequest = {}
    
    

    
        fig, ax = plt.subplots(figsize=(8.0,5.0))
        plt.xlabel('Device ids.',fontsize=18)
        plt.ylabel('Resource usage (%)',fontsize=18)
    
        plt.plot(self.cn.nodeResUse, c=self.colorPartition, label=self.labelPartition,linewidth=4.0)
        plt.plot(self.ilp.nodeResUseILP, c=self.colorILP, label=self.labelILP,linewidth=4.0,linestyle='--')
        lgnd=plt.legend(fontsize=18,loc='upper left', ncol=1)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
    
 
        plt.grid()
        if self.cnf.graphicTerminal:
            plt.show()
    
        fig.savefig('./'+self.cnf.resultFolder+'/nodevsresourceuse.pdf',format='pdf')
    
        plt.close(fig)    
        
        
        

    def plotDistanceRequest(self):
        
        ####PLOT distance vs request
        #distance:request
        #statisticsCentralityResources = {}
    
        x=list()
        y=list()
    
    
        for i in self.cn.statisticsDistancesRequest.items():
            x.append(i[0])
            y.append(i[1])
    
    
        xILP=list()
        yILP=list()
    
        for i in self.ilp.statisticsDistancesRequestILP.items():
            xILP.append(i[0])
            yILP.append(i[1])
    

    
        fig, ax = plt.subplots(figsize=(8.0,5.0))
        plt.xlabel('Hop distance',fontsize=18)
        plt.ylabel('Num. of IoT devices',fontsize=18)
    
        plt.scatter(x, y,s=100, c=self.colorPartition, label=self.labelPartition)
        plt.scatter(xILP, yILP,s=100, c=self.colorILP, label=self.labelILP,marker="X")
        lgnd=plt.legend(fontsize=18,loc='upper right', ncol=1)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
    
        for handle in lgnd.legendHandles:
            handle.set_sizes([150.0])
    
        plt.grid()
        if self.cnf.graphicTerminal:
            plt.show()
    
        fig.savefig('./'+self.cnf.resultFolder+'/distancevsrequest.pdf',format='pdf')
    
        plt.close(fig)
    
    
    def plotFailures(self):
        ########
        #Availability with fails in random order
    
    
        for i in range(0,len(self.failures.unavailableCommunityrnd)):
            self.failures.unavailableCommunityrnd[i] = 70-self.failures.unavailableCommunityrnd[i]
            
        for i in range(0,len(self.failures.unavailableILPrnd)):
            self.failures.unavailableILPrnd[i] = 70-self.failures.unavailableILPrnd[i]
            
        for i in range(0,len(self.failures.unavailableAllinGtwsrnd)):
            self.failures.unavailableAllinGtwsrnd[i] = 70-self.failures.unavailableAllinGtwsrnd[i]
            
        self.labelGtws = 'All in gtws.'
            
    
        fig, ax = plt.subplots(figsize=(8.0,5.0))
        plt.xlabel('Num. of failed fog devices',fontsize=18)
        plt.ylabel('IoT devices with\n available service',fontsize=18)
    
        plt.plot(self.failures.unavailableCommunityrnd, c=self.colorPartition, alpha=0.5,label=self.labelPartition,linewidth=4.0)
        plt.plot(self.failures.unavailableILPrnd, c=self.colorILP, label=self.labelILP,linewidth=4.0,linestyle='--')
        plt.plot(self.failures.unavailableAllinGtwsrnd, c=self.colorGtws, label=self.labelGtws,linewidth=4.0,linestyle=':')
        plt.gcf().subplots_adjust(bottom=0.15)
        lgnd=plt.legend(fontsize=18,loc='upper right')
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
    
    
        plt.grid()
        if self.cnf.graphicTerminal:
            plt.show()
    
        fig.savefig('./'+self.cnf.resultFolder+'/availabilityRND.pdf',format='pdf')
    
        plt.close(fig)
    
    

        