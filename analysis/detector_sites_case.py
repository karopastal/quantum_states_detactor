import numpy as np
from src.detector_sites import DetectorSites

N = 100
TAUS = 50
SITE_ZERO = 0
DETECTOR = 50
DETECTOR_FREQUENCY = 5
TAU_INTERVAL = 20
HOPPING_AMP = 1
ENABLE_DETECTOR = True


def main():

    detector = DetectorSites(n=N,
                             taus=TAUS,
                             site_zero=SITE_ZERO,
                             detector=DETECTOR,
                             detector_frequency=DETECTOR_FREQUENCY,
                             tau_interval=TAU_INTERVAL,
                             hopping_amp=HOPPING_AMP,
                             enable_detector=ENABLE_DETECTOR)

    detector.plot_detector()
    detector.plot_probabilities_t()

    # print("Energies: \n", detector.ring.energies)
    # print("States: \n", detector.ring.states)
    # print("| + > : ", np.linalg.solve(detector.ring.states, np.array([1, 0])))
    # print("| - > : ", np.linalg.solve(detector.ring.states, np.array([0, 1])))


if __name__ == '__main__':
    main()
