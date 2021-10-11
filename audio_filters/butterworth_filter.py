from math import sqrt, sin, tau, cos

from audio_filters.iir_filter import IIRFilter


class ButterworthFilter:
    """
    Create 2nd-order IIR filters with Butterworth design.

    Code based on https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html
    Alternatively you can use scipy.signal.butter, which should yield the same results.
    """

    @staticmethod
    def make_lowpass(frequency: int, samplerate: int, q_factor: float = 1 / sqrt(2)) -> IIRFilter:
        """
        Creates a low-pass filter

        >>> ButterworthFilter.make_lowpass(1000, 48000)
        <audio_filters.iir_filter.IIRFilter object at 0x7f3dbb93d040>
        """
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)

        b0 = (1 - _cos) / 2
        b1 = 1 - _cos

        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha

        filt = IIRFilter(2)
        filt.set_coefficients([a0, a1, a2], [b0, b1, b0])
        return filt

    @staticmethod
    def make_highpass(frequency: int, samplerate: int, q_factor: float = 1 / sqrt(2)) -> IIRFilter:
        """
        Creates a high-pass filter

        >>> ButterworthFilter.make_highpass(1000, 48000)
        <audio_filters.iir_filter.IIRFilter object at 0x7f3dbb93d040>
        """
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)

        b0 = (1 + _cos) / 2
        b1 = - 1 - _cos

        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha

        filt = IIRFilter(2)
        filt.set_coefficients([a0, a1, a2], [b0, b1, b0])
        return filt

    @staticmethod
    def make_bandpass(frequency: int, samplerate: int, q_factor: float = 1 / sqrt(2)) -> IIRFilter:
        """
        Creates a band-pass filter

        >>> ButterworthFilter.make_bandpass(1000, 48000)
        <audio_filters.iir_filter.IIRFilter object at 0x7f3dbb93d040>
        """
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)

        b0 = _sin / 2
        b1 = 0
        b2 = - b0

        a0 = 1 + alpha
        a1 = -2 * _cos
        a2 = 1 - alpha

        filt = IIRFilter(2)
        filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
        return filt

    @staticmethod
    def make_allpass(frequency: int, samplerate: int, q_factor: float = 1 / sqrt(2)) -> IIRFilter:
        """
        Creates an all-pass filter

        >>> ButterworthFilter.make_allpass(1000, 48000)
        <audio_filters.iir_filter.IIRFilter object at 0x7f3dbb93d040>
        """
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)

        b0 = 1 - alpha
        b1 = -2 * _cos
        b2 = 1 + alpha

        filt = IIRFilter(2)
        filt.set_coefficients([b2, b1, b0], [b0, b1, b2])
        return filt

    @staticmethod
    def make_peak(frequency: int, samplerate: int, gain_db: float, q_factor: float = 1 / sqrt(2)) -> IIRFilter:
        """
        Creates a peak filter

        >>> ButterworthFilter.make_peak(1000, 48000, 6)
        <audio_filters.iir_filter.IIRFilter object at 0x7f3dbb93d040>
        """
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        big_a = 10 ** (gain_db / 40)

        b0 = 1 + alpha * big_a
        b1 = -2 * _cos
        b2 = 1 - alpha * big_a
        a0 = 1 + alpha / big_a
        a1 = -2 * _cos
        a2 = 1 - alpha / big_a

        filt = IIRFilter(2)
        filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
        return filt

    @staticmethod
    def make_lowshelf(frequency: int, samplerate: int, gain_db: float, q_factor: float = 1 / sqrt(2)) -> IIRFilter:
        """
        Creates a low-shelf filter

        >>> ButterworthFilter.make_lowshelf(1000, 48000, 6)
        <audio_filters.iir_filter.IIRFilter object at 0x7f3dbb93d040>
        """
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        big_a = 10 ** (gain_db / 40)
        pmc = (big_a+1) - (big_a-1)*_cos
        ppmc = (big_a+1) + (big_a-1)*_cos
        mpc = (big_a-1) - (big_a+1)*_cos
        pmpc = (big_a-1) + (big_a+1)*_cos
        aa2 = 2*sqrt(big_a)*alpha

        b0 = big_a * (pmc + aa2)
        b1 = 2 * big_a * mpc
        b2 = big_a * (pmc - aa2)
        a0 = ppmc + aa2
        a1 = -2 * pmpc
        a2 = ppmc - aa2

        filt = IIRFilter(2)
        filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
        return filt

    @staticmethod
    def make_highshelf(frequency: int, samplerate: int, gain_db: float, q_factor: float = 1 / sqrt(2)) -> IIRFilter:
        """
        Creates a high-shelf filter

        >>> ButterworthFilter.make_highshelf(1000, 48000, 6)
        <audio_filters.iir_filter.IIRFilter object at 0x7f3dbb93d040>
        """
        w0 = tau * frequency / samplerate
        _sin = sin(w0)
        _cos = cos(w0)
        alpha = _sin / (2 * q_factor)
        big_a = 10 ** (gain_db / 40)
        pmc = (big_a+1) - (big_a-1)*_cos
        ppmc = (big_a+1) + (big_a-1)*_cos
        mpc = (big_a-1) - (big_a+1)*_cos
        pmpc = (big_a-1) + (big_a+1)*_cos
        aa2 = 2*sqrt(big_a)*alpha

        b0 = big_a * (ppmc + aa2)
        b1 = -2 * big_a * pmpc
        b2 = big_a * (ppmc - aa2)
        a0 = pmc + aa2
        a1 = 2 * mpc
        a2 = pmc - aa2

        filt = IIRFilter(2)
        filt.set_coefficients([a0, a1, a2], [b0, b1, b2])
        return filt
