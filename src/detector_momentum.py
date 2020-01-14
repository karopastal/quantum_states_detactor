import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from src.ring import Ring

N = 100
HOPPING_AMPLITUDE = 0.01
TAUS = 100
TAU_INTERVAL = 1
ENABLE_DETECTOR = True
SITE_ZERO = 50
DETECTOR = SITE_ZERO
DETECTOR_FREQUENCY = 1
MOMENTUM_STATE = 0


class DetectorMomentum:
    def __init__(self,
                 n=3,
                 taus=6,
                 site_zero=0,
                 detector=0,
                 detector_frequency=1,
                 tau_interval=25,
                 hopping_amp=1,
                 momentum_state=0,
                 enable_detector=False):

        self.n = n
        self.taus = np.arange(0, taus)  # [0,1,2,3,4,5]
        self.site_zero = site_zero
        self.detector = detector
        self.detector_frequency = detector_frequency
        self.hopping_amp = hopping_amp
        self.momentum_state = momentum_state
        self.enable_detector = enable_detector

        self.ring = Ring(n=N,
                         site_zero=site_zero,
                         detector=self.detector,
                         detector_frequency=self.detector_frequency,
                         tau_interval=tau_interval,
                         hopping_amp=hopping_amp,
                         enable_detector=self.enable_detector)

        self.time, psi_momentum, probabilities_momentum = self.ring.compute_momentum_tau(
            taus=self.taus, momentum_state=self.momentum_state)

        self.psi_momentum_t = np.stack(psi_momentum, axis=0)
        self.probabilities_momentum_t = np.stack(probabilities_momentum, axis=0)

    def plot_detector(self):
        detector = self.detector
        probabilities_site_zero_t = self.probabilities_momentum_t[:, detector:detector + 1].reshape(
            self.probabilities_momentum_t[:, detector:detector + 1].shape[0], )

        fig, ax = plt.subplots()
        ax.plot(self.time, probabilities_site_zero_t)

        ax.set(xlabel='Time (a.u)',
               ylabel='Probability(Time)',
               title='%s sites, %s detections, detector at site: #%s, hopping: %s' %
                     (self.n, len(self.taus), self.detector, self.hopping_amp))

        ax.grid()
        plt.show()

    def plot_momentum_t(self):
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.imshow(self.probabilities_momentum_t, interpolation='nearest', aspect='auto')
        ax.set_ylim(0, self.probabilities_momentum_t.shape[0])

        plt.title('%s sites, %s detections, detector at site: #%s, hopping: %s, momentum state: %s ' %
                  (self.n, len(self.taus), self.detector, self.hopping_amp, self.momentum_state))

        plt.ylabel('Time (a.u)')
        plt.xlabel('Position')
        plt.show()


def main():
    detector = DetectorMomentum(n=N,
                                taus=TAUS,
                                site_zero=SITE_ZERO,
                                detector=DETECTOR,
                                detector_frequency=DETECTOR_FREQUENCY,
                                tau_interval=TAU_INTERVAL,
                                hopping_amp=HOPPING_AMPLITUDE,
                                momentum_state=MOMENTUM_STATE,
                                enable_detector=ENABLE_DETECTOR)

    detector.plot_momentum_t()


if __name__ == '__main__':
    main()
