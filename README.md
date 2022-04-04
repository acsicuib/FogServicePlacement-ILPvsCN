This program has been implemented for the research presented in the article "Availability-aware Service Placement Policy in Fog Computing Based on Graph Partitions", accepted for publication in "IEEE IoT Journal".


These are the implementations of two service placement algorithms for fog computing in python 2.7. One is an ILP-based algorithm and the second one is based on the use of complex networks and graph partitions. For more details, please, read the article in https://ieeexplore.ieee.org/document/8588297

This repository only contains the files that generate and solve the placement of the services into the fog devices. This is stored in JSON files. For the execution of the simulation, it is necessary to install the the YAFS simulator (https://github.com/acsicuib/YAFS) and this installation already includes an example with our allocation results including those JSON files in https://github.com/acsicuib/YAFS/tree/master/src/examples/PartitionILPPlacement. To execute the simulation it is necessary to execute in that folder the command "python main.py". By this, different simulation with different allocations can be also executed by just replacing the JSON files.


This program is released under the GPLv3 License.

**Please consider to cite this work as**:

```bash
@article{lera_availability-aware_2019,
	title = {Availability-{Aware} {Service} {Placement} {Policy} in {Fog} {Computing} {Based} on {Graph} {Partitions}},
	volume = {6},
	copyright = {All rights reserved},
	issn = {2327-4662},
	doi = {10.1109/JIOT.2018.2889511},
	abstract = {Fog computing extends the cloud to where things are by placing applications closer to the users and Internet of Things devices. The placement of those applications, or their services, has an important influence on the performance of the fog architecture. Improving the availability and the latency of the applications is a challenging task due to the complexity of this type of distributed system. In this paper, we propose a service placement policy inspired by complex networks. We are able to increase the service availability and the quality of service (QoS) satisfaction rate by first mapping applications to communities of fog devices and then transitively placing the services of the applications on the fog devices of the community. The underlying idea is to place as many interrelated services as possible in the devices closest to the users. We compare our solution with an integer linear programming approach, and the simulation results show that our proposal obtains improved QoS satisfaction and service availability.},
	number = {2},
	journal = {IEEE Internet of Things Journal},
	author = {Lera, Isaac and Guerrero, Carlos and Juiz, Carlos},
	month = apr,
	year = {2019},
	note = {Conference Name: IEEE Internet of Things Journal},
	keywords = {Internet of Things, Computer architecture, Optimization, Cloud computing, Edge computing, Resource management, fog computing, service placement, Complex network communities, graph transitive closures, performance optimization, Proposals, service availability},
	pages = {3641--3651}
}
```

**Execution of the program**:

```bash
    python placementMain.py
```

**Acknowledgment**:

This research was supported by the Spanish Government (Agencia Estatal de Investigación) and the European Commission (Fondo Europeo de Desarrollo Regional) through Grant Number TIN2017-88547-P (AEI/FEDER, UE).
