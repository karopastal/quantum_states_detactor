from src.detector_sites import DetectorSites
from src.detector_momentum import DetectorMomentum

"""
1. 2 sites without detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    2, 1, 100, 0, 0, 1, 20, 0.1, False

title = 'Probability Density'
path = 'docs/examples/1_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)

"""
2.1 100 sites without detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    100, 1, 100, 0, 50, 1, 20, 1, False

title = 'Probability Density'
path = 'docs/examples/2_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)


"""
2.2 101 sites without detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    101, 1, 100, 0, 50, 1, 20, 1, False

title = 'Probability Density'
path = 'docs/examples/2_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)

"""
3.1 100 Sites with detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    100, 1, 100, 0, 50, 1, 20, 1, True

title = 'Probability Density'
path = 'docs/examples/3_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)


"""
3.2 101 Sites with detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    101, 1, 100, 0, 50, 1, 20, 1, True

title = 'Probability Density'
path = 'docs/examples/3_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)

"""
4.1 100 Sites with detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    100, 1, 100, 25, 50, 1, 20, 1, True

title = 'Probability Density'
path = 'docs/examples/4_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)


"""
4.2 101 Sites with detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    101, 1, 100, 25, 50, 1, 20, 1, True

title = 'Probability Density'
path = 'docs/examples/4_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)

"""
4.3 20 Sites with detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    20, 1, 100, 0, 10, 1, 20, 0.5, True

title = 'Probability Density'
path = 'docs/examples/4_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)

"""
4.4 21 Sites with detector
"""

n, a, taus, site_zero, detector, detector_frequency, tau_interval, hopping_amp, enable_detector = \
    21, 1, 100, 0, 10, 2, 20, 0.5, True

title = 'Probability Density'
path = 'docs/examples/4_sites_n_%s_site_zero_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, site_zero, detector, hopping_amp, enable_detector)

detector_sites = DetectorSites(n=n,
                               a=a,
                               taus=taus,
                               site_zero=site_zero,
                               detector=detector,
                               detector_frequency=detector_frequency,
                               tau_interval=tau_interval,
                               hopping_amp=hopping_amp,
                               enable_detector=enable_detector)

detector_sites.save_plot(title=title, path=path)

"""
6.1 100 Momentum  detector
"""

n, a, taus, momentum_state, detector, detector_frequency, tau_interval, hopping_amp, enable_detector, enable_detector_velocity = \
    100, 1, 50, 50, 50, 5, 10, 2, True, False

title = 'Probability Density'
path = 'docs/examples/6_momentum_n_%s_m_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, momentum_state, detector, hopping_amp, enable_detector)

detector_momentum = DetectorMomentum(n=n,
                                     a=1,
                                     taus=taus,
                                     detector=detector,
                                     detector_frequency=detector_frequency,
                                     tau_interval=tau_interval,
                                     hopping_amp=hopping_amp,
                                     momentum_state=momentum_state,
                                     enable_detector=enable_detector,
                                     enable_detector_velocity=enable_detector_velocity)

detector_momentum.save_plot(title=title, path=path)

"""
6.2 101 Momentum without detector
"""

n, a, taus, momentum_state, detector, detector_frequency, tau_interval, hopping_amp, enable_detector, enable_detector_velocity = \
    101, 1, 50, 50, 50, 5, 10, 2, True, False

title = 'Probability Density'
path = 'docs/examples/6_momentum_n_%s_m_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, momentum_state, detector, hopping_amp, enable_detector)

detector_momentum = DetectorMomentum(n=n,
                                     a=1,
                                     taus=taus,
                                     detector=detector,
                                     detector_frequency=detector_frequency,
                                     tau_interval=tau_interval,
                                     hopping_amp=hopping_amp,
                                     momentum_state=momentum_state,
                                     enable_detector=enable_detector,
                                     enable_detector_velocity=enable_detector_velocity)

detector_momentum.save_plot(title=title, path=path)

"""
10.1 100 Momentum with detector and velocity
"""

n, a, taus, momentum_state, detector, detector_frequency, tau_interval, hopping_amp, enable_detector, enable_detector_velocity = \
    200, 1, 100, 50, 101, 5, 5, 1, True, True

title = 'Probability Density'
path = 'docs/examples/10_momentum_n_%s_m_%s_detector_%s_c_%s_enable_%s.jpeg' % \
       (n, momentum_state, detector, hopping_amp, enable_detector)

detector_momentum = DetectorMomentum(n=n,
                                     a=1,
                                     taus=taus,
                                     detector=detector,
                                     detector_frequency=detector_frequency,
                                     tau_interval=tau_interval,
                                     hopping_amp=hopping_amp,
                                     momentum_state=momentum_state,
                                     enable_detector=enable_detector,
                                     enable_detector_velocity=enable_detector_velocity)

detector_momentum.save_plot(title=title, path=path)
