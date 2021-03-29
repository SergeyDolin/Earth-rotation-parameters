import numpy as np

# Return (dlnpr) (Point 1.1)
def Param4():
    try:
        with open("Data/param4.txt", "r") as readFile:
            for read in readFile:
                return 90, float(read) * 365.25
    except IOError:
        print("Error file")


# (Point 1.2)
def rdk():
    i = 0
    kod = [12.390122175216670, 2.832145333290100, 20.112080812454220, 15.690995275974270,
           3.823979675769806, 9.120352447032928, 13.699975907802580, 11.079364597797390,
           16.337700843811040, 23.027701914310460, 7.377863466739655, 19.226244270801540,
           18.344215989112850, 10.244575619697570, 8.497311115264893, 22.905920863151550,
           6.783666491508484, 17.759827792644500, 1.257015407085419, 21.546307027339940,
           5.033347547054291, 14.981535315513610, 4.134304285049438]
    ret = []
    try:
        with open("Data/param2.txt", "r") as readFile:
            for read in readFile:
                ret.append(float(read)/kod[i])
                i += 1
                if i >= 23:
                    i = 0
            return ret
    except IOError:
        print("Error file")

# (Point 1.3)
def Param2():
    ff = rdk()

    ng = 250    # Harmonic number
    nput = int(100*len(ff)+0.5)
    perut = np.zeros((nput, ng))
    amput = np.zeros((nput, ng))
    fazut = np.zeros((nput, ng))

    perxp = np.zeros((nput, ng))
    ampxp = np.zeros((nput, ng))
    fazxp = np.zeros((nput, ng))

    peryp = np.zeros((nput, ng))
    ampyp = np.zeros((nput, ng))
    fazyp = np.zeros((nput, ng))

    for i in range(nput):
        for j in range(ng):
            perut[i, j] = 1 / (ff[j] * 1000)
            amput[i, j] = ff[j] * 100
            fazut[i, j] = ff[j]
            perxp[i, j] = 1 / (ff[j] * 10000)
            ampxp[i, j] = ff[j] * 100
            fazxp[i, j] = ff[j]

    peryp = perxp
    ampyp = ampxp
    fazyp = fazxp

