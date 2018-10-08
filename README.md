This program has been implemented for the research presented in the article "Availability-aware Service Placement Policy in Fog Computing Based on Graph Partitions", submitted for consideration for publication in "IEEE IoT Journal".


These are the implementations of two service placement algorithms for fog computing in python 2.7. One is an ILP-based algorithm and the second one is based on the use of complex networks and graph partitions. For more details, please, read the article in XXXTBDXXXX

This repository only contains the files that generate and solve the placement of the services into the fog devices. This is stored in JSON files. For the execution of the simulation, it is necessary to install the the YAFS simulator (https://github.com/acsicuib/YAFS) and this installation already includes an example with our allocation results including those JSON files in https://github.com/acsicuib/YAFS/tree/master/src/examples/PartitionILPPlacement. To execute the simulation it is necessary to execute in that folder the command "python main.py". By this, different simulation with different allocations can be also executed by just replacing the JSON files.


This program is released under the GPLv3 License.

**Please consider to cite this work as**:

```bash
TBD
```

**Execution of the program**:

```bash
    python placementMain.py
```

**Acknowledgment**:

This research was supported by the Spanish Government (Agencia Estatal de Investigación) and the European Commission (Fondo Europeo de Desarrollo Regional) through Grant Number TIN2017-88547-P (AEI/FEDER, UE).
