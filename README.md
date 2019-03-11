# Distributed-Average-Consensus

This program is aimed to help understand the path of how Distributed Average Consensus works across multiple nodes in a network.

## How to use by command

Run the command below:  
```
python cmd.py [graph] [deviance_threshold]
```

### Arguments:
`[graph]` *(optional)*: Change this to a graph represented in the file `graphs.py`. Defaults to `cross`.  
`[deviance_threshold]` *(optional)*: Sets the deviance value in which the iterations should stop. Defaults to `0.01`.  

### Example usage:
```
python cmd.py pentagon 0
```

## Example output  
```
 ITER |     AVG |     DEV |      #1 |      #2 |      #3 |      #4 |      #5 |
    0 |     3.0 |     2.0 |     1.0 |     2.0 |     3.0 |     4.0 |     5.0 |
    1 |     2.4 |     0.9 |     3.0 |     1.5 |     2.0 |     2.5 |     3.0 |
    2 |    2.58 |    0.42 |     2.4 |    2.25 |     2.5 |    2.75 |     3.0 |
    3 |    2.53 |     0.2 |    2.58 |    2.33 |    2.45 |    2.58 |     2.7 |
    4 |    2.54 |     0.1 |    2.53 |    2.45 |    2.52 |    2.58 |    2.64 |
    5 |    2.54 |    0.05 |    2.54 |    2.49 |    2.52 |    2.55 |    2.58 |
    6 |    2.54 |    0.02 |    2.54 |    2.52 |    2.53 |    2.55 |    2.56 |
    7 |    2.54 |    0.01 |    2.54 |    2.53 |    2.53 |    2.54 |    2.55 |
    8 |    2.54 |    0.01 |    2.54 |    2.53 |    2.54 |    2.54 |    2.54 |
```

### Legend
`ITER`: The current iteration of the consensus loop.  
`AVG`: The current average value of the network.  
`DEV`: The maximum deviance of the network from the average value.  
`#[ID]`: The value of the given sensor with id=`[ID]`.  


## How to integrate

Import the module `Network` by using the following line (see example usage in `cmd.py`).

```python
from Network import Network
network = Network()
```

### Adding a node

Either add nodes one by one by one or all together with either of the following code.

#### Adding nodes one by one
```python
network.add_node(<node_id_1>, <node_value_1>)
network.add_node(<node_id_1>, <node_value_2>)
```

#### Adding multiple nodes
```python
nodes = {
    node_id_1: node_value_1,
    node_id_1: node_value_2,
    ...
}

network.add_nodes(nodes)
```

### Adding an edge

Similarly to adding nodes you can add edges one by one or multiple at once.

> **Note**: Adding edges will automatically make them bidirectional, 
> there's no need to make reverse edges, however it won't hurt either.

#### Adding edges one by one

```python
network.add_edge(<node_id_1>, <node_id_2>)
network.add_edge(<node_id_1>, <node_id_3>)
network.add_edge(<node_id_2>, <node_id_3>)
```

#### Adding multiple edges

```python
edges = {
    <node_id_1>: [<node_id_2>, <node_id_3>],
    <node_id_2>: [<node_id_3>],
    ...
}
network.add_edges(edges)
```

### Preparing to solve the network

When finding the distributed distributed average consensus you can set 
the deviance and the maximum number of iterations allowed when trying to solve the network.

This is done by using the following commands:

```python
network.set_max_iterations(1000)
network.set_deviance(0.01)
```

However, both of these are optional and will default to the following:

```python
max iterations = 1000
deviance       = 0.01
```

### Actually solving the network

In order to find a consensus you can use the `network.solve()` function. The `solve` 
takes 1 argument which decides whether it will print all the iterations.

```python
# Will print the output
result = network.solve(True)
```

```python
# Will NOT print the output (defaults to False)
result = network.solve(False)
result = network.solve()
```

The function will also return a resulting value which has 3 properties.

```python
result = network.solve()

result[0] # True/False: True if a consensus was found, otherwise False.
result[1] # Integer: Number of iterations that has been stepped through. 
          # Will at maximum be <max_iterations> + 1
result[2] # Float: The deviance of the last iteration.
```

