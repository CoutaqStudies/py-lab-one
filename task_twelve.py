def get_frames(signal, size, overlap):
    output = list()
    if 0>overlap>=1: raise ValueError("Overlap cant be >1 or <0 i think")
    sig_len = len(signal)
    if sig_len<=size:
        return signal
    overlapping_size = overlap*size
    n_of_elems = int((sig_len/overlapping_size)-1)
    for i in range(n_of_elems):
        if i == 0:
            output.append(signal[0:size+1])
        else:
            output.append(signal[(size-overlapping_size)*i:(size+overlapping_size)*i+1])
    return output
