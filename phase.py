import numpy as np
from pyphs import PhaseSpace

# Define the parameters of the first phase-type distribution
T1 = np.array([[-1, 0.5], [0.2, -0.3]])
D1 = np.array([1, 0])

# Define the parameters of the second phase-type distribution
T2 = np.array([[-0.5, 0.1], [0.3, -0.2]])
D2 = np.array([0.5, 0.5])

# Define the phase spaces of the two distributions
ps1 = PhaseSpace(T1, D1)
ps2 = PhaseSpace(T2, D2)

# Convolve the two phase spaces
conv_ps = ps1.convolve(ps2)

# Evaluate the PDF of the convolution at a point
x = 1.5
pdf_val = conv_ps.pdf(x)
print("PDF value at x =", x, ":", pdf_val)
