# Spanning Tree (Netztechnik Labor TINF20B)
### Usage
Before you run the programm you need to install the required packages:
```bash
pip install -r requirements.txt
```
```bash
python main.py [args]
```
#### Arguments
| Command Line Argument | Value type | Explanation
-- | -- | --
| `-f`, `--file` | `string` | File for reading the data of the spanning tree. This argument is required to run. You can use the example.txt as an example. |
| `-o`, `--out`  | `string` | File for writing the ouput of the spanning tree. If the file does not exist, it will be created. If no filename is provided, the output will be written to the console.  |
|`-m`, `--min`| `int` | The minimum number that a node must have sent |
|`-q`, `--quiet`| `none`| Specifies whether more precise output is to be output. |
### Input
The input is possible via a file, which one passes via the arguments. In the file the nodes and edges must be specified. You can find an example under `example.txt`.
### Algorithm
The algorithm has a while loop which iterates as long as all nodes have not reached the specified minimum number of sent messages. After a node is randomly selected, it iterates through the entire list of edges. 

Just as a hint, the list of edges is larger than the given one, which is due to the fact that the edges are stored twice and only the nodes are swapped to cover both directions.

Then it is checked if the edge leads to the root of the selected node, if this is the case it will be skipped. If this is not the case, the exact node is checked to see if its root id is greater than that of the randomly selected node. If this is the case, the properties of the next node will be overwritten. If the root id of the random selected node and root id of the next node are the same, only the cost is checked to see if it is cheaper.
### Output
The output of the program indicates the current node and its next node with the associated cost. For the root node, only "root" is displayed
Example:
```
A - B (10)
B (Root)
C - D (15)
D - E (12)
E - B (10)
F - E (12)
```