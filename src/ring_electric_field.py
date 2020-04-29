import numpy as np
import scipy.special as sp


class RingElectricField:
    def __init__(self,
                 n=2,
                 a=1,
                 electric_field=1,
                 site_zero=0,
                 detector=0,
                 detector_frequency=1,
                 tau_interval=25,
                 hopping_amp=1,
                 enable_detector=False):

        if n < 2:
            raise Exception('Oops, valid Ring has no less than two sites, try again..')

        self.n = n
        self.nu = n
        self.a = a
        self.electric_field = electric_field
        self.site_zero = site_zero
        self.detector = detector
        self.detector_frequency = detector_frequency
        self.tau_interval = tau_interval
        self.hopping_amp = hopping_amp
        self.enable_detector = enable_detector

    def compute_psi_tau(self, taus):
        psi_time_series = []
        probabilities_time_series = []

        detection_counter = 0
        time = np.linspace(0, taus[-1], self.tau_interval * len(taus))

        for tau in taus:

            for idx in range(self.tau_interval):
                tic = time[idx + (detection_counter * self.tau_interval)]

                psi_tau_tic = np.zeros(self.n)

                for site in range(self.n):
                    gamma = site - self.site_zero
                    x = 2*(self.hopping_amp/self.electric_field)*(np.sin((self.electric_field * tic)/2))
                    psi_tau_tic[site] = sp.jv(gamma, x)

                # psi_tau_tic = psi_tau_tic / np.linalg.norm(psi_tau_tic)

                psi_time_series.append(psi_tau_tic)
                probabilities_time_series.append(np.power(np.abs(psi_tau_tic), 2))

            if self.enable_detector and ((tau + 1) % self.detector_frequency) == 0:
                psi_collapse = psi_time_series[-1]

                psi_collapse[self.detector] = 0
                psi_tau_tic = psi_collapse / np.linalg.norm(psi_collapse)

                psi_time_series[-1] = psi_tau_tic
                probabilities_time_series[-1] = np.square(np.abs(psi_tau_tic))

                detection_counter = 0
            else:
                detection_counter = detection_counter + 1

        return time, psi_time_series, probabilities_time_series


def main():
    ring = RingElectricField()

    print(ring.states)
    print(ring.energies)


if __name__ == '__main__':
    main()
