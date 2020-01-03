import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from src.ring import Ring

N = 200
HOPPING_AMPLITUDE = 0.15
TAUS = 50
TAU_INTERVAL = 50
ENABLE_DETECTOR = True
SITE_ZERO = 100
DETECTOR = SITE_ZERO
DETECTOR_FREQUENCY = 1


class DetectorSites:
    def __init__(self,
                 n=3,
                 taus=6,
                 site_zero=0,
                 detector=0,
                 detector_frequency=1,
                 tau_interval=25,
                 hopping_amp=1,
                 enable_detector=False):

        self.n = n
        self.taus = np.arange(0, taus)  # [0,1,2,3,4,5]
        self.site_zero = site_zero
        self.detector_frequency = detector_frequency
        self.detector = detector  # int(int(self.site_zero + self.n)/2)
        self.hopping_amp = hopping_amp
        self.enable_detector = enable_detector

        self.ring = Ring(n=N,
                         site_zero=site_zero,
                         detector=self.detector,
                         detector_frequency=self.detector_frequency,
                         tau_interval=tau_interval,
                         hopping_amp=hopping_amp,
                         enable_detector=self.enable_detector)

        self.time, psi, probabilities = self.ring.compute_psi_tau(taus=self.taus)
        self.psi_t = np.stack(psi, axis=0)
        self.probabilities_t = np.stack(probabilities, axis=0)

    def plot_detector(self):
        detector = self.detector
        probabilities_site_zero_t = self.probabilities_t[:, detector:detector + 1].reshape(
            self.probabilities_t[:, detector:detector + 1].shape[0], )

        fig, ax = plt.subplots()
        ax.plot(self.time, probabilities_site_zero_t)

        ax.set(xlabel='Time (a.u)',
               ylabel='Probability(Time)',
               title='%s sites, %s detections, detector at site: #%s, hopping: %s' %
                     (self.n, len(self.taus), self.detector, self.hopping_amp))

        ax.grid()
        plt.show()

    def plot_probabilities_t(self):
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.imshow(self.probabilities_t, interpolation='nearest', aspect='auto')
        ax.set_ylim(0, self.probabilities_t.shape[0])

        plt.title('%s sites, %s detections, detector at site: #%s, hopping: %s' %
                  (self.n, len(self.taus), self.detector, self.hopping_amp))

        plt.ylabel('Time (a.u)')
        plt.xlabel('Position')
        plt.show()


def main():
    detector = DetectorSites(n=N,
                             taus=TAUS,
                             site_zero=SITE_ZERO,
                             detector=DETECTOR,
                             detector_frequency=DETECTOR_FREQUENCY,
                             tau_interval=TAU_INTERVAL,
                             hopping_amp=HOPPING_AMPLITUDE,
                             enable_detector=ENABLE_DETECTOR)

    detector.plot_probabilities_t()


if __name__ == '__main__':
    main()
