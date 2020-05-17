def besselCorrection(std, n):
	return std*n/(n-1)**0.5 #Bessel's correction for unbiased variance

