import numpy as np

def GetFFT(pF):
    cF = pF["sF"] / 2

    # Fast Fourier Transform
    NFFT = 2 ** int(np.ceil(np.log2(pF["sp"])) + 1)  # Next power of 2 from the number of samples
    dataf = np.fft.fft(pF["data"], NFFT) / pF["sp"]  # Gets the fast Fourier transform
    pF["fftData"] = 2 * np.abs(dataf[0:NFFT // 2 + 1, :])  # Get the half of the data considering absolute values,
    # since it is symmetric and we
    # only look at the half, it is multiplied by 2

    pF["fftData"][0, :] = 0  # The first element is set to 0 to reduce artifacts of low frequencies.

    pF["fftDataT"] = np.sum(pF["fftData"], axis=0)  # Sum of all frequency contributions

    pF["fV"] = (pF["sF"] / 2) * np.linspace(0, 1, NFFT // 2 + 1)  # Creates the frequency vector

    # Plot for visualization if required
    # import matplotlib.pyplot as plt
    # plt.figure()
    # plt.plot(pF["fV"], pF["fftData"][:, 0])

    # Cut the matrix to cF for analysis
    cF = 1000  # Cut frequency for feature estimation
    # If sF > 1 kHz, the estimation of frequency-related features
    # will be within 0 to 1 kHz
    if pF["fV"][-1] > cF:
        cS = int(round(cF * len(pF["fftData"][:, 0]) / (pF["sF"] / 2)))
        pF["fftData"] = pF["fftData"][:cS, :]
        pF["fV"] = pF["fV"][:cS]

    return pF
    