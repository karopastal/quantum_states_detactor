import numpy as np
from src.detector_bloch_sites import DetectorBlochSites

# N = 200
# A = 1
# ELECTRIC_FIELD = 0.05
# HOPPING_AMPLITUDE = 100
# TAUS = 380
# TAU_INTERVAL = 10
# SITE_ZERO = 100
# DETECTOR = 0
# DETECTOR_FREQUENCY = 25
# ENABLE_DETECTOR = False

N = 20
A = 1
ELECTRIC_FIELD = 0.05
HOPPING_AMPLITUDE = 100
TAUS = 100
TAU_INTERVAL = 10
SITE_ZERO = 100
DETECTOR = 0
DETECTOR_FREQUENCY = 25
ENABLE_DETECTOR = False


def main():

    detector = DetectorBlochSites(n=N,
                                  taus=TAUS,
                                  site_zero=SITE_ZERO,
                                  electric_field=ELECTRIC_FIELD,
                                  detector=DETECTOR,
                                  detector_frequency=DETECTOR_FREQUENCY,
                                  tau_interval=TAU_INTERVAL,
                                  hopping_amp=HOPPING_AMPLITUDE,
                                  enable_detector=ENABLE_DETECTOR)

    detector.plot_probability_per_site()
    detector.plot_probability_density()


if __name__ == '__main__':
    main()
