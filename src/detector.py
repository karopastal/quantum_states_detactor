import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from src.ring import Ring

N = 25
TAUS = 11
SITE_ZERO = 1  # np.random.randint(1, n+1)
TAU_INTERVAL = 100
HOPPING_AMPLITUDE = 1


class Detector:
    def __init__(self, n=3, taus=6, site_zero=0, tau_interval=25, hopping_amp=1):
        self.n = n
        self.taus = np.arange(1, taus)
        self.site_zero = site_zero

        self.ring = Ring(n=N,
                         site_zero=site_zero,
                         tau_interval=tau_interval,
                         hopping_amp=hopping_amp)

        self.time, psi, probabilities = self.ring.compute_psi_tau(taus=self.taus)
        self.psi_t = np.stack(psi, axis=0)
        self.probabilities_t = np.stack(probabilities, axis=0)

    def plot_site_zero(self):
        probabilities_site_zero_t = self.probabilities_t[:, self.site_zero:self.site_zero + 1].reshape(
            self.probabilities_t[:, self.site_zero:self.site_zero + 1].shape[0], )

        fig, ax = plt.subplots()
        ax.plot(self.time, probabilities_site_zero_t)

        ax.set(xlabel='Time (a.u)',
               ylabel='Probability(Time)',
               title='%s sites system, %s detections, detector located on site: #%s' %
                     (self.n, len(self.taus), self.site_zero))

        ax.grid()
        plt.show()

    def plot_probabilities_t(self):
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.imshow(self.probabilities_t, interpolation='nearest', aspect='auto')

        plt.title('%s sites system, %s detections, detector located on site: #%s' %
                  (self.n, len(self.taus), self.site_zero))

        plt.ylabel('Time (a.u)')
        plt.xlabel('Position')
        plt.show()


def main():
    detector = Detector(n=N,
                        taus=TAUS,
                        site_zero=SITE_ZERO,
                        tau_interval=TAU_INTERVAL,
                        hopping_amp=HOPPING_AMPLITUDE)

    detector.plot_site_zero()
    detector.plot_probabilities_t()


if __name__ == '__main__':
    main()
