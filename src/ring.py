import numpy as np


class Ring:
    def __init__(self,
                 n=2,
                 a=1,
                 site_zero=0,
                 detector=0,
                 detector_frequency=1,
                 tau_interval=25,
                 hopping_amp=1,
                 enable_detector=False,
                 enable_detector_velocity=False):

        if n < 2:
            raise Exception('Oops, valid Ring has no less than two sites, try again..')

        self.n = n
        self.a = a
        self.site_zero = site_zero
        self.detector = detector
        self.detector_frequency = detector_frequency
        self.tau_interval = tau_interval
        self.hopping_amp = hopping_amp
        self.hamiltonian = self.__init_hamiltonian()
        self.position_hat = self.__init_position_hat()
        self.energies, self.states = self.__get_states_and_energies()
        self.enable_detector = enable_detector
        self.enable_detector_velocity = enable_detector_velocity

    def __init_hamiltonian(self):
        hamiltonian = np.zeros((self.n, self.n))
        frequencies = np.ones(self.n - 1) * self.hopping_amp
        np.fill_diagonal(hamiltonian[1:], frequencies)
        np.fill_diagonal(hamiltonian[:, 1:], frequencies)

        hamiltonian[0, self.n - 1] = self.hopping_amp
        hamiltonian[self.n - 1, 0] = self.hopping_amp

        return hamiltonian

    def __init_position_hat(self):
        position_hat = np.zeros((self.n, self.n))
        x = np.arange(1, self.n + 1)
        np.fill_diagonal(position_hat, x)
        
        return position_hat

    def __k(self, n):
        return (2 * np.pi * n) / self.n

    def __get_states_and_energies(self):
        energies = np.zeros(self.n)
        states = []

        for i in range(self.n):
            energies[i] = 2 * self.hopping_amp * np.cos(self.a * self.__k(i))

            weights = np.fromfunction(
                lambda n: np.power(np.sqrt(self.n), -1) * np.exp(1j * self.__k(i) * n), (self.n,), dtype=int)

            states.append(np.eye(self.n).dot(weights))

        return energies, np.stack(states, axis=0)

    def __init_psi_zero(self):
        psi_zero = np.zeros(self.n)
        psi_zero[self.site_zero] = 1

        return psi_zero

    def __init_momentum_zero(self, momentum_state):
        psi_zero = np.zeros(self.n)
        psi_zero[momentum_state] = 1

        return psi_zero

    def __momentum_zero_velocity(self, momentum_state):
        v_zero = -2 * self.a * self.hopping_amp * np.sin(self.a * self.__k(momentum_state))  # add self.a

        return v_zero

    def compute_detection_site(self, prev_detector, t, momentum_state):
        v_zero = self.__momentum_zero_velocity(momentum_state)

        detection_site = (prev_detector + (t * v_zero)) % self.n

        print("detection :", detection_site, "v :", v_zero, "detection: ", int(detection_site))

        return int(np.ceil(detection_site))

    def compute_psi_tau(self, taus):
        psi_tau = self.__init_psi_zero()

        psi_tau_states_basis = np.linalg.solve(self.states, psi_tau)
        psi_tau_states_basis = psi_tau_states_basis / np.linalg.norm(psi_tau_states_basis)

        time = np.linspace(0, taus[-1], self.tau_interval * len(taus))

        psi_time_series = []
        probabilities_time_series = []

        detection_counter = 0

        for tau in taus:

            for idx in range(self.tau_interval):
                tic = time[idx + (detection_counter * self.tau_interval)]

                psi_tau_states_basis_tic = np.diag(np.exp(-1j * tic * self.energies)).dot(psi_tau_states_basis)

                psi_tau_tic = self.states.dot(psi_tau_states_basis_tic)
                psi_tau_tic = psi_tau_tic / np.linalg.norm(psi_tau_tic)

                psi_time_series.append(psi_tau_tic)
                probabilities_time_series.append(np.power(np.abs(psi_tau_tic), 2))

            if self.enable_detector and ((tau + 1) % self.detector_frequency) == 0:
                psi_collapse = psi_time_series[-1]

                psi_collapse[self.detector] = 0
                psi_tau_tic = psi_collapse / np.linalg.norm(psi_collapse)

                psi_time_series[-1] = psi_tau_tic
                probabilities_time_series[-1] = np.square(np.abs(psi_tau_tic))

                psi_tau_states_basis = np.linalg.solve(self.states, psi_time_series[-1])
                psi_tau_states_basis = psi_tau_states_basis / np.linalg.norm(psi_tau_states_basis)

                detection_counter = 0

            else:
                detection_counter = detection_counter + 1

        return time, psi_time_series, probabilities_time_series

    def compute_momentum_tau(self, taus, momentum_state):
        detection_site = self.detector
        momentum_zero = self.__init_momentum_zero(momentum_state)
        psi_momentum_tau = momentum_zero

        time = np.linspace(0, taus[-1], self.tau_interval * len(taus))

        psi_time_series = []
        probabilities_time_series = []

        detection_counter = 0

        for tau in taus:

            for idx in range(self.tau_interval):
                tic = time[idx + (detection_counter * self.tau_interval)]

                psi_momentum_tau_tic = np.diag(np.exp(-1j * tic * self.energies)).dot(psi_momentum_tau)

                psi_tau_tic = self.states.dot(psi_momentum_tau_tic)
                psi_tau_tic = psi_tau_tic / np.linalg.norm(psi_tau_tic)
                psi_time_series.append(psi_tau_tic)
                probabilities_time_series.append(np.square(np.abs(psi_tau_tic)))

            if self.enable_detector and ((tau + 1) % self.detector_frequency) == 0:
                if self.enable_detector_velocity:
                    detection_site = self.compute_detection_site(self.detector, tau, momentum_state)

                psi_time_series[-1][detection_site] = 0
                psi_collapse = psi_time_series[-1]
                psi_tau_tic = psi_collapse / np.linalg.norm(psi_collapse)

                psi_time_series[-1] = psi_tau_tic
                probabilities_time_series[-1] = np.square(np.abs(psi_tau_tic))

                psi_momentum_tau = np.linalg.solve(self.states, psi_time_series[-1])
                psi_momentum_tau = psi_momentum_tau / np.linalg.norm(psi_momentum_tau)

                detection_counter = 0

            else:
                detection_counter = detection_counter + 1

        return time, psi_time_series, probabilities_time_series


def main():
    ring = Ring()

    print(ring.states)
    print(ring.energies)


if __name__ == '__main__':
    main()
