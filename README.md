# Traveling detector of a momentum state
1. [Introduction](#intro)
2. [Usage](#usage)

<a name="desc"></a>
### Introduction
 
This is a demonstration of the n-th of detection probability on a ring.
The system consists of a composition of `N sites`, hopping amplitude `c` and periodic boundary conditions.
At `t = 0`  the wavefunction is prepared on one of the sites, the detector stays at fixed location and 
is applied at intervals of `tau`.  Once the detection is affirmative the experiment is over.

<img src="https://media.giphy.com/media/PZ4y3x4F6y7de/giphy.gif" width="185" height="185" />


<a name="desc"></a>
### Usage

make sure you are using `python3` for computability with the syntax. If you are running
on windows `gitbash` (installed with git) is the right terminal to run the commands.
 
```shell script
    $ git clone https://github.com/karopastal/quantum_states_detactor.git
    $ cd quantum_states_detactor
```

Run the detector with:

```shell script
   $ make detector 
``` 

```shell script
   $ make site 
``` 

```shell script
   $ make ring 
``` 