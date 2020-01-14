import numpy as np
from src.detector_sites import DetectorSites


def main():
    detector = DetectorSites(n=2,
                             taus=10,
                             site_zero=0,
                             detector=1,
                             detector_frequency=1,
                             tau_interval=20,
                             hopping_amp=1,
                             enable_detector=False)

    print("Energies: \n", detector.ring.energies)
    print("States: \n", detector.ring.states)
    print("| + > : ", np.linalg.solve(detector.ring.states, np.array([1, 0])))
    print("| - > : ", np.linalg.solve(detector.ring.states, np.array([0, 1])))

    detector.plot_detector()
    detector.plot_probabilities_t()


if __name__ == '__main__':
    main()
