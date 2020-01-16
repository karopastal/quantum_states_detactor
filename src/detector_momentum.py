import numpy as np
import matplotlib.pyplot as plt
from src.ring import Ring

N = 200
A = 1
HOPPING_AMPLITUDE = 1
TAUS = 100
TAU_INTERVAL = 5
ENABLE_DETECTOR = True
SITE_ZERO = 101
DETECTOR = SITE_ZERO
DETECTOR_FREQUENCY = 5
MOMENTUM_STATE = 50
ENABLE_DETECTOR_VELOCITY = True


class DetectorMomentum:
    def __init__(self,
                 n=3,
                 a=1,
                 taus=6,
                 site_zero=0,
                 detector=0,
                 detector_frequency=1,
                 tau_interval=25,
                 hopping_amp=1,
                 momentum_state=0,
                 enable_detector=False,
                 enable_detector_velocity=False):

        self.n = n
        self.a = a
        self.taus = np.arange(0, taus)
        self.site_zero = site_zero
        self.detector = detector
        self.detector_frequency = detector_frequency
        self.hopping_amp = hopping_amp
        self.momentum_state = momentum_state
        self.enable_detector = enable_detector
        self.enable_detector_velocity = enable_detector_velocity

        self.ring = Ring(n=self.n,
                         site_zero=site_zero,
                         detector=self.detector,
                         detector_frequency=self.detector_frequency,
                         tau_interval=tau_interval,
                         hopping_amp=hopping_amp,
                         enable_detector=self.enable_detector,
                         enable_detector_velocity=self.enable_detector_velocity)

        self.time, psi_momentum, probabilities_momentum = self.ring.compute_momentum_tau(
            taus=self.taus, momentum_state=self.momentum_state)

        self.psi_momentum_t = np.stack(psi_momentum, axis=0)
        self.probabilities_momentum_t = np.stack(probabilities_momentum, axis=0)

    def plot_detector(self):
        fig, ax = plt.subplots()

        for i in range(len(self.probabilities_momentum_t.T)):
            ax.plot(self.time, self.probabilities_momentum_t.T[i], label='site ' + str(i + 1))

        plt.legend(bbox_to_anchor=(1.125, 1), loc='upper right', borderaxespad=0.1, fontsize=14)

        if self.enable_detector:
            detector = '| %s >' % self.detector

            if self.enable_detector_velocity:
                detections = 'every %s [tau], v_m: %s' % (self.detector_frequency, 'on',)
            else:
                detections = 'every %s [tau], v_m: %s' % (self.detector_frequency, 'off',)

        else:
            detector = 'disabled'
            detections = 'None'

        plt.title('%s sites, momentum(t=0): | k_%s >, detector: %s, detections: %s' %
                  (self.n,  self.momentum_state, detector, detections), fontsize=18)

        plt.xlabel('Time [tau]', fontsize=20)
        plt.ylabel('Probability', fontsize=20)

        ax.grid()
        plt.show()

    def plot_momentum_t(self):
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.imshow(self.probabilities_momentum_t.T,
                  extent=(0, len(self.taus), self.n, 0),
                  interpolation='nearest',
                  aspect='auto',
                  cmap='pink')

        ax.set_ylim(0, self.n)

        if self.enable_detector:
            detector = '| %s >' % self.detector

            if self.enable_detector_velocity:
                detections = 'every %s [tau], v_m: %s' % (self.detector_frequency, 'on',)
            else:
                detections = 'every %s [tau], v_m: %s' % (self.detector_frequency, 'off',)

        else:
            detector = 'disabled'
            detections = 'None'

        plt.title('%s sites, momentum(t=0): | k_%s >, detector: %s, detections: %s' %
                  (self.n,  self.momentum_state, detector, detections), fontsize=18)

        plt.xlabel('Time [tau]')
        plt.ylabel('Position')
        plt.show()

    def save_plot(self, title, path):
        fig, ax = plt.subplots(figsize=(15, 9))
        img = ax.imshow(self.probabilities_momentum_t.T,
                        extent=(0, len(self.taus), self.n, 0),
                        interpolation='nearest',
                        aspect='auto',
                        cmap='pink')

        ax.set_ylim(0, self.n)

        fig.colorbar(img, ax=ax)

        plt.title(title, fontsize=25)
        plt.xlabel('Time [tau]', fontsize=22)
        plt.ylabel('Position',  fontsize=22)

        plt.savefig(path)


def main():
    detector = DetectorMomentum(n=N,
                                a=A,
                                taus=TAUS,
                                site_zero=SITE_ZERO,
                                detector=DETECTOR,
                                detector_frequency=DETECTOR_FREQUENCY,
                                tau_interval=TAU_INTERVAL,
                                hopping_amp=HOPPING_AMPLITUDE,
                                momentum_state=MOMENTUM_STATE,
                                enable_detector=ENABLE_DETECTOR,
                                enable_detector_velocity=ENABLE_DETECTOR_VELOCITY)

    detector.plot_momentum_t()
    # detector.plot_detector()


if __name__ == '__main__':
    main()
