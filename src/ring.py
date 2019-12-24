import numpy as np


class Ring:
    def __init__(self, n=3, site_zero=0, detector=0, tau_interval=25, hopping_amp=1):
        if n < 3:
            raise Exception('Oops, valid Ring has no less than three sites, try again..')

        self.n = n
        self.site_zero = site_zero
        self.detector = detector
        self.tau_interval = tau_interval
        self.hopping_amp = hopping_amp
        self.hamiltonian = self.__init_hamiltonian()
        self.energies, self.states = self.__get_states_and_energies()

    def __init_hamiltonian(self):
        hamiltonian = np.zeros((self.n, self.n))
        frequencies = np.ones(self.n - 1)*self.hopping_amp
        np.fill_diagonal(hamiltonian[1:], frequencies)
        np.fill_diagonal(hamiltonian[:, 1:], frequencies)

        hamiltonian[0, self.n - 1] = self.hopping_amp
        hamiltonian[self.n - 1, 0] = self.hopping_amp

        return hamiltonian

    def __get_states_and_energies(self):
        (energies, states) = np.linalg.eig(self.hamiltonian)

        return energies, states

    def __init_psi_zero(self):
        psi_zero = np.zeros(self.n)
        psi_zero[self.site_zero] = 1

        return psi_zero

    def compute_psi_tau(self, taus):
        """
             psi_tau_* : wave-function at sites bases
             psi_tau_states_basis_* : wave-function at hamiltonian eigensates bases

             time_series :
             probabilities_series :
         """

        psi_tau = self.__init_psi_zero()
        psi_tau_states_basis = np.linalg.solve(self.states, psi_tau)

        time = np.linspace(0, taus[-1], self.tau_interval*len(taus))
        psi_time_series = []
        probabilities_time_series = []

        for tau in taus:

            for idx in range(self.tau_interval):
                tic = time[idx + tau*self.tau_interval]
                psi_tau_states_basis_tic = np.diag(np.exp(tic*self.energies*1.j)).dot(psi_tau_states_basis)

                psi_tau_tic = self.states.dot(psi_tau_states_basis_tic)
                psi_tau_tic = psi_tau_tic / np.linalg.norm(psi_tau_tic)
                psi_time_series.append(psi_tau_tic)
                probabilities_time_series.append(np.square(np.abs(psi_tau_tic)))

            # once we measured at self.site the wave function collapses
            # detector = int(int(self.site_zero + self.n)/2)

            psi_time_series[-1][self.detector] = 0
            psi_collapse = psi_time_series[-1]
            psi_tau_tic = psi_collapse / np.linalg.norm(psi_collapse)

            psi_time_series[-1] = psi_tau_tic
            probabilities_time_series[-1] = np.square(np.abs(psi_tau_tic))

            psi_tau_states_basis = np.linalg.solve(self.states, psi_time_series[-1])

        return time, psi_time_series, probabilities_time_series


def main():
    ring = Ring()

    print(ring.hamiltonian)
    print(ring.energies)

    # print(ring.hamiltonian.dot(ring.states[1][1]))
    # print(np.dot(ring.hamiltonian[:, :], ring.states[:, 2]))
    # print(np.dot(ring.hamiltonian[:, :], ring.states[:, 2])/ring.energies[2])

    # convert to new basis
    # a = np.linalg.solve(ring.states, np.array([1, 0, 0]))

    # convert back
    # print(ring.states.dot(a))


if __name__ == '__main__':
    main()
