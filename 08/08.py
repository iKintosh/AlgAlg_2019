import numpy as np


def read_inputs():
    coeffs = list(map(float, input().split()))
    return np.array(coeffs)


def print_result(result):
    print(' '.join(f'{x.real},{x.imag}' for x in result))


def to2power(coeffs):
    n = coeffs.shape[0]
    if (n & (n - 1)) == 0:
        return coeffs
    new_n = int(2 ** np.ceil(np.log2(n)))
    coeffs = np.append(coeffs, np.zeros(new_n - n))
    return coeffs


def fft(coeffs):
    n = coeffs.shape[0]
    if n == 1:
        return coeffs

    factor = np.exp(2j * np.pi * np.arange(n) / n)
    y_even = fft(coeffs[::2])
    y_odd = fft(coeffs[1::2])
    y = np.concatenate([y_even + factor[:n // 2] * y_odd, y_even + factor[n // 2:] * y_odd])
    return y


if __name__ == '__main__':
    coeffs = read_inputs()
    result = fft(coeffs)
    print_result(result)
