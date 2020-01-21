# Traveling detector of a momentum state
1. [Introduction](#intro)
2. [Usage](#usage)
3. [Examples](#examples)

<a name="desc"></a>
### Introduction

There are three main components to the system:


`Ring` is the core component where the physical configuration takes place and the computations of the prepared wave function over time.
The `Ring` is configured by the following parameters:

```
    N = (Integer), number of sites.
    TAUS = (Integer), the duration of the experiment in units of tau=1.
    TAU_INTERVAL = (Integer), the resolution of 1[tau] interval (partition).
    HOPPING_AMPLITUDE = (Float), the hopping constant between sites.
```

`SitesDetector` component represent an instant of detector on a ring and configured with the following parameters:

```
    SITE_ZERO = (Integer), the site number where the particle is prepared at when (t=0).
    ENABLE_DETECTOR = (Boolean), enable or disable the detector.
    $DETECTOR = (Integer), the site number where the detector is placed.
    DETECTOR_FREQUENCY = (Integer), determines the frequency of detection in units of `[tau]`
```

`MomentumDetector` component represent an instant of detector on a ring such that the wave function prepared at a s
specific momentum state `|k_m>` when `t=0`. Moreover, the detector can be stationary or travel with the speed of the initial momentum state.
Momentum Detector is configured with the following parameters:

```
    MOMENTUM_STATE = (Integer), the `m` index of `|k_m>` that the wave function prepared at.
    ENABLE_DETECTOR = (Boolean), enable or disable the detector.
    DETECTOR = (Integer), the site number where the detector is placed at `t=0`.
    DETECTOR_FREQUENCY = (Integer), determines the frequency of detection in units of `[tau]`.
    ENABLE_DETECTOR_VELOCITY = (Boolean), determines if the detector is stationary or traveling.
```
 

<a name="desc"></a>
### Usage

#### prerequisites
make sure you are using `python3` for compatibility with the syntax.
*nix environment is preferred, but if you are running on windows `gitbash` (installed with git) 
is the recommended terminal to run the commands.
 
 #### install
```shell script
    $ git clone https://github.com/karopastal/quantum_states_detactor.git
    $ cd quantum_states_detactor
    $ pip3 install numpy matplotlib
```

#### run expirements

At `./analysis/` you can find a templates for experiments for the two cases. After parametrization of the
desired configuration run the relevant expirement with:
 
```shell script
   $ make detector_sites_case 
``` 
Or

```shell script
   $ make detector_momentum_case 
``` 

<a name="examples"></a>
### Examples
 #### Configuration:
 
 ```shell script
N = 10
TAUS = 50
SITE_ZERO = 0
DETECTOR = 0
DETECTOR_FREQUENCY = 5
TAU_INTERVAL = 20
HOPPING_AMP = 0.05
ENABLE_DETECTOR = False
```
```shell script
   $ make detector_sites_case 
``` 

#### plot_detector:

![](/docs/examples/10_sites.png)

#### configuration:

 ```shell script
N = 100
TAUS = 50
SITE_ZERO = 0
DETECTOR = 50
DETECTOR_FREQUENCY = 5
TAU_INTERVAL = 20
HOPPING_AMP = 1
ENABLE_DETECTOR = True
```

```shell script
   $ make detector_sites_case 
``` 

#### plot_probabilities_t:
![](/docs/examples/100_sites.png)

#### configuration:
```shell script
N = 10
HOPPING_AMPLITUDE = 0.25
TAUS = 100
TAU_INTERVAL = 5
ENABLE_DETECTOR = True
DETECTOR = 5
DETECTOR_FREQUENCY = 5
MOMENTUM_STATE = 5
ENABLE_DETECTOR_VELOCITY = True
```

```shell script
   $ make detector_momentum_case 
``` 

#### plot_detector:
![](/docs/examples/10_momentum.png)


#### configuration:
```shell script
N = 200
HOPPING_AMPLITUDE = 1
TAUS = 100
TAU_INTERVAL = 5
ENABLE_DETECTOR = True
DETECTOR = 100
DETECTOR_FREQUENCY = 5
MOMENTUM_STATE = 50
ENABLE_DETECTOR_VELOCITY = True
```

```shell script
   $ make detector_momentum_case 
``` 

#### plot_probabilities_t:
![](/docs/examples/200_momentum.png)
