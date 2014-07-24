def inverse_linear_cdf(y):
    y = y * 255 #denormalization
    y = round(y) #discrete approximations
    return y


def inverse_log_cdf(y):
    y = y * log(255)
    y = exp(y)
    return y


def inverse_parabolic_cdf(y):
    y = (y * 255)**2
    y = round(sqrt(y))
    return y

def curves(img):
    [hist, bins] = np.histogram(img.ravel(), 255, [0, 255])
    print "hist", hist
    plt.plot(hist)
    plt.show()
    #normalized cumsum of the histogram
    cumulative_sum = np.cumsum(hist)
    cumsum_max = max(cumulative_sum)
    cdf = cumulative_sum/cumsum_max #normalized cumsum