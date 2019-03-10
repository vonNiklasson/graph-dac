# Distributed-Average-Consensus

This program is aimed to help understand the path of how Distributed Average Consensus works across multiple nodes in a network.

## How to use

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
